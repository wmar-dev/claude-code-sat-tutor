#!/usr/bin/env python3
"""Convert the SAT Prep Meeting Word doc to markdown via pandoc.

Usage:
    extract_meeting_notes.py [--input INPUT.docx] [--output OUTPUT.md]

Defaults to assets/SAT Prep Meeting.docx -> assets/SAT Prep Meeting.md
(relative to the project root, four levels up from this script).

Requires pandoc (`brew install pandoc` on macOS).
"""

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[4]
DEFAULT_INPUT = PROJECT_ROOT / "assets" / "SAT Prep Meeting.docx"


def convert(input_path: Path, output_path: Path) -> None:
    if shutil.which("pandoc") is None:
        sys.exit("pandoc is required (install with `brew install pandoc`)")

    result = subprocess.run(
        ["pandoc", str(input_path), "-t", "markdown-smart", "--wrap=none"],
        capture_output=True, text=True, check=True,
    )
    text = result.stdout

    # Simplify underlined hyperlinks: [[text]{.underline}](url) -> [text](url)
    text = re.sub(r"\[\[(.*?)\]\{\.underline\}\]\((.*?)\)", r"[\1](\2)", text)
    # Drop underline markers on plain text: [text]{.underline} -> text
    text = re.sub(r"\[([^\]]*)\]\{\.underline\}", r"\1", text)
    # Unescape pipes (pandoc escapes | so it isn't read as a table delimiter)
    text = text.replace(r"\|", "|")

    output_path.write_text(text, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT, help="Path to .docx file")
    parser.add_argument("--output", type=Path, default=None, help="Path to write markdown (default: input with .md extension)")
    args = parser.parse_args()

    input_path = args.input
    output_path = args.output or input_path.with_suffix(".md")

    if not input_path.exists():
        sys.exit(f"Input not found: {input_path}")

    convert(input_path, output_path)
    print(f"Wrote {output_path}")


if __name__ == "__main__":
    main()
