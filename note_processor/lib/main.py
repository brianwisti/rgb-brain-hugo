"""Manages preparation of exported notes for Hugo."""

import json
import logging
from dataclasses import dataclass, field
from pathlib import Path

from rich.logging import RichHandler

from lib.vault_note import VaultNote

SITE_DIR = Path("site")
CONTENT_DIR = SITE_DIR / "content"
DATA_DIR = SITE_DIR / "data"
BACKLINKS_FILE = DATA_DIR / "backlinks.json"

logging.basicConfig(level=logging.INFO, handlers=[RichHandler()])


@dataclass
class BacklinkInfo:
    """Information about a backlink for serialization."""

    path: str
    title: str

    def to_dict(self):
        """Return a dictionary representation of the backlink info."""
        return {"path": self.path, "title": self.title}


@dataclass
class Backlinks:
    """All backlinks in the vault."""

    content_dir: Path
    backlinks: dict[str, list[BacklinkInfo]] = field(default_factory=dict)

    @classmethod
    def from_notes(cls, content_dir: Path, notes: list[VaultNote]):
        """Create a Backlinks instance from a list of notes."""
        backlinks = {}

        for note in notes:
            logging.debug("note: %s", note.path)

            for link in note.internal_links:
                logging.debug("link: %s", link)
                source_path = link.source.path.relative_to(content_dir)
                source_name = link.source.get_name()
                target_path = link.target.path.relative_to(content_dir)

                if str(source_path) == "_index.md":
                    source_path = "/_index.md"

                backlink = BacklinkInfo(str(source_path), source_name)
                link_target = str(target_path)

                if link_target not in backlinks:
                    backlinks[link_target] = []

                backlinks[link_target].append(backlink)

        return cls(content_dir, backlinks)

    def get_backlinks(self, note: VaultNote):
        """Return all backlinks for a note."""
        return self.backlinks.get(str(note.path), [])

    def to_dict(self):
        """Return a dictionary representation of the backlinks."""
        return {
            str(path): [backlink.to_dict() for backlink in links]
            for path, links in self.backlinks.items()
        }


def main():
    """Process notes exported from Obsidian."""
    content_dir = CONTENT_DIR.resolve()
    notes = [VaultNote.from_path(path) for path in content_dir.glob("**/*.md")]
    backlinks = Backlinks.from_notes(content_dir, notes)
    logging.debug("backlinks: %s", backlinks.to_dict())
    backlinks_json = json.dumps(backlinks.to_dict(), indent=4)
    logging.info("Writing %s", BACKLINKS_FILE)
    BACKLINKS_FILE.write_text(backlinks_json, encoding="utf-8")

    for note in notes:
        if note.is_dirty:
            logging.info("Writing %s", note.path)
            note.write_file()


if __name__ == "__main__":
    main()
