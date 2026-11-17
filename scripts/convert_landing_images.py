"""Convert Google Flow JPGs into sized WebP assets for the landing pages."""
from pathlib import Path

from PIL import Image

root = Path(__file__).resolve().parents[1]
src_root = root / "assets" / "Landing Page Images"
out_dir = root / "assets"

# (folder, filename prefix, output name, width, height)
MAPPINGS = [
    ("Salon", "A1", "salon-hero.webp", 800, 1000),
    ("Salon", "A2", "salon-door.webp", 800, 600),
    ("Salon", "A3", "salon-facial.webp", 600, 450),
    ("Salon", "A4", "salon-hairspa.webp", 600, 450),
    ("Salon", "A5", "salon-manicure.webp", 600, 450),
    ("Salon", "A6", "salon-blowdry.webp", 600, 450),
    ("home services", "B1", "paonta-hero.webp", 800, 1000),
    ("home services", "B2", "svc-electrician.webp", 600, 450),
    ("home services", "B3", "svc-plumber.webp", 600, 450),
    ("home services", "B4", "svc-ro.webp", 600, 450),
    ("home services", "B5", "svc-tank.webp", 600, 450),
    ("home services", "B6", "svc-mens-salon.webp", 600, 450),
    ("join as a partner", "C1", "partner-hero.webp", 800, 1000),
]


def find_source(folder: str, prefix: str) -> Path:
    d = src_root / folder
    matches = [p for p in d.iterdir() if p.is_file() and p.name.startswith(prefix)]
    if not matches:
        raise FileNotFoundError(f"No file starting with {prefix} in {d}")
    return matches[0]


def fit_cover(im: Image.Image, tw: int, th: int) -> Image.Image:
    """Center-crop to target aspect, then resize (object-fit: cover)."""
    sw, sh = im.size
    target_aspect = tw / th
    src_aspect = sw / sh
    if src_aspect > target_aspect:
        new_w = int(round(sh * target_aspect))
        left = (sw - new_w) // 2
        im = im.crop((left, 0, left + new_w, sh))
    elif src_aspect < target_aspect:
        new_h = int(round(sw / target_aspect))
        top = max(0, int((sh - new_h) * 0.35))
        if top + new_h > sh:
            top = sh - new_h
        im = im.crop((0, top, sw, top + new_h))
    return im.resize((tw, th), Image.Resampling.LANCZOS)


def main() -> None:
    results = []
    for folder, prefix, out_name, tw, th in MAPPINGS:
        src = find_source(folder, prefix)
        im = Image.open(src).convert("RGB")
        out = fit_cover(im, tw, th)
        out_path = out_dir / out_name
        out.save(out_path, "WEBP", quality=82, method=6)
        results.append((out_name, src.name, out.size, out_path.stat().st_size))

    for name, src_name, size, nbytes in results:
        print(f"{name:22} <- {src_name[:55]:55} {size[0]}x{size[1]} {nbytes // 1024}KB")
    print(f"Done: {len(results)} files")


if __name__ == "__main__":
    main()
