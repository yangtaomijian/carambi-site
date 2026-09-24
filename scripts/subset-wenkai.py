"""Regenerate the self-hosted WenKai subset from the official specimen TTF.

The Chinese homepage is the glyph source. Re-run this script when its copy changes.
Requires the small, build-time-only dependencies in font-requirements.txt.
"""

from pathlib import Path
import shutil

from fontTools import subset
from fontTools.ttLib import TTFont


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "public/_specimen/fonts/LXGWWenKai-Regular.ttf"
LICENSE = ROOT / "public/_specimen/fonts/LXGWWenKai-OFL.txt"
PAGE = ROOT / "src/pages/zh/index.astro"
DESTINATION = ROOT / "public/fonts/LXGWWenKai-Regular-subset.woff2"

# Include the page's Han characters and punctuation, plus basic Latin for the
# mixed-language About line. The English game titles use Newsreader instead.
page_text = PAGE.read_text(encoding="utf-8")
glyphs = {
    char for char in page_text
    if ("\u3400" <= char <= "\u9fff")
    or (char.isascii() and char.isprintable())
    or char in "，。；、？！“”‘’（）《》·↗©"
}

font = TTFont(SOURCE, recalcTimestamp=False)  # Preserve source timestamp for reproducible output.
options = subset.Options()
options.name_IDs = ["*"]  # Retain copyright and license metadata.
options.name_languages = ["*"]
options.name_legacy = True
options.layout_features = ["*"]
subsetter = subset.Subsetter(options=options)
subsetter.populate(text="".join(sorted(glyphs)))
subsetter.subset(font)
font.flavor = "woff2"

DESTINATION.parent.mkdir(parents=True, exist_ok=True)
font.save(DESTINATION)
shutil.copyfile(LICENSE, DESTINATION.parent / "LXGWWenKai-OFL.txt")

print(f"Wrote {DESTINATION.relative_to(ROOT)} ({DESTINATION.stat().st_size:,} bytes)")
print(f"Requested {len(glyphs)} distinct characters from {PAGE.relative_to(ROOT)}")
