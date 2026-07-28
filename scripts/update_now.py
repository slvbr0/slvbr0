#!/usr/bin/env python3
"""Rewrite the // now block in README.md from NOW.md, stamping today's date.

ponytail: single regex substitution, stdlib only. No templating engine needed
for two markers and a date line.
"""
import datetime
import re
import sys

README = "README.md"
SOURCE = "NOW.md"
START = "<!-- NOW:START -->"
END = "<!-- NOW:END -->"


def main() -> int:
    with open(SOURCE, encoding="utf-8") as f:
        body = f.read().strip()

    today = datetime.date.today().isoformat()
    block = f"{START}\n{body}\n_Last updated: {today}_\n{END}"

    with open(README, encoding="utf-8") as f:
        readme = f.read()

    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.DOTALL)
    if not pattern.search(readme):
        print("NOW markers not found in README.md", file=sys.stderr)
        return 1

    new_readme = pattern.sub(block, readme, count=1)

    if new_readme == readme:
        print("No change.")
        return 0

    with open(README, "w", encoding="utf-8") as f:
        f.write(new_readme)
    print("README.md updated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
