# Carambi

Carambi is an independent home for guides and reference projects for furry visual novels and related games.

- [English site](https://carambi.com/)
- [中文网站](https://carambi.com/zh/)

Individual guide projects are maintained in separate repositories. This repository contains the bilingual root site.

## Local development

```sh
npm ci
npm run dev
npm run build
```

The site is built with Astro and deployed through GitHub Pages. It uses Newsreader for English editorial text, Source Sans 3 for interface text, and LXGW WenKai Regular for Chinese editorial text. LXGW WenKai is licensed under the [SIL Open Font License 1.1](public/fonts/LXGWWenKai-OFL.txt).

See [maintenance notes](docs/maintenance.md) for font, social-card, crawler, and deployment upkeep.
