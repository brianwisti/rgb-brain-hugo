"""Test note processing logic."""

from pathlib import Path

import frontmatter
import pytest

from note_processor.lib.vault_note import VaultNote

# Tell pylint not to worry about:
# - Function docstrings
# - Class docstrings
# - Redefined names from outer scope
# pylint: disable=C0115,C0116,W0621


@pytest.fixture
def post():
    meta = {"title": "My Card"}
    content = "This is my card."
    handler = None

    return frontmatter.Post(content, handler, **meta)


@pytest.fixture
def md_path(faker):
    return Path(faker.file_path(extension="md"))


@pytest.fixture
def vault_note(post, md_path):
    return VaultNote(md_path, post)


@pytest.fixture
def untitled_vault_note(vault_note):
    note = vault_note.note
    del note.metadata["title"]

    return VaultNote(vault_note.path, note)


@pytest.fixture
def vault_note_with_callout(vault_note):
    new_content = "> \\[!NOTE\\]\n> This is my card."
    note = vault_note.note
    note.content = new_content
    return VaultNote(vault_note.path, note)


class TestVaultNote:
    def test_meta_get(self, vault_note: VaultNote):
        assert vault_note.meta == vault_note.note.metadata

    def test_is_dirty_default(self, vault_note: VaultNote):
        assert not vault_note.is_dirty

    def test_dumps(self, vault_note: VaultNote):
        assert vault_note.dumps() == frontmatter.dumps(vault_note.note)


class TestVaultNoteContent:
    def test_content_get(self, vault_note: VaultNote):
        assert vault_note.content == vault_note.note.content

    def test_content_set(self, vault_note: VaultNote, faker):
        new_content = faker.sentence()
        vault_note.content = new_content

        assert vault_note.content == new_content

    def test_content_set_is_dirty(self, vault_note: VaultNote, faker):
        new_content = faker.sentence()
        vault_note.content = new_content

        assert vault_note.is_dirty

    def test_content_with_callout(self, vault_note_with_callout: VaultNote):
        assert "> **NOTE**" in vault_note_with_callout.content

    def test_content_with_callout_is_dirty(self, vault_note_with_callout: VaultNote):
        assert vault_note_with_callout.is_dirty


class TestVaultNoteTitle:
    def test_title_get(self, vault_note: VaultNote):
        assert vault_note.title == vault_note.meta["title"]

    def test_title_get_from_path(self, untitled_vault_note: VaultNote):
        assert untitled_vault_note.title == untitled_vault_note.path.stem

    def test_title_from_path_persists(self, untitled_vault_note: VaultNote):
        title = untitled_vault_note.title

        assert untitled_vault_note.meta["title"] == title

    def test_title_from_meta_is_not_dirty(self, vault_note: VaultNote):
        _ = vault_note.title

        assert not vault_note.is_dirty

    def test_title_from_path_is_dirty(self, untitled_vault_note: VaultNote):
        _ = untitled_vault_note.title

        assert untitled_vault_note.is_dirty
