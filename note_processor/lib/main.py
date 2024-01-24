"""Manages preparation of exported notes for Hugo."""

import logging
import re
from dataclasses import dataclass, field
from pathlib import Path

import frontmatter
from rich.logging import RichHandler

from .const import CONTENT_DIR, CALLOUT

logging.basicConfig(level=logging.INFO, handlers=[RichHandler()])


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
class VaultNote:
    """Tracks what a note needs to know about itself."""

    path: Path
    post: frontmatter.Post = field(init=False)
    is_dirty: bool = False

    def __post_init__(self):
        post = frontmatter.loads(self.path.read_text(encoding="utf-8"))

        if "title" not in post.metadata:
            post.metadata["title"] = self.path.stem
            self.is_dirty = True

        updated_content = re.sub(CALLOUT, callout_title, post.content)

        if updated_content != post.content:
            post.content = updated_content
            logging.debug("updated content")
            self.is_dirty = True

        self.post = post


def main():
    content_path = Path(CONTENT_DIR)

    for note_path in content_path.glob("**/*.md"):
        logging.debug("Path: %s", note_path)
        note = VaultNote(note_path)

        if note.is_dirty:
            note.path.write_text(frontmatter.dumps(note.post), encoding="utf-8")


if __name__ == "__main__":
    main()
