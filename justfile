python := 'python3'
pytest := 'pytest -n auto'

default:
  @just --list

# Build and test the site
site: build test-site

pull: export backlinks process

# Grab my Obsidian notes for Hugo
export:
  obsidian-export $VAULT_HOME site/content

backlinks:
  perl bin/find-backlinks.pl

process:
  python bin/process_notes.py

serve:
  hugo serve -D

build:
  cd site && hugo --environment production

# Install initial python dependencies
setup:
  {{ python }} -m pip install --upgrade -r requirements.txt

syndicate:
  {{ python }} scripts/syndicate.py

# Test consistency and format of exported notes
test-content:
  {{ pytest }} note_processor/tests/content

# Test note processing logic
test-main:
  {{ pytest }} note_processor/tests/note_processor

# Test Hugo output
test-site:
  {{ pytest }} note_processor/tests/site

# Refresh Python dependencies from requirements.in
update:
  pip-compile --resolver=backtracking requirements.in > requirements.txt
  pip-sync requirements.txt
