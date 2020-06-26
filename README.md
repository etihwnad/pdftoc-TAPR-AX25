# PDF bookmarks for AX.25 Link Access Protocol for Amateur Packet Radio

version 2.2 (July 1998)

published by https://tapr.org

canonical location http://www.tapr.org/pdf/AX25.2.2.pdf

**Version with PDF Bookmarks:** [AX25.2.2_toc.pdf](https://github.com/etihwnad/pdftoc-TAPR-AX25/releases/download/2.2-toc1/AX25.2.2_toc.pdf)

Unfortunately, the canonical version does not include bookmarks which make navigating to
various sections convenient.
This repository contains a tool for converting a specially-formatted
[VimOutliner-style](https://github.com/vimoutliner/vimoutliner) file `toc.votl`
into an input file suitable for input to [PDFtk](https://www.pdflabs.com/tools/pdftk-the-pdf-toolkit/) for adding such a set of hierarchical bookmarks.

The bookmark input file `toc.votl` is formatted as:

    {tab-indented level}(pdfpagenumber) The bookmark text

The `totoc.py` script and Makefile handle the work of fetching the source PDF,
converting to the correct bookmark file, and merging the information.

## Requirements

* PDFtk available as `pdftk`
* Python 3 available as `python3`
