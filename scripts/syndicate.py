"""
Syndicate newest post to Mastodon and Twitter.

Still just a copy and paste of what I had working for the Mastodon announcement code.
Needs some work to apply here.
"""

import csv
import json
import os
import subprocess
from dataclasses import dataclass
from io import StringIO
from pathlib import Path
from typing import Any, cast

import frontmatter
import pandas as pd
import requests
import rich
from mastodon import Mastodon
from rich.prompt import Confirm
from slugify import slugify

# I got mine stashed in a `.envrc` file
API_BASE = os.environ.get("API_BASE")
CLIENT_KEY = os.environ.get("CLIENT_KEY")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
MASTO_KEY=os.environ.get("MASTO_KEY")
MASTO_SECRET=os.environ.get("MASTO_SECRET")
MASTO_TOKEN=os.environ.get("MASTO_TOKEN")
MASTO_URL=os.environ.get("API_BASE")

TWITTER_BEARER_TOKEN=os.environ.get("MASTO_KEY")
TWITTER_API_KEY=os.environ.get("MASTO_KEY")
TWITTER_API_SECRET=os.environ.get("MASTO_KEY")
TWITTER_CLIENT_ID=os.environ.get("MASTO_KEY")
TWITTER_CLIENT_SECRET=os.environ.get("MASTO_KEY")
TWITTER_ACCESS_TOKEN=os.environ.get("MASTO_KEY")
TWITTER_ACCESS_SECRET=os.environ.get("MASTO_KEY")


def stored(func):
    def inner(*args, **kwargs):
        filename = f"{func.__name__}.json"
        rich.print(f"stored.inner for {func.__name__}")

        if os.path.exists(filename):
            with open(filename, "r") as f:
                rich.print(f"Loading data from {filename}")
                data = json.load(f)
            return data

        rich.print(f"Calling {func.__name__}")
        data = func(*args, **kwargs)

        with open(filename, "w") as f:
            rich.print(f"Writing data to {filename}")
            json.dump(data, f, indent=4, default=str)

        return data

    return inner


@dataclass
class App:
    """Provides convenience methods for querying an instance and posting toots."""

    mastodon: Mastodon

    @stored
    def instance(self):
        """Return a dictionary of information about the connected instance."""

        return self.mastodon.instance()

    def instance_summary(self):
        instance = self.instance()
        fields = ["uri", "title", "short_description"]
        data = {field: instance[field] for field in fields}
        data["contact_account"] = instance["contact_account"]["display_name"]

        return data

    def status_post(self, status: str, visibility: str = "direct"):
        """Post a toot to our connection, private unless we say otherwise."""

        return self.mastodon.status_post(status, visibility=visibility)

    @classmethod
    def connect(
        cls,
        client_key=MASTO_KEY,
        api_base_url=MASTO_URL,
        client_secret=MASTO_SECRET,
        access_token=MASTO_TOKEN,
    ) -> "App":
        """Return an App connected to a specific Mastodon instance."""

        mastodon = Mastodon(
            client_id=client_key,
            api_base_url=api_base_url,
            client_secret=client_secret,
            access_token=access_token,
        )
        return cls(mastodon=mastodon)


def list_hugo_content() -> pd.DataFrame:
    """Return a listing of hugo content entries"""
    result = subprocess.run(
        ["hugo", "list", "all"], capture_output=True, text=True, check=True
    )
    csv_out = StringIO(result.stdout)
    entries = cast(
        pd.DataFrame,
        pd.read_csv(
            csv_out,
            usecols=["path", "title", "date", "draft", "permalink"],
            parse_dates=["date"],
        ),
    )
    rich.print(entries)
    path_parts = entries["path"].str.split("/", expand=True)
    entries["section"] = path_parts[1]

    return entries


def get_newest_entry() -> dict[str, Any]:
    """Return the most recently published entry."""
    entries = list_hugo_content()
    blog = entries[entries["section"] == "post"]
    newest = blog[blog["date"] == blog["date"].max()]
    newest_post = newest.to_dict('records')[0]

    return newest_post


def announce():
    """Announce the most recently posted content if needed."""
    newest_entry = get_newest_entry()
    rich.print(newest_entry)
    post_url = newest_entry["permalink"]
    source_path = Path(newest_entry["path"])

    content_dir = source_path.parent
    social_file = content_dir / "meta.yaml"

    if social_file.is_file():
        rich.print("[b]TODO:[/b] Parse social data files")
        return

    if not source_path.is_file():
        raise ValueError(f"Did not find expected source {source_path}!")

    announcement_text = compose_announcement(source_path, post_url)

    rich.print(announcement_text)

    confirmation = Confirm.ask("Check site and post announcement?")

    if confirmation:
        r = requests.head(post_url)

        if r.status_code == 200:
            rich.print("Ready to go!")
            app = App.connect()
            toot = app.status_post(announcement_text, visibility="public")
            toot_url = toot["url"]
            rich.print(f"{toot_url=}")
        else:
            rich.print(f"Got status code {r.status_code} for {post_url}")


def compose_announcement(source_path: Path, post_url: str) -> str:
    """Extract a social share announcement from article details."""
    meta = frontmatter.loads(source_path.read_text()).metadata
    rich.print(meta)

    if "category" not in meta:
        raise ValueError(f"No category in #{source_path}")

    if "title" not in meta:
        raise ValueError(f"No title in #{source_path}")

    title = meta["title"]
    category = meta["category"]
    opener = f"new {category} on random geekery:"

    if "description" in meta:
        opener = meta["description"]

    tag_list = " ".join([syndication_tag(tag) for tag in meta["tags"]])

    announcement_text = f"""{opener}

{title}

{tag_list} #Blog

{post_url}
"""
    return announcement_text


def syndication_tag(site_tag: str) -> str:
    """Return a tag formatted how I like for social sharing."""
    return "#" + "".join(
        [tag_term.title() for tag_term in slugify(site_tag).split("-")]
    )

if __name__ == "__main__":
    announce()
