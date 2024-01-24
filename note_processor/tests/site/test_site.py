"""Automatic tests for the generated site."""

import io
import subprocess
from pathlib import Path
from typing import cast

import pandas as pd
import pytest
import rich
from bs4 import BeautifulSoup
from yarl import URL

# Tell pylint not to worry about:
# - Function docstrings
# - Class docstrings
# - Redefined names from outer scope
# pylint: disable=C0115,C0116,W0621


def load_hugo_pages(site_path: Path) -> pd.DataFrame:
    """Return data that Hugo reports about site contents."""
    cmd = ("hugo", "list", "all")
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, cwd=site_path)

    if not process.stdout:
        raise ValueError(f"No output from {cmd}")

    csv = io.StringIO(process.stdout.read().decode())
    data = cast(pd.DataFrame, pd.read_csv(csv, index_col=0))
    csv.close()
    data["out"] = data["permalink"].apply(lambda s: URL(s).path[1:] + "index.html")

    return data


HUGO_SITE_PATH = Path("site")
HUGO_BUILD_PATH = HUGO_SITE_PATH / "public"
HUGO_PAGES = load_hugo_pages(HUGO_SITE_PATH)
PAGE_HTML_PATHS = [HUGO_BUILD_PATH / page for page in HUGO_PAGES["out"].to_list()]
PLAUSIBLE_DOMAIN = "randomgeekery.org"
PLAUSIBLE_SRC = "https://plausible.io/js/script.js"
PLAUSIBLE_TOKEN = (
    f'<script defer data-domain="{PLAUSIBLE_DOMAIN}"'
    ' src="https://plausible.io/js/script.js"></script>'
)


def parse_html_path(html_path: Path) -> BeautifulSoup:
    """Return the BeautifulSoup object from parsing a Path."""
    html = html_path.read_text(encoding="utf-8")

    return BeautifulSoup(html, "html.parser")


def link_is_local(link: str | None):
    return (
        link is not None
        and not link.startswith("https://")
        and not link.startswith("http://")
        and not link.startswith("mailto:")
        and not link.startswith("tel:")
        and not link.startswith("sms:")
        and "#" not in link
    )


class TestGeneratedMarkup:
    @pytest.mark.parametrize("html_path", PAGE_HTML_PATHS, ids=str)
    def test_internal_links(self, html_path):
        soup = parse_html_path(html_path)
        links = [a.get("href") for a in soup.find_all("a")]
        local_links = [link for link in links if link_is_local(link)]

        for local_link in local_links:
            rich.print(f"{html_path} → {local_link}")
            site_link_path = HUGO_BUILD_PATH / local_link[1:]
            assert site_link_path.is_dir() or site_link_path.is_file()

    @pytest.mark.parametrize("html_path", PAGE_HTML_PATHS, ids=str)
    def test_analytics_token(self, html_path):
        soup = parse_html_path(html_path)
        scripts = [
            (script.get("data-domain"), script.get("src"))
            for script in soup.find_all("script")
        ]
        rich.print(scripts)

        assert any(
            script for script in scripts if script == (PLAUSIBLE_DOMAIN, PLAUSIBLE_SRC)
        )

    @pytest.mark.parametrize("html_path", PAGE_HTML_PATHS, ids=str)
    def test_rss_link(self, html_path):
        soup = parse_html_path(html_path)
        links = [
            link.get("href")
            for link in soup.find_all("link")
            if link.get("type") == "application/rss+xml"
        ]
        rich.print(links)
        assert any(href for href in links if href == "/index.xml")
