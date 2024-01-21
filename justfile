
pull:
  obsidian-export /mnt/c/Users/brian/vaults/v2024/ content

backlinks:
  perl scripts/find-backlinks.pl

process:
  python scripts/process_notes.py

refresh: pull backlinks process

serve:
  hugo serve
