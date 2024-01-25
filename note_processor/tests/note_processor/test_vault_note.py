"""Test note processing logic."""

from pathlib import Path

import frontmatter
import pytest

from note_processor.lib.vault_note import VaultNote, VaultResource

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
def vault_resource(faker):
    path = Path(faker.file_path())
    return VaultResource(path)


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


class TestVaultResource:
    def test_get_name(self, vault_resource):
        assert vault_resource.get_name() == vault_resource.path.stem


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


class TestVaultNoteLinks:
    def test_empty(self, vault_note):
        assert len(vault_note.internal_links) == 0

    def test_add_link(self, vault_note, vault_resource, faker):
        link_text = faker.word()
        vault_note.add_link(vault_resource, link_text)

        assert len(vault_note.internal_links) > 0

    def test_add_link_sets_source(self, vault_note, vault_resource, faker):
        link_text = faker.word()
        vault_note.add_link(vault_resource, link_text)
        link = vault_note.internal_links[-1]

        assert link.source == vault_note
        assert link.target == vault_resource
        assert link.link_text == link_text

    @pytest.mark.skip(reason="Not implemented")
    def test_single_untitled_link(self):
        assert False

    @pytest.mark.skip(reason="Not implemented")
    def test_single_link_with_title(self):
        assert False


class TestVaultNoteTitle:
    def test_title_get(self, vault_note: VaultNote):
        assert vault_note.title == vault_note.meta["title"]

    def test_title_get_from_path(self, untitled_vault_note: VaultNote):
        assert untitled_vault_note.title == untitled_vault_note.get_name()

    def test_title_from_path_persists(self, untitled_vault_note: VaultNote):
        title = untitled_vault_note.title

        assert untitled_vault_note.meta["title"] == title

    def test_title_from_meta_is_not_dirty(self, vault_note: VaultNote):
        _ = vault_note.title

        assert not vault_note.is_dirty

    def test_title_from_path_is_dirty(self, untitled_vault_note: VaultNote):
        _ = untitled_vault_note.title

        assert untitled_vault_note.is_dirty
