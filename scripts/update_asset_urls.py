"""Add cache-bust query params and fix logo dimensions in landing HTML."""
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
files = [
    root / "sales" / "salon-at-home" / "index.html",
    root / "sales" / "paonta-home-services" / "index.html",
    root / "partner" / "join-as-a-partner" / "index.html",
]
CDN = "https://cdn.jsdelivr.net/gh/Ranjan-Kashyap/fixkardo-landing-pages@main/assets/"
V = "20261117b"

pattern = re.compile(
    r"https://cdn\.jsdelivr\.net/gh/Ranjan-Kashyap/fixkardo-landing-pages@main/assets/"
    r"([A-Za-z0-9._-]+\.(?:webp|png|jpg|jpeg))(?:\?[^\"']*)?"
)

for f in files:
    text = f.read_text(encoding="utf-8")
    new = pattern.sub(lambda m: f"{CDN}{m.group(1)}?v={V}", text)
    new = re.sub(
        r'(<img class="logo" src="[^"]+" )width="\d+" height="\d+"( alt="FixKardo">)',
        r'\1width="152" height="51"\2',
        new,
    )
    new = re.sub(
        r'(<img class="logo" src="[^"]+" )width="\d+" height="\d+"( alt="FixKardo" loading="lazy">)',
        r'\1width="134" height="45"\2',
        new,
    )
    f.write_text(new, encoding="utf-8")
    print(f.name, "updated", new.count(f"?v={V}"), "urls")
