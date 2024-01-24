python := 'python3'
pytest := 'pytest'

default:
  @just --list

export:
  obsidian-export /mnt/c/Users/brian/vaults/v2024/ site/content

backlinks:
  perl bin/find-backlinks.pl

process:
  python bin/process_notes.py

pull: export backlinks process

serve:
  hugo serve -D

build:
  cd site && hugo --environment production

test: build
  {{ pytest }} -n auto tests

setup:
  {{ python }} -m pip install --upgrade -r requirements.txt

push:
  rsync --recursive --archive --update --verbose public/ a2:public_html

syndicate:
  {{ python }} scripts/syndicate.py

update:
  pip-compile --resolver=backtracking requirements.in > requirements.txt
  pip-sync requirements.txt
