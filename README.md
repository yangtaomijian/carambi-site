# Carambi static site

Astro builds the English `/` and Chinese `/zh/` editions for the domain root at `https://carambi.com`. Run `npm install`, then `npm run dev` for local review or `npm run build` for the static `dist/` output. The normal build is offline and does not fetch fonts or other assets.

The production Latin fonts are Newsreader and Source Sans 3, bundled from Fontsource 5.3.0 as one Latin WOFF2 each. The Chinese edition uses a local LXGW WenKai Regular WOFF2 subset; its SIL Open Font License 1.1 notice is at `public/fonts/LXGWWenKai-OFL.txt`. The original font is from the [official LXGW WenKai v1.522 release](https://github.com/lxgw/LxgwWenKai/releases/tag/v1.522). The source license declares no Reserved Font Name. The subset retains the source's internal naming and copyright/license metadata; `Carambi WenKai Subset` is only its CSS alias.

## Regenerate the Chinese subset

Regeneration is an explicit maintenance step, not part of `npm run build`. Use Python 3 in a disposable environment:

```sh
python3 -m venv /tmp/carambi-fonts
/tmp/carambi-fonts/bin/pip install -r scripts/font-requirements.txt
/tmp/carambi-fonts/bin/python scripts/subset-wenkai.py
```

The script downloads `LXGWWenKai-Regular.ttf` from the pinned official v1.522 release into gitignored `.cache/fonts/` only if absent, checks SHA-256 `39ad71264b588165b469e35e6afb162a378dacd1f95348160240ba9038ac3009`, then generates `public/fonts/LXGWWenKai-Regular-subset.woff2`. It also verifies any cached file before use. To use a separately supplied copy of that exact source, pass `--source /path/to/LXGWWenKai-Regular.ttf`; the same checksum is required.

The glyph source currently assumes Chinese production copy is present in `src/pages/zh/index.astro`. If copy moves into shared data or components, update the subset script's source inputs before regenerating the font.

## Social cards

The reproducible card sources are `scripts/social/en.html`, `scripts/social/zh.html`, and `scripts/social/card.css`. The final 1200 × 630 PNGs are in `public/social/`. To render them locally, serve the repository root with `python3 -m http.server 4333`, open each source page in a 1200 × 630 browser viewport, wait for `document.fonts.ready`, and save a viewport screenshot. For example, using Playwright CLI and the installed Edge browser:

```sh
npx --yes --package @playwright/cli playwright-cli -s=carambi-social open http://127.0.0.1:4333/scripts/social/en.html --browser msedge
npx --yes --package @playwright/cli playwright-cli -s=carambi-social run-code 'async (page) => { await page.setViewportSize({width:1200,height:630}); await page.evaluate(() => document.fonts.ready); await page.screenshot({path:"public/social/carambi-en.png"}); }'
npx --yes --package @playwright/cli playwright-cli -s=carambi-social goto http://127.0.0.1:4333/scripts/social/zh.html
npx --yes --package @playwright/cli playwright-cli -s=carambi-social run-code 'async (page) => { await page.evaluate(() => document.fonts.ready); await page.screenshot({path:"public/social/carambi-zh.png"}); }'
```

## Crawler policy

`robots.txt` allows normal search, OAI-SearchBot, Claude-SearchBot, and Claude-User; it blocks GPTBot, ClaudeBot, and CCBot. Google-Extended is intentionally unset. Its rule remains a publication-policy decision because it affects both future Gemini training and certain grounding uses.
