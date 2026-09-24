# Carambi local prototype

The root route is the first English desktop homepage prototype. The temporary typography comparison remains at `/specimen/type/` for local review; remove the `specimen` route and its font files before a public release.

Run `npm install`, then `npm run dev` for browser review or `npm run build` for a static build.

## Specimen font sources

- Newsreader, Source Serif 4, Literata, and Source Sans 3: Fontsource variable packages, version 5.3.0. Their `standard.css` (editorial) or `wght.css` (interface) declarations and WOFF2 files are bundled locally by Astro. Source Sans 3 has no optical-size axis in this package.
- Spectral: Fontsource static package, version 5.3.0, regular weight (`400.css`), bundled locally by Astro as WOFF2/WOFF assets.
- LXGW WenKai Regular: unmodified `LXGWWenKai-Regular.ttf` from the [official v1.522 release](https://github.com/lxgw/LxgwWenKai/releases/tag/v1.522), copied into `public/_specimen/fonts/`.
- LXGW WenKai Screen: unmodified `LXGWWenKaiScreen.ttf` from the [official v1.522 release](https://github.com/lxgw/LxgwWenKai-Screen/releases/tag/v1.522), copied into `public/_specimen/fonts/`.

These fonts are under SIL Open Font License 1.1; see the package `LICENSE` files and the adjacent LXGW `OFL.txt` copies for copyright notices and conditions. Keep the relevant license notices with any redistributed font assets. The two full LXGW TTF files total about 51 MB. This is a temporary local comparison method, not a production font delivery choice. The Screen release maps a heavier source design to regular weight, which is an inherent visual difference under the shared CSS `400` target.
