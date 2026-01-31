#!/usr/bin/env python3

import sys
from pathlib import Path
from fontTools.ttLib import TTFont

SCRIPT_DIR = Path(__file__).parent.resolve()
PROJECT_ROOT = SCRIPT_DIR.parent

DEFAULT_INPUT = PROJECT_ROOT / "ReadingGuide-Regular.otf"
DEFAULT_OUTPUT = PROJECT_ROOT / "web-fonts"


def build_webfonts(input_path: Path, output_dir: Path):
    output_dir.mkdir(parents=True, exist_ok=True)

    font = TTFont(input_path)

    stem = input_path.stem

    woff_path = output_dir / f"{stem}.woff"
    woff2_path = output_dir / f"{stem}.woff2"

    # WOFF
    font.flavor = "woff"
    font.save(woff_path)

    # WOFF2
    font.flavor = "woff2"
    font.save(woff2_path)

    print(f"Generated:")
    print(f"  {woff_path}")
    print(f"  {woff2_path}")


def main():
    if len(sys.argv) == 1:
        input_path = DEFAULT_INPUT
        output_dir = DEFAULT_OUTPUT
    elif len(sys.argv) == 3:
        input_path = Path(sys.argv[1])
        output_dir = Path(sys.argv[2])
    else:
        print("Usage: python build_webfont.py [input_font.otf output_dir]")
        print(f"Defaults: {DEFAULT_INPUT} -> {DEFAULT_OUTPUT}")
        sys.exit(1)

    if not input_path.exists():
        print(f"Input font not found: {input_path}")
        sys.exit(1)

    build_webfonts(input_path, output_dir)


if __name__ == "__main__":
    main()