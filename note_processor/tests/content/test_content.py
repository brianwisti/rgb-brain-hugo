"""Check that content sources are in good, quality shape."""

import re
from pathlib import Path
from subprocess import run

import frontmatter
import pytest

# Tell pylint not to worry about:
# - Function docstrings
# - Class docstrings
# - Redefined names from outer scope
# pylint: disable=C0115,C0116,W0621


# Setting expected folders will cause a failure when I add a new public folder
# AND THAT IS OKAY.
EXPECTED_SECTIONS = [
    "attachments",
    "card",
    "config",
    "page",
    "post",
]

CONTENT_PATH = Path("site/content")
ALL_MARKDOWN = list(CONTENT_PATH.glob("**/*.md"))
ALL_BUT_SITE_INDEX = [
    article
    for article in ALL_MARKDOWN
    if str(article.relative_to(CONTENT_PATH)) != "_index.md"
]
BLOG_POSTS = [
    article
    for article in ALL_MARKDOWN
    if article.parts[1] == "post" and article.name == "index.md"
]

CONFIG_ARTICLES = [article for article in ALL_MARKDOWN if article.parts[1] == "config"]

PAGE_ARTICLES = [
    article
    for article in ALL_MARKDOWN
    if article not in BLOG_POSTS
    and article not in CONFIG_ARTICLES
    and article.name == "index.md"
]

SECTION_PAGES = [
    article
    for article in ALL_MARKDOWN
    if article.name == "_index.md" and article not in CONFIG_ARTICLES
]

ARTIFACT_PASS = [
    "using-markdown-it-in-python",
]

ARTIFACT_PAGES = [page for page in ALL_MARKDOWN if page.stem not in ARTIFACT_PASS]

IMAGE_ARTIFACT = re.compile(r"^#\[", re.MULTILINE)


class TestSources:
    @pytest.mark.parametrize("content_path", ALL_BUT_SITE_INDEX)
    def test_section_is_expected(self, content_path: Path):
        assert content_path.relative_to(CONTENT_PATH).parts[0] in EXPECTED_SECTIONS


class TestMarkdown:
    def test_markdownlint(self):
        res = run(
            ["markdownlint", "-c", ".markdownlint.yml", "content/"],
            capture_output=True,
            check=True,
        )
        print(res.stderr.decode())
        assert res.returncode == 0

    @pytest.mark.parametrize("content_path", ARTIFACT_PAGES, ids=str)
    def test_admonition_artifact(self, content_path: Path):
        post = frontmatter.loads(content_path.read_text(encoding="utf-8"))

        assert not any(
            line for line in post.content.split("\n") if line.startswith(":::")
        )

    @pytest.mark.parametrize("content_path", ARTIFACT_PAGES, ids=str)
    def test_image_artifact(self, content_path: Path):
        post = frontmatter.loads(content_path.read_text(encoding="utf-8"))

        assert not IMAGE_ARTIFACT.search(post.content)
