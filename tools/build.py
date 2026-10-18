#!/usr/bin/env python3
"""Build a portable prompt and self-contained skill ZIP using Python's standard library."""
import argparse
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "acid-method"


def portable_prompt():
    text = (SKILL / "SKILL.md").read_text()
    body = text.split("---", 2)[2].strip()
    body = body.replace(
        "Read [references/framework.md](references/framework.md) when explaining the framework, its provenance, or its symbolic origins.",
        "Use the framework reference included below when explaining provenance or symbolic origins.",
    )
    body = body.replace(
        "[ACID Method - Framework.svg](assets/ACID%20Method%20-%20Framework.svg)",
        "[ACID Method - Framework.svg](https://raw.githubusercontent.com/designonacid/skills/main/skills/acid-method/assets/ACID%20Method%20-%20Framework.svg)",
    )
    body = body.replace(
        "## Required visual: framework heat map\n",
        "## Required visual: framework heat map\n\n"
        "For this portable prompt, retrieve the original SVG through the link below or use a user-supplied copy. "
        "If the original is inaccessible, ask for it; if rendering is unsupported, disclose that limitation. "
        "Do not recreate the framework, invent a heat map, or claim to have displayed one.\n",
    )
    return (
        "# ACID Method — portable instructions\n\n"
        "Use these instructions for content analysis in this conversation unless I explicitly request another method. "
        "This prompt supplies the methodology directly; it does not install a skill or imply access to external files.\n\n"
        + body + "\n\n---\n\n"
        + (SKILL / "references" / "framework.md").read_text().strip() + "\n"
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Check portable prompt parity without writing files")
    args = parser.parse_args()
    destination = ROOT / "prompts" / "acid-method.md"
    expected = portable_prompt()
    if args.check:
        if not destination.exists() or destination.read_text() != expected:
            raise SystemExit("Portable prompt is stale: run python3 tools/build.py")
        print("Portable prompt matches skill and framework reference.")
        return
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(expected)
    dist = ROOT / "dist"
    dist.mkdir(exist_ok=True)
    with ZipFile(dist / "acid-method.zip", "w", ZIP_DEFLATED) as archive:
        for path in sorted(SKILL.rglob("*")):
            if path.is_file():
                archive.write(path, Path("acid-method") / path.relative_to(SKILL))
        archive.write(ROOT / "LICENSE", "acid-method/LICENSE")
    print("Built prompts/acid-method.md and dist/acid-method.zip")


if __name__ == "__main__":
    main()
