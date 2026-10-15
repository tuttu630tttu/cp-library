#!/usr/bin/env python3
"""Generate VS Code snippets from the C++ sources (Python standard library only)."""

import argparse
from datetime import datetime
import json
import os
from pathlib import Path
import shutil
import tempfile
from textwrap import dedent


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "vscode" / "cpp.code-snippets"
TARGET = Path.home() / "Library/Application Support/Code/User/snippets/cpp.json"
PREFIXES = {"grid4": "dxdy4", "grid8": "dxdy8"}
LEGACY = {
    "Kyopro Template 2026": "kyopro",
    "Out of func": "outof",
    "4 dx dy": "dxdy4",
    "8 dx dy": "dxdy8",
}
DESCRIPTIONS = {
    "grid4": "4方向のdy/dx。grid8と併用しない",
    "grid8": "8方向のdy/dx。grid4と併用しない",
    "outof": "solve内の範囲外判定。h, wとllが必要。引数は行、列",
    "digits": "非負整数を桁の配列に変換。儀式テンプレートが必要",
    "rnum": "非負整数の桁を反転。結果がlong longに収まること。llが必要",
}


def snippet_body(source):
    # Escape snippet syntax in addition to JSON encoding below: C++ literals
    # such as '\\n' and '$value' must survive VS Code snippet expansion.
    text = dedent(source).rstrip("\n")
    return text.replace("\\", "\\\\").replace("$", "\\$").split("\n")


def build_snippets():
    template = snippet_body((ROOT / "template.cpp").read_text(encoding="utf-8"))
    # Only the generated snippet gets a cursor stop; the C++ original stays valid.
    solve_line = template.index("int solve(){")
    if template[solve_line + 1].strip():
        raise ValueError("Expected a blank line immediately after int solve(){")
    template[solve_line + 1] = "    $0"
    snippets = {
        "cp-library: template": {
            "scope": "cpp",
            "prefix": "kyopro",
            "body": template,
            "description": "競プロ用の儀式テンプレート",
        }
    }
    for path in sorted((ROOT / "snippets").glob("*.inc")):
        snippets[f"cp-library: {path.stem}"] = {
            "scope": "cpp",
            "prefix": PREFIXES.get(path.stem, path.stem),
            "body": snippet_body(path.read_text(encoding="utf-8")),
            "description": DESCRIPTIONS.get(path.stem, f"cp-library: {path.stem}"),
        }
    return snippets


def encode(value):
    return json.dumps(value, ensure_ascii=False, indent=2) + "\n"


def install(snippets, target):
    # Parse before writing anything. Invalid JSON/JSONC is never overwritten.
    before = target.read_text(encoding="utf-8") if target.exists() else None
    existing = json.loads(before) if before is not None else {}
    if not isinstance(existing, dict):
        raise ValueError(f"Expected a JSON object: {target}")
    for name, prefix in LEGACY.items():
        entry = existing.get(name)
        if isinstance(entry, dict) and entry.get("prefix") == prefix:
            del existing[name]
    # Language-specific cpp.json rejects scope; only .code-snippets uses it.
    installed = {
        name: {key: value for key, value in entry.items() if key != "scope"}
        for name, entry in snippets.items()
    }
    existing.update(installed)
    after = encode(existing)
    if before == after:
        print(f"Already up to date: {target}")
        return
    target.parent.mkdir(parents=True, exist_ok=True)
    if before is not None:
        backup = target.with_name(target.name + datetime.now().strftime(".%Y%m%d-%H%M%S-%f.bak"))
        shutil.copy2(target, backup)
        print(f"Backup: {backup}")
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=target.parent, delete=False) as stream:
            temporary = Path(stream.name)
            stream.write(after)
        if target.exists():
            shutil.copymode(target, temporary)
        os.replace(temporary, target)
    finally:
        if temporary is not None and temporary.exists():
            temporary.unlink()
    print(f"Installed {len(snippets)} snippets: {target}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--generate-only", action="store_true", help="Generate repository JSON without installing")
    parser.add_argument("--target", type=Path, default=TARGET, help="Destination cpp.json")
    args = parser.parse_args()
    snippets = build_snippets()
    if not args.generate_only:
        install(snippets, args.target.expanduser())
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(encode(snippets), encoding="utf-8")
    print(f"Generated {len(snippets)} snippets: {OUTPUT}")


if __name__ == "__main__":
    main()
