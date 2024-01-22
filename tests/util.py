"""
Utility logic for testing.

Wouldn't be surprised if it ended up in site-wide support code later.
"""

import io
import subprocess
from typing import cast

import pandas as pd
from yarl import URL

def load_hugo_pages() -> pd.DataFrame:
    """Return data that Hugo reports about site contents."""
    cmd = ("hugo", "list", "all")
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE)

    if not process.stdout:
        raise ValueError(f"No output from {cmd}")

    csv = io.StringIO(process.stdout.read().decode())
    data = cast(pd.DataFrame, pd.read_csv(csv, index_col=0))
    csv.close()
    data["out"] = data["permalink"].apply(lambda s: URL(s).path[1:] + "index.html")

    return data
