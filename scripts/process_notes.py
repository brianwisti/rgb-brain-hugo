#!/usr/bin/env python

import logging
from dataclasses import dataclass, field
from pathlib import Path

import frontmatter
from rich.logging import RichHandler

CONTENT_DIR = "content";
NOTE_LINK = r"""
  \[
    (?<title> [^\]]+? )
  \]
  \(
    (?<path> [^\)]+? \.md)
  \)
"""

logging.basicConfig(level=logging.INFO, handlers=[RichHandler()])


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

        self.post = post


def main():
    logging.info("Yo")
    content_path = Path(CONTENT_DIR)

    for note_path in content_path.glob("**/*.md"):
        logging.info("Path: %s", note_path)
        note = VaultNote(note_path)

        if note.is_dirty:
            note.path.write_text(frontmatter.dumps(note.post))




if __name__ == "__main__":
    main()
