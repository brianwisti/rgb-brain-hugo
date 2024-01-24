"""Constant values for site-processing logic."""

import re

# Where Hugo expects to find notes and attachments
CONTENT_DIR = "site/content"

# Obsidian Markdown: wiki links
NOTE_LINK = r"""
  \[
    (?<title> [^\]]+? )
  \]
  \(
    (?<path> [^\)]+? \.md)
  \)
"""

# Obsidian Markdown: callouts
CALLOUT = re.compile(
    r"""> \s
        \\\[\! (?P<callout_type>[A-Z]+) \\\]
        (?: \s (?P<title> [^ \n ]+?))?
        \n
    """,
    re.VERBOSE,
)
