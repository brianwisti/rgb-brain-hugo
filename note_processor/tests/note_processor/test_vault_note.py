"""Test note processing logic."""

from pathlib import Path

import frontmatter
import pytest

from note_processor.lib.vault_note import (
    NOTE_LINK,
    NoteLink,
    VaultNote,
    VaultResource,
)


def generate_md_path(faker):
    """Return a random Markdown file path."""
    return Path(faker.file_path(extension="md"))


def generate_post(faker):
    """Return a random frontmatter.Post."""
    meta = {"title": faker.sentence()}
    content = faker.text()
    handler = None

    return frontmatter.Post(content, handler, **meta)


def generate_post_with_note_links(faker, note_link_list):
    """Return a random frontmatter.Post with note links."""
    meta = {"title": faker.sentence()}
    content = generate_text_with_note_links(faker, note_link_list)
    handler = None

    return frontmatter.Post(content, handler, **meta)


def generate_text_with_note_links(faker, note_link_list):
    """Return a string of text with note links."""
    return " ".join(
        [f"{note_link_as_markdown(link)} {faker.text()}" for link in note_link_list]
    )


def note_link_as_markdown(link: NoteLink):
    """Return a Markdown-formatted link."""
    return f"[{link.link_text}]({link.target.path})"


# Tell pylint not to worry about:
# - Function docstrings
# - Class docstrings
# - Redefined names from outer scope
# pylint: disable=C0115,C0116,W0621


@pytest.fixture
def md_path(faker):
    return generate_md_path(faker)


@pytest.fixture
def md_paths(faker, limit=10):
    return [generate_md_path(faker) for _ in range(limit)]


@pytest.fixture
def post(faker):
    return generate_post(faker)


@pytest.fixture
def markdown_link(faker, md_path):
    link_text = faker.word()
    text = f"[{link_text}]({md_path})"
    return text


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
def note_link(faker, vault_note, md_path):
    link_text = faker.word()

    return NoteLink(vault_note, VaultResource(md_path), link_text)


@pytest.fixture
def note_links(faker, vault_note, md_paths):
    link_text = faker.word()

    return [
        NoteLink(vault_note, VaultResource(md_path), link_text) for md_path in md_paths
    ]


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
