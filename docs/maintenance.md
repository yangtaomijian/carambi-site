# Site maintenance

## Production architecture

This is a static Astro site. `src/pages/index.astro` renders the English homepage, `src/pages/zh/index.astro` renders the Chinese homepage, and `src/pages/404.astro` renders the custom 404 page. Shared head metadata lives in `src/components/SiteHead.astro`; styling lives in `src/styles/`. Static assets live in `public/`. Individual guide projects are linked from the homepages and maintained in separate repositories.

`astro.config.mjs` sets the domain-root origin to `https://carambi.com` and uses trailing slashes. Keep production URLs rooted at `/` and `/zh/`.

## Local build

```sh
npm ci
npm run dev
npm run build
npm run preview
```

The build writes the static site to gitignored `dist/`. It uses the committed WenKai subset and does not download or regenerate the source font.

## WenKai subset regeneration

When Chinese production copy changes, regenerate `public/fonts/LXGWWenKai-Regular-subset.woff2` with Python 3:

```sh
python3 -m venv /tmp/carambi-fonts
/tmp/carambi-fonts/bin/pip install -r scripts/font-requirements.txt
/tmp/carambi-fonts/bin/python scripts/subset-wenkai.py
```

The script pins the official LXGW WenKai Regular v1.522 source and verifies its SHA-256 before subsetting. It downloads the TTF only for explicit regeneration, caching it in gitignored `.cache/fonts/`. A matching local source can instead be passed with `--source /path/to/LXGWWenKai-Regular.ttf`. Keep `public/fonts/LXGWWenKai-OFL.txt` with the subset.

The script currently reads glyphs from `src/pages/zh/index.astro`. If Chinese copy moves into data files or components, update its glyph-source inputs before regenerating.

## Social-card regeneration

The source pages are `scripts/social/en.html` and `scripts/social/zh.html`, styled by `scripts/social/card.css`. After `npm ci`, serve the repository root:

```sh
python3 -m http.server 4333
```

Open `/scripts/social/en.html` and `/scripts/social/zh.html` on that local server in a browser at a 1200 × 630 viewport. Wait for `document.fonts.ready`, then save viewport screenshots as `public/social/carambi-en.png` and `public/social/carambi-zh.png`. The source CSS loads Newsreader from `node_modules/` and Chinese WenKai from the committed subset.

## Crawler policy

`public/robots.txt` allows general search crawling, OAI-SearchBot, Claude-SearchBot, and Claude-User; it disallows GPTBot, ClaudeBot, and CCBot. It references `public/sitemap.xml`, which lists only `/` and `/zh/`. No Google-Extended rule is set.

## GitHub Pages deployment

`.github/workflows/deploy.yml` builds and deploys on pushes to `main` and supports manual `workflow_dispatch`. The Pages source is GitHub Actions. The workflow uploads Astro's static output and deploys it to the `github-pages` environment.

The repository's GitHub Pages setting holds the `carambi.com` custom domain. The Actions deployment does not need a `CNAME` file. Keep `astro.config.mjs` pointed at `https://carambi.com` without a repository-name `base` path.
