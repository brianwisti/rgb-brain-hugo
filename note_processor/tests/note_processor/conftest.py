"""Shared fixtures for note_processor tests."""

from pathlib import Path

import frontmatter
import pytest

from note_processor.lib.vault_note import NoteLink, VaultNote, VaultResource


def generate_links_from_note(faker, note: VaultNote, limit=10) -> list[NoteLink]:
    """Return a list of links from a note."""
    return [
        NoteLink(note, VaultResource(generate_md_path(faker)), faker.word())
        for _ in range(limit)
    ]


def generate_links_to_note(faker, note: VaultNote, limit=10) -> list[NoteLink]:
    """Return a list of links for a note."""
    return [
        NoteLink(VaultResource(generate_md_path(faker)), note, faker.word())
        for _ in range(limit)
    ]


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
def vault_note_with_redirects(post, md_path, faker):
    post.metadata["aliases"] = [faker.word() for _ in range(3)]
    return VaultNote(md_path, post)

@pytest.fixture
def note_link(faker, vault_note, md_path):
    link_text = faker.word()

    return NoteLink(vault_note, VaultResource(md_path), link_text)


@pytest.fixture
def note_links(faker, vault_note):
    return generate_links_from_note(faker, vault_note)


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


@pytest.fixture
def linked_vault_notes(faker, vault_note):
    notes = [vault_note]
    note_links = generate_links_to_note(faker, vault_note)

    for note_link in note_links:
        note = generate_post_with_note_links(faker, [note_link])
        notes.append(VaultNote(note_link.source.path, note))

    return notes
