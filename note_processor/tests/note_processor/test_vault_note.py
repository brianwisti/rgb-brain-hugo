"""Test note processing logic."""

import frontmatter
import pytest

from note_processor.lib.vault_note import NOTE_LINK, VaultNote
from .conftest import (
    generate_post_with_note_links,
    generate_text_with_note_links,
    note_link_as_markdown,
)


# Tell pylint not to worry about:
# - Function docstrings
# - Class docstrings
# - Redefined names from outer scope
# pylint: disable=C0115,C0116,W0621


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

    def test_vault_note_with_links(self, faker, md_path, note_links):
        note = generate_post_with_note_links(faker, note_links)
        vault_note = VaultNote(md_path, note)

        assert len(vault_note.internal_links) == len(note_links)

        for link, internal_link in zip(note_links, vault_note.internal_links):
            assert internal_link.source == vault_note
            assert internal_link.target == link.target
            assert internal_link.link_text == link.link_text


class TestNoteLinkPattern:
    def test_empty(self, faker):
        text = faker.sentence()
        assert len(NOTE_LINK.findall(text)) == 0

    def test_single_untitled_link(self, note_link):
        md = note_link_as_markdown(note_link)
        links = NOTE_LINK.findall(md)

        assert len(links) == 1

        link_text, link_path = links[0]
        assert link_text == note_link.link_text
        assert link_path == str(note_link.target.path)

    def test_non_note_link(self, faker):
        text = f"[{faker.word()}]({faker.url()})"
        links = NOTE_LINK.findall(text)

        assert len(links) == 0

    def test_text_with_multiple_links(self, note_links):
        md = "\n".join([note_link_as_markdown(link) for link in note_links])
        links = NOTE_LINK.findall(md)

        assert len(links) == len(note_links)

        for link, (link_text, link_path) in zip(note_links, links):
            assert link_text == link.link_text
            assert link_path == str(link.target.path)

    def test_line_with_multiple_links(self, faker, note_links):
        md = generate_text_with_note_links(faker, note_links)
        links = NOTE_LINK.findall(md)

        assert len(links) == len(note_links)

        for link, (link_text, link_path) in zip(note_links, links):
            assert link_text == link.link_text
            assert link_path == str(link.target.path)

class TestVaultNoteAliases:
    def test_default(self, vault_note):
        assert "aliases" not in vault_note.meta
    
    def test_with_redirects(self, vault_note_with_redirects):
        assert "aliases" in vault_note_with_redirects.meta
        assert "redirects" not in vault_note_with_redirects.meta

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
