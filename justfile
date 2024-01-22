python := 'python3'
pytest := 'pytest'

default:
  @just --list

pull:
  obsidian-export /mnt/c/Users/brian/vaults/v2024/ content

backlinks:
  perl scripts/find-backlinks.pl

process:
  python scripts/process_notes.py

refresh: pull backlinks process

serve:
  hugo serve -D

build:
  hugo --environment production

test: build
  {{ pytest }} -n auto tests

setup:
  {{ python }} -m pip install --upgrade -r requirements.txt

update:
  pip-compile --resolver=backtracking requirements.in > requirements.txt
  pip-sync requirements.txt
