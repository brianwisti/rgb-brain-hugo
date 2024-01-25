"""Manages preparation of exported notes for Hugo."""

import logging
from pathlib import Path

from rich.logging import RichHandler

from const import CONTENT_DIR
from vault_note import VaultNote

logging.basicConfig(level=logging.INFO, handlers=[RichHandler()])


def main():
    """Process notes exported from Obsidian."""
    content_path = Path(CONTENT_DIR)

    for note_path in content_path.glob("**/*.md"):
        logging.debug("Path: %s", note_path)
        note = VaultNote.from_path(note_path)

        if note.is_dirty:
            logging.info("Writing %s", note.path)
            note.write_file()


if __name__ == "__main__":
    main()
