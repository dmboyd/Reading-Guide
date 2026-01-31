#!/usr/bin/env python3

import shutil
from pathlib import Path
from build_webfont import build_webfonts, DEFAULT_INPUT, DEFAULT_OUTPUT

DOCS = Path(__file__).parent.parent / "docs"

build_webfonts(DEFAULT_INPUT, DEFAULT_OUTPUT)

DOCS.mkdir(exist_ok=True)
shutil.copy2(DEFAULT_OUTPUT / "ReadingGuide-Regular.woff", DOCS)
shutil.copy2(DEFAULT_OUTPUT / "ReadingGuide-Regular.woff2", DOCS)

print("Copied to docs/")
