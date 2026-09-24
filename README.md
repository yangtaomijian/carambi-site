# Carambi local prototype

The English homepage is at `/`, and the Chinese edition is at `/zh/`. The temporary typography comparison remains at `/specimen/type/` in development. The build omits that route and its full source TTF files from `dist/`.

Run `npm install`, then `npm run dev` for browser review or `npm run build` for a static build.

## Specimen font sources

- Newsreader, Source Serif 4, Literata, and Source Sans 3: Fontsource variable packages, version 5.3.0. Their `standard.css` (editorial) or `wght.css` (interface) declarations and WOFF2 files are bundled locally by Astro. Source Sans 3 has no optical-size axis in this package.
- Spectral: Fontsource static package, version 5.3.0, regular weight (`400.css`), bundled locally by Astro as WOFF2/WOFF assets.
- LXGW WenKai Regular: unmodified `LXGWWenKai-Regular.ttf` from the [official v1.522 release](https://github.com/lxgw/LxgwWenKai/releases/tag/v1.522), copied into `public/_specimen/fonts/`.
- LXGW WenKai Screen: unmodified `LXGWWenKaiScreen.ttf` from the [official v1.522 release](https://github.com/lxgw/LxgwWenKai-Screen/releases/tag/v1.522), copied into `public/_specimen/fonts/`.

These fonts are under SIL Open Font License 1.1; see the package `LICENSE` files and the adjacent LXGW `OFL.txt` copies for copyright notices and conditions. Keep the relevant license notices with any redistributed font assets. The two full LXGW TTF files total about 51 MB. This is a temporary local comparison method, not a production font delivery choice. The Screen release maps a heavier source design to regular weight, which is an inherent visual difference under the shared CSS `400` target.

## Chinese homepage font subset

`/zh/` uses a self-hosted WOFF2 subset of the official LXGW WenKai Regular v1.522 specimen source. The English homepage does not use this font. The full TTF remains only in `public/_specimen/` for the temporary development specimen and subset regeneration; `scripts/omit-specimen.mjs` excludes it from production build output.

To regenerate after editing Chinese copy, use Python 3 in a disposable environment:

```sh
python3 -m venv /tmp/carambi-fonts
/tmp/carambi-fonts/bin/pip install -r scripts/font-requirements.txt
/tmp/carambi-fonts/bin/python scripts/subset-wenkai.py
```

The script reads `src/pages/zh/index.astro`, subsets the source TTF, and writes `public/fonts/LXGWWenKai-Regular-subset.woff2` with a copy of the complete SIL OFL 1.1 license beside it. The source license contains no declared Reserved Font Name after its copyright statements. The subset keeps the font's internal naming and copyright/license metadata; `Carambi WenKai Subset` is only the CSS `@font-face` alias. The modified font remains under OFL 1.1, and the font authors are credited solely through the license notice.

The glyph source currently assumes Chinese production copy is present in `src/pages/zh/index.astro`. If copy moves into shared data or components, update the subset script's source inputs before regenerating the font.
