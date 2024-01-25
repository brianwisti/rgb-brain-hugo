"""Logic for handling Vault notes."""

import logging
import re
from dataclasses import dataclass, field
from pathlib import Path

import frontmatter

# Obsidian Markdown: callouts
CALLOUT_BLOCK = re.compile(
    r"""> \s
        \\\[\! (?P<callout_type>[A-Z]+) \\\]
        (?: \s (?P<title> [^ \n ]+?))?
        \n
    """,
    re.VERBOSE,
)

# Obsidian Markdown: wiki links
NOTE_LINK = re.compile(
    r"""
  \[
    ( [^\]]+? )
  \]
  \(
    ( [^\)]+? \.md)
  \)
""",
    re.VERBOSE,
)


def callout_title(match):
    """Return a formatted title for callouts."""
    groups = match.groupdict()
    callout_type = groups["callout_type"]

    if matched_title := groups.get("title"):
        title = matched_title
    else:
        title = callout_type

    logging.debug("Found %s, using %s", groups, title)
    return f"> **{title}**\n>\n"


@dataclass
class VaultResource:
    """Some file in the vault."""

    # Where this resource is located
    path: Path

    def get_name(self):
        """Return a handy stringified reference to this resource."""
        return self.path.stem


@dataclass
class NoteLink:
    """A link between two internal resources."""

    # Where the link was found
    source: VaultResource

    # Where the link points to
    target: VaultResource

    # what the user sees
    link_text: str


@dataclass
class VaultNote(VaultResource):
    """Tracks what a note needs to know about itself."""

    note: frontmatter.Post
    is_dirty: bool = False
    internal_links: list[NoteLink] = field(init=False, default_factory=list)

    def __post_init__(self):
        self.__ensure_title()
        self.__find_links()
        self.__adjust_content()

    @property
    def content(self):
        """Return the note's raw Markdown content."""
        return self.note.content

    @content.setter
    def content(self, new_content):
        """
        Set the note's raw Markdown content.

        Changing the content will mark the note as dirty.
        """
        self.note.content = new_content
        self.is_dirty = True

    @property
    def meta(self):
        """Return a dictionary of the note's frontmatter metadata."""
        return self.note.metadata

    @property
    def title(self):
        """Return the note's title."""
        return self.meta["title"]

    @classmethod
    def from_path(cls: type["VaultNote"], path: Path):
        """Return a VaultNote by processing the file at a given path."""
        post = frontmatter.loads(path.read_text(encoding="utf-8"))
        is_dirty = False
        updated_content = re.sub(CALLOUT_BLOCK, callout_title, post.content)

        if updated_content != post.content:
            post.content = updated_content
            logging.debug("updated content")
            is_dirty = True

        return cls(path=path, note=post, is_dirty=is_dirty)

    def add_link(self, resource: VaultResource, link_text: str):
        """Remembers a vault link from this note."""
        self.internal_links.append(NoteLink(self, resource, link_text))

    def dumps(self):
        """Return the note's Markdown content as a string."""
        return frontmatter.dumps(self.note)

    def write_file(self):
        """Write the note's Markdown content to its file."""
        self.path.write_text(self.dumps(), encoding="utf-8")

    def __adjust_content(self):
        """
        Process Obsidian specifics in the note's content.

        This method will update the note's content and mark it as dirty if
        necessary.
        """
        updated_content = re.sub(CALLOUT_BLOCK, callout_title, self.note.content)

        if updated_content != self.note.content:
            self.note.content = updated_content
            logging.debug("updated content")
            self.is_dirty = True

    def __ensure_title(self):
        """Ensure that the note has a title.

        If frontmatter has no title field, add one from the note's filename.
        Changing the title will mark the note as dirty.
        """
        if "title" not in self.meta:
            self.meta["title"] = self.path.stem
            self.is_dirty = True

    def __find_links(self):
        """Find all internal links in the note's content."""
        for match in NOTE_LINK.finditer(self.content):
            link_text, link_path = match.groups()
            self.add_link(VaultResource(Path(link_path)), link_text)
