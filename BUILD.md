# Building Reading Guide Webfonts

## Requirements

- Python 3.x
- fontTools (`pip install fonttools brotli`)

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Build

```bash
python source/build.py
```

This generates:
- `web-fonts/ReadingGuide-Regular.woff`
- `web-fonts/ReadingGuide-Regular.woff2`
- Copies both to `docs/` for GitHub Pages
