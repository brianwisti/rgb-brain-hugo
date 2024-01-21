#!/usr/bin/env python

import logging
from pathlib import Path

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


def main():
    logging.info("Yo")
    content_path = Path(CONTENT_DIR)

    for note_path in content_path.glob("**/*.md"):
        logging.info("Path: %s", note_path)




if __name__ == "__main__":
    main()
