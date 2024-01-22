"""Test structure and contents of site Atom feeds."""

from urllib.parse import urlparse
from pathlib import Path
from typing import Any, Dict

import feedparser
import pytest
import rich

SITE_BUILD_DIR = "public"


@pytest.fixture(scope="session")
def site_build() -> Path:
    """Return a Path pointing at generated site files."""
    path = Path(SITE_BUILD_DIR)

    if not path.is_dir():
        raise ValueError(f"Site build dir {SITE_BUILD_DIR} does not exist.")

    return path


@pytest.fixture(scope="session")
def main_feed_file(site_build) -> Path:
    return site_build / "index.xml"


@pytest.fixture(scope="session")
def main_feed(main_feed_file):
    return feedparser.parse(str(main_feed_file))


class TestFeedsGenerated:
    def test_main_feed_generated(self, main_feed_file):
        assert main_feed_file.is_file()

    def test_category_feeds_generated(self, site_build):
        feed_filename = "index.xml"
        category_path = site_build / "category"

        for child in category_path.iterdir():
            if not child.is_dir():
                continue

            child_feed = child / feed_filename
            assert child_feed.is_file()


class TestMainFeedContent:
    def test_item_count(self, main_feed):
        expected_count = 10
        assert len(main_feed.entries) == expected_count

    def test_only_blog_articles_in_feed(self, main_feed):
        # <link>https://randomgeekery.org/blog/2022/added-nano-based-emacs-config/</link>
        links = [urlparse(entry["link"]).path for entry in main_feed.entries]
        rich.print(links)
        assert not any(link for link in links if link.split("/")[1] != "post")
