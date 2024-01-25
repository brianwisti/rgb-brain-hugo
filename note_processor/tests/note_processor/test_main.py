"""Testing for note_processor.main module."""

import pytest

from note_processor.lib.main import Backlinks

# Tell pylint not to worry about:
# - Function docstrings
# - Class docstrings
# - Redefined names from outer scope
# pylint: disable=C0115,C0116,W0621


@pytest.fixture
def content_dir(tmp_path):
    return tmp_path / "content"


class TestBacklinks:
    def test_empty(self, content_dir):
        backlinks = Backlinks(content_dir)

        assert not backlinks.backlinks

    def test_with_linked_notes(self, content_dir, linked_vault_notes):
        backlinks = Backlinks.from_notes(content_dir, linked_vault_notes)
        output = backlinks.to_dict()
        import rich

        rich.inspect(output)
        rich.inspect(linked_vault_notes[1].internal_links)
        assert len(backlinks.backlinks) == 1
