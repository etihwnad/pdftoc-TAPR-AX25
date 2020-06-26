#!/usr/bin/env python3

# Copyright 2020 Dan White
# MIT License
# https://opensource.org/licenses/MIT

"""
Tool to take a text file describing the page number and bookmark title and
convert to a file suitable for adding bookmarks to a PDF file using pdftk.

Bookmark levels are indicated by levels of tab indentation (\t characters)

File format
(1) Title
(3) Section
\t(4) Subsection
"""

import argparse
import re
import sys

parser = argparse.ArgumentParser(
    description='Convert an outline file of PDF bookmark pages and titles to a format suitable for pdftk.'
)
parser.add_argument('infile', nargs='?', default='toc.votl')

args = parser.parse_args()


fmt = """BookmarkBegin
BookmarkTitle: {title}
BookmarkLevel: {level}
BookmarkPageNumber: {page}"""

page_re = re.compile(r'\((\d+)\)')

with open(args.infile) as f:
    for line in f:
        line = line.rstrip()
        x = line.split('\t')
        level = 1 + sum([1 for k in x if k == ''])

        m = page_re.search(line)
        if m is not None:
            page = int(m.group(1))
            title = line[m.end():].lstrip()
        else:
            continue

        print(fmt.format(title=title, level=level, page=page))

