"""Regenerate the homepage character art from the project source image.

This is an optional design tool; the website build only needs Node.js.
Requires Pillow: pip install pillow
"""

from pathlib import Path
from PIL import Image, ImageOps, ImageFilter

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "assets" / "asuka-source.png"
OUTPUT = ROOT / "src" / "art" / "asuka.txt"
COLS = 76
ROWS = 68

image = Image.open(SOURCE).convert("L")
image = ImageOps.autocontrast(image)
image = image.resize((COLS * 2, ROWS * 4), Image.Resampling.LANCZOS)
image = image.filter(ImageFilter.UnsharpMask(radius=1.2, percent=120, threshold=3))

dots = ((0, 0, 0), (0, 1, 1), (0, 2, 2), (1, 0, 3),
        (1, 1, 4), (1, 2, 5), (0, 3, 6), (1, 3, 7))
lines = []
for row in range(ROWS):
    chars = []
    for col in range(COLS):
        bits = 0
        for dx, dy, bit in dots:
            if image.getpixel((col * 2 + dx, row * 4 + dy)) < 110:
                bits |= 1 << bit
        chars.append(chr(0x2800 + bits) if bits else " ")
    lines.append("".join(chars).rstrip())

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
OUTPUT.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
print(f"Wrote {OUTPUT}")
