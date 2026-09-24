"""Regenerate the self-hosted WenKai subset from a verified official TTF.

The Chinese homepage is the glyph source. Re-run this script when its copy changes.
Requires the small, build-time-only dependencies in font-requirements.txt.
"""

import argparse
import hashlib
from pathlib import Path
import shutil
from urllib.request import urlopen

from fontTools import subset
from fontTools.ttLib import TTFont


ROOT = Path(__file__).resolve().parents[1]
SOURCE_URL = "https://github.com/lxgw/LxgwWenKai/releases/download/v1.522/LXGWWenKai-Regular.ttf"
SOURCE_SHA256 = "39ad71264b588165b469e35e6afb162a378dacd1f95348160240ba9038ac3009"
CACHED_SOURCE = ROOT / ".cache/fonts/LXGWWenKai-Regular-v1.522.ttf"
PAGE = ROOT / "src/pages/zh/index.astro"
DESTINATION = ROOT / "public/fonts/LXGWWenKai-Regular-subset.woff2"
LICENSE = ROOT / "public/fonts/LXGWWenKai-OFL.txt"

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--source", type=Path, help="Use a local copy of the official v1.522 Regular TTF")
args = parser.parse_args()

source = args.source or CACHED_SOURCE
if not source.exists() and args.source is None:
    source.parent.mkdir(parents=True, exist_ok=True)
    temporary = source.with_suffix(".download")
    try:
        with urlopen(SOURCE_URL, timeout=120) as response, temporary.open("wb") as target:
            shutil.copyfileobj(response, target)
        source_hash = hashlib.sha256(temporary.read_bytes()).hexdigest()
        if source_hash != SOURCE_SHA256:
            raise ValueError(f"Downloaded source SHA-256 mismatch: {source_hash}")
        temporary.replace(source)
    finally:
        temporary.unlink(missing_ok=True)

actual_hash = hashlib.sha256(source.read_bytes()).hexdigest()
if actual_hash != SOURCE_SHA256:
    raise ValueError(f"Source SHA-256 mismatch for {source}: {actual_hash}")
if not LICENSE.is_file():
    raise FileNotFoundError(f"Required OFL notice is missing: {LICENSE}")

# Include the page's Han characters and punctuation, plus basic Latin for the
# mixed-language About line. The English game titles use Newsreader instead.
page_text = PAGE.read_text(encoding="utf-8")
glyphs = {
    char for char in page_text
    if ("\u3400" <= char <= "\u9fff")
    or (char.isascii() and char.isprintable())
    or char in "，。；、？！“”‘’（）《》·↗©"
}

font = TTFont(source, recalcTimestamp=False)  # Preserve source timestamp for reproducible output.
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

print(f"Wrote {DESTINATION.relative_to(ROOT)} ({DESTINATION.stat().st_size:,} bytes)")
print(f"Requested {len(glyphs)} distinct characters from {PAGE.relative_to(ROOT)}")
