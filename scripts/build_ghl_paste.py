"""Build GHL-ready paste files: #fk-lp only (CDN image URLs, same as index.html)."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PAGES = [
    ROOT / "sales" / "salon-at-home" / "index.html",
    ROOT / "sales" / "paonta-home-services" / "index.html",
    ROOT / "partner" / "join-as-a-partner" / "index.html",
]


def extract_fk_lp(html: str) -> str:
    start = html.find('<div id="fk-lp">')
    if start < 0:
        raise ValueError('Could not find <div id="fk-lp">')
    end_body = html.rfind("</body>")
    chunk = html[start:end_body].rstrip()
    if not chunk.endswith("</div>"):
        raise ValueError("fk-lp extract did not end with </div>")
    return chunk


def build(page: Path) -> Path:
    html = page.read_text(encoding="utf-8")
    body = extract_fk_lp(html)
    out = page.with_name("ghl-paste.html")
    header = (
        "<!-- FixKardo GHL paste: copy ALL of this file into one Custom HTML / Custom Code element. -->\n"
        "<!-- Fonts (Work Sans / Mukta / Material Symbols) self-load from the paste JS. -->\n"
        "<!-- Optional: also paste head-snippet.html into Tracking Code → Head (Pixel + early fonts). -->\n"
        "<!-- Images load from jsDelivr — repo must be public with assets/ on main. -->\n"
    )
    out.write_text(header + body + "\n", encoding="utf-8")
    size_kb = out.stat().st_size / 1024
    print(f"{out.relative_to(ROOT)}  ({size_kb:.0f} KB)")
    return out


def main() -> None:
    for page in PAGES:
        build(page)


if __name__ == "__main__":
    main()
