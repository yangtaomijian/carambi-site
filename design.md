# Carambi Design Guide

Version: 0.2
Status: Typography selected; desktop browser calibration pending
Updated: 2026-09-25

## 1. Purpose and identity

Carambi is an independent creator identity and the long-term public home for maintained guides and reference projects.

The root site is an **identity hub and project index**. It is not another guide site, a portfolio, a wiki, a dashboard, or a publishing platform.

The current body of work is centered on independently maintained guides and reference projects for furry visual novels and related games. Many of these projects involve detailed documentation, source auditing, state and route reconstruction, runtime verification, and long-term maintenance.

That methodological rigor should influence the site's editorial character, but it should **not** be visualized literally through code, database interfaces, terminal motifs, technical diagrams, or dashboard UI.

English-facing identity:

**Carambi**

Chinese-speaking identity:

**杨桃蜜饯 / 杨桃**

The relationship between these identities may be stated naturally in the About copy. The etymology or naming process behind “Carambi” does not need to be explained publicly.

---

## 2. Core design direction

The desktop target balance is approximately:

**70% contemporary web interface + 30% editorial / archival publication**

Carambi should first read clearly as a modern website. Editorial and archival influences should enrich the typography, hierarchy, grid, numbering, spacing, and material character rather than turning the website into a simulated book or magazine page.

Useful conceptual references include the design logic of:

- an independent editorial publication
- a reference catalogue
- an academic monograph
- a small independent press
- an archival project index

The site should feel:

- quiet
- authored
- precise
- warm
- literate
- archival
- methodical
- independent
- long-lived

A modest degree of refinement or luxury is acceptable.

**Do not confuse restraint with plainness.**

Visual richness should come primarily from:

- typography
- spacing
- hierarchy
- grid relationships
- numbering
- fine rules
- carefully controlled asymmetry
- restrained marginal devices
- subtle materiality

It should not come from digital visual effects.

---

## 3. Information architecture

Version 1 is intentionally small.

### English

```text
/
├── Header
├── Hero
├── Selected Guides
├── About
└── Footer
```

### Chinese

```text
/zh/
├── Header
├── Hero
├── Selected Guides
├── About
└── Footer
```

The root site should remain a one-page creator index until the amount of real content justifies additional pages.

Do not create `/guides/`, `/projects/`, `/about/`, or other dedicated sections in v1 merely to make the site appear more complete.

Current header navigation should behave approximately as:

```text
Guides  → #guides
About   → #about
中文     → /zh/
GitHub  → external GitHub profile
```

The Chinese page should provide the corresponding English-language switch back to `/`.

The homepage may show a curated set of active or representative guides rather than becoming an exhaustive database. If the project catalogue eventually becomes too large for the homepage, a dedicated guide index may be introduced later.

---

## 4. Visual system

### 4.1 Color

The established palette is:

- warm ivory / soft paper-like background
- near-black charcoal primary text
- warm gray secondary text
- muted olive identity accent

The olive should feel mature, quiet, and desaturated. It should not resemble bright lime, neon green, or literal fruit branding.

For v1, use **one primary accent only**. Do not introduce a second accent merely for visual variety.

Exact color values are **TBD** and should be calibrated in the browser during prototype work.

Use the successful Phase 1 specimen palette as the Phase 2 starting point:

```text
ivory      #f5f2e9
charcoal   #272822
secondary  #79776e
olive      #626949
rule       #ccc9bd
```

These are prototype values, not a finalized production palette.

The target relationship is more important than any specific preliminary hex value.

---

### 4.2 Typography

Typography is one of the primary identity systems of the site.

Use two functional voices:

**Editorial / content voice**

Used for:

- hero title
- project titles
- About heading
- substantive editorial copy where appropriate

**Interface / reference voice**

Used for:

- navigation
- section labels
- project numbering
- versions and coverage metadata
- language metadata
- small structural labels
- footer metadata

The editorial voice should carry personality.

The interface voice should provide precision and structure.

#### English editorial / content voice

Use **Newsreader** for the Hero title, project titles, About heading, and editorial/content copy where the design specifies the editorial voice.

Use variable-font optical sizing where supported: `font-optical-sizing: auto`.

#### English interface / reference voice

Use **Source Sans 3** for navigation, section labels, numbering, version/coverage metadata, language metadata, small structural labels, and footer metadata.

It should remain neutral and subordinate to the editorial serif.

#### Chinese editorial / content voice

Use **LXGW WenKai Regular** for the Chinese Hero, Chinese project titles, Chinese About heading, and Chinese editorial/content copy. LXGW WenKai Screen is no longer a candidate.

#### Chinese interface / reference voice

Use a **PingFang SC / system sans-serif stack** for navigation, labels, numbering, and metadata. Fallbacks should remain robust.

#### Mixed-language text

Chinese text embedded in an English editorial context, such as `杨桃蜜饯`, should have appropriate language markup such as `lang="zh-CN"` and the intended Chinese font stack rather than uncontrolled browser fallback.

#### Production Chinese font delivery

The full local LXGW WenKai TTF used in the Phase 1 specimen is a testing source, not a production delivery decision. Do not assume that the full approximately 25 MB font file should be shipped on the production site. Chinese webfont delivery and subsetting remain TBD for the bilingual phase.

#### General principle

Do not try to make English and Chinese glyph shapes imitate each other.

The goal is functional and emotional equivalence:

```text
English editorial serif ≈ Chinese WenKai
English neutral sans    ≈ Chinese system sans
```

The two language versions should belong to the same design system without being typographically identical.

---

### 4.3 Grid and spacing

The site should use:

- generous outer whitespace
- clearly controlled content width
- strong alignment
- deliberate asymmetry
- clear vertical rhythm
- relatively restrained line lengths
- a more expressive Hero followed by a more structured Guide index

Avoid arbitrary floating placement.

Whitespace is structural and intentional.

Do not add decorative elements or copy merely to fill unused space.

Exact values for:

- maximum content width
- gutters
- column widths
- gaps
- section spacing
- font sizes
- line heights

are **TBD** and must be calibrated through browser screenshots rather than inferred mechanically from generated concept images.

---

### 4.4 Rules and editorial devices

Fine rules are part of the visual grammar.

Permitted devices include:

- thin horizontal rules
- one restrained vertical or marginal device
- guide numbering
- small uppercase structural labels
- subtle index- or folio-like alignment
- carefully controlled rule intersections

The site should not become covered in editorial ornament.

For desktop, the current preferred marginal motif is a single restrained:

**INDEX**

device associated primarily with the Hero or main page grid.

Its final position is **TBD**.

Do not repeat marginal labels throughout every section.

Do not create a persistent decorative rail containing repeated items such as:

```text
INDEX
GUIDES
ABOUT
01
02
...
```

The marginal device is an accent, not a second navigation system.

---

### 4.5 Materiality

The background may have extremely subtle material warmth.

Core rule:

**The user should perceive warmth, not perceive “a paper texture.”**

Acceptable:

- warm ivory background
- extremely subtle tonal variation
- very low-opacity CSS or SVG micro-noise if it materially improves the result
- a barely perceptible tonal field behind a lower section

Avoid:

- visible grain
- scanned paper
- stains
- paper damage
- distressed texture
- vintage aging
- vignette
- fake physical page edges

Materiality should remain subordinate to typography and layout.

---

## 5. Homepage composition

### 5.1 Header

Desktop structure:

```text
Carambi                                  Guides  About  中文  GitHub ↗
```

The header should be:

- lightweight
- horizontally composed
- visually quiet
- clearly part of the page grid

Do not use:

- pill-shaped navigation containers
- prominent CTA buttons
- glass or translucent sticky navigation
- large social-icon groups
- profile images
- decorative menu containers

A sticky header is not required.

---

### 5.2 Hero

The Hero carries a significant portion of the site's editorial character.

Current English copy:

```text
Guides and reference projects
for furry visual novels
and related games.

Independent documentation and long-term reference work.
```

The Hero should use the editorial typeface prominently.

It may use:

- deliberate asymmetric composition
- generous whitespace
- a restrained INDEX marginal device
- careful relationship between display and supporting copy
- fine rules

It should not use:

- illustrations
- project screenshots
- portraits
- CTA buttons
- invented slogans
- decorative brand statements

The current large-serif character is intentional and should not be flattened into a generic sans-serif portfolio hero.

---

### 5.3 Selected Guides

The Guide index is the core functional component of the homepage.

The preferred desktop grammar is approximately:

```text
01 │ Demons Within                         Public 14.6
   │ Bilingual player guide                中文 · English
────────────────────────────────────────────────────────

02 │ Password                              Build 0.85
   │ Guide and reference archive           中文 · English
────────────────────────────────────────────────────────
```

This is a structural reference, not a pixel specification.

Required characteristics:

- editorial index rows, not cards
- visible ordering number
- number may be larger and lighter than the title
- thin vertical separator may divide number and main content
- project title uses editorial typography
- metadata uses neutral sans-serif typography
- version / coverage metadata remains visually secondary
- language metadata remains visually secondary
- thin horizontal separators
- subtle external-link arrow
- strong alignment
- entire row may act as the primary clickable target
- design must scale naturally from 2 entries to approximately 5–10 entries

Do not add:

- rounded cards
- screenshots
- generated project thumbnails
- status pills
- “Maintained” badges unless there is a future semantic need
- last-updated timestamps
- page counts
- GitHub stars
- repository statistics
- search statistics
- fake project metadata

Homepage project metadata should remain concise.

Current intended fields are:

- title
- short description / type
- supported version or coverage
- languages

---

### 5.4 About

The About section is intentionally brief.

Current English copy:

```text
Carambi is the name I use for English-language projects.
Also known as 杨桃蜜饯 in Chinese-speaking communities.
```

A simple GitHub link may follow.

The About section may receive:

- slightly stronger spacing
- a subtle column relationship
- a very pale tonal background shift
- one fine rule

It must not become:

- a profile card
- a résumé
- a biography timeline
- a skills list
- a technology stack
- a portrait section
- an autobiographical essay

The root site is a creator identity hub, not a CV.

---

### 5.5 Footer

The footer may have a restrained publication-colophon character.

Current content:

```text
Carambi
Independent guides & reference projects
中文
GitHub ↗
© 2026
```

Use typography, spacing, alignment, and rules to create the colophon feeling.

Do not invent:

- “Published by”
- “Designed by”
- issue numbers
- edition numbers
- revision numbers
- archive IDs
- fake locations
- fake institutional metadata
- additional copyright language
- build information

---

## 6. Bilingual design

The English and Chinese sites use:

**the same information architecture and the same design grammar, but not pixel-identical typography.**

Shared between locales:

- component hierarchy
- section order
- palette
- grid logic
- guide-row structure
- rules
- responsive principles
- interaction behavior
- overall spacing rhythm

Locale-specific adjustment is explicitly permitted for:

- font family
- font size where necessary
- line height
- hero line breaks
- letter spacing
- content width
- metadata spacing
- small typographic alignment details

Do not mechanically reproduce English line breaks in Chinese.

Chinese typography should be composed according to natural Chinese reading rhythm.

The language versions should feel like two editions of the same publication, not one original site and one mechanically translated skin.

---

## 7. Responsive behavior

Responsive design must preserve hierarchy before ornament. The qualitative balance is approximately 70% contemporary web / 30% editorial and archival on desktop, and 85% contemporary web / 15% editorial and archival on mobile. These ratios are design direction, not measurable CSS targets.

### Desktop

Desktop may use:

- asymmetric Hero composition
- marginal INDEX device
- side-by-side project metadata
- more generous editorial spacing
- more visible publication-style grid relationships

### Mobile

The design should simplify.

A guide entry should collapse approximately toward:

```text
01

Demons Within ↗
Bilingual player guide

Public 14.6 · 中文 · English
────────────────────────────
```

On mobile:

- project metadata moves below the title/description
- marginal INDEX ornament disappears
- decorative vertical rails disappear
- horizontal space belongs to content
- Hero typography scales naturally
- typography remains expressive but readable
- whitespace remains generous but not wasteful
- content hierarchy takes precedence over preservation of desktop ornament

Do not introduce a hamburger menu unless navigation genuinely becomes too complex in the future.

For the current small navigation set, a simple compact mobile arrangement is preferred.

Core responsive rule:

**On mobile, preserve information hierarchy before preserving editorial ornament.**

Initial prototype targets should include at least:

- approximately 1440 px desktop
- approximately 390 px mobile

Exact breakpoints are **TBD** and should be based on content behavior rather than arbitrary device categories.

---

## 8. Interaction and motion

Interaction should remain quiet.

Permitted:

- underline changes
- subtle color transitions
- external-link arrow movement of approximately a few pixels
- restrained hover emphasis
- clear keyboard focus states

Avoid:

- scroll-reveal animation
- parallax
- animated backgrounds
- cursor effects
- text scrambling
- loading intros
- page-transition spectacle
- hover transforms that materially move layout
- decorative continuous animation

Respect:

```text
prefers-reduced-motion
```

The site should remain visually complete with motion disabled.

---

## 9. Imagery and identity marks

### Project imagery

Version 1 should use **no project imagery**.

Do not use:

- project screenshots
- guide screenshots
- generated thumbnails
- game artwork
- character artwork
- stock photography
- abstract landscape imagery
- decorative photographs

Project identity belongs primarily to the individual project sites.

Carambi provides the consistent directory layer.

### Logo

A formal Carambi logo is not required for v1.

The primary identity may simply be the word:

**Carambi**

Typography and the broader editorial system should carry most of the identity.

A favicon may be designed separately later.

If an abstract identity mark is ever explored, it should be:

- small
- geometric
- flat
- simple
- reproducible in CSS or SVG
- secondary to typography

It must not be:

- a literal carambola / starfruit
- a mascot
- a furry character
- a decorative seal
- a crest
- a dominant monogram
- a large homepage illustration

Do not force a mark into the layout merely because brands are expected to have logos.

---

## 10. Explicit anti-patterns

Do not reinterpret Carambi as any of the following:

- SaaS landing page
- startup homepage
- developer portfolio
- gaming portal
- fan wiki
- dashboard
- GitHub profile clone
- AI-generated “modern website”
- generic template portfolio

Avoid:

- bento grids
- excessive rounded cards
- card-inside-card layouts
- glassmorphism
- gradient hero backgrounds
- gradient text
- neon colors
- glow effects
- large shadows
- 3D decoration
- oversized CTA buttons
- pill badges
- tech-stack badges
- programming-language logos
- terminal windows
- code snippets as decoration
- GitHub contribution graphs
- live activity dashboards
- fake analytics
- fake metrics
- fake testimonials
- fake clients
- fake awards
- fake publication metadata
- fake archive classification
- fake dates
- fake issue or volume numbers
- invented slogans
- invented brand mottos
- stock imagery
- decorative project thumbnails
- literal fruit branding

Critical rule:

**Do not add content merely to fill visual empty space. Empty space is intentional.**

Do not invent copy that is not present in the approved content source.

---

## 11. Implementation principles

The visual design should remain realistically reproducible through ordinary web technologies.

Prefer:

- semantic HTML
- CSS Grid
- Flexbox
- CSS custom properties
- normal web typography
- simple CSS or SVG geometry
- static rendering
- progressive enhancement
- accessible interaction states

Avoid implementation choices that require:

- raster compositing
- image-heavy layout reconstruction
- WebGL
- complex canvas rendering
- animation frameworks
- heavy UI component libraries

The site should require approximately zero client-side JavaScript unless a concrete feature later justifies it.

Do not introduce complexity merely because the implementation agent can generate it.

No framework should be allowed to impose its default visual language on the site.

If Astro is selected for implementation, it should function primarily as a static build-time structure and component system, not as an excuse to turn Carambi into a web application.

Shared bilingual content and guide data may be structured centrally where doing so reduces duplication without introducing unnecessary abstraction.

---

## 12. Prototype sequence

Do not attempt to finalize every design variable in one implementation pass.

### Phase 1 — Typography specimen

Completed. The browser specimen compared the English and Chinese candidates using real Carambi copy. Newsreader and LXGW WenKai Regular were selected for the editorial voices; Source Sans 3 and PingFang SC / system sans were selected for the interface voices.

The specimen remains temporary and must not become part of the public site.

### Phase 2 — Desktop prototype

Implement the approved design first at a desktop reference width around 1440 px.

Calibrate:

- content width
- hero size
- line breaks
- serif weight
- guide-row spacing
- metadata alignment
- rule contrast
- olive intensity
- background warmth
- marginal INDEX placement
- footer rhythm

Use browser screenshots for comparison.

### Phase 3 — Mobile

Adapt the approved desktop system to approximately 390 px.

Do not merely compress the desktop grid.

### Phase 4 — Bilingual refinement

Apply the shared system to `/zh/` and adjust Chinese typography independently where necessary.

### Phase 5 — Production details

Only after visual approval, finalize:

- accessibility
- metadata
- canonical URLs
- hreflang
- sitemap
- robots.txt
- font loading
- favicon
- social preview
- 404
- GitHub Pages build and deployment
- custom domain

---

## 13. Current TBD items

The following decisions intentionally remain open until real browser prototypes are reviewed:

1. exact production palette values
2. exact type scale
3. exact line heights
4. exact content width
5. spacing scale
6. breakpoint values
7. final placement and treatment of the desktop INDEX marginal device
8. background materiality strength
9. production delivery strategy for the Chinese webfont

Do not silently resolve these as permanent design decisions during the first implementation pass.

Prototype them and make the differences visible for review.

---

## 14. Visual-reference authority

The visual concept work has already converged.

Use the left-hand **A concept** in `references/carambi-homepage-v3.png` as the primary visual reference for the Pure Refined Editorial direction.

Use the neighboring concepts only selectively:

- archival/marginal concept: reference for one restrained marginal vertical device
- material concept: reference for extremely subtle background warmth and materiality

Do not copy invented text, fake metadata, decorative imagery, or incidental image-generation artifacts from any concept image.

The intended final mixture is approximately:

```text
Primary editorial structure     ≈ 85%
Archival marginal refinement    ≈ 10%
Subtle material refinement      ≈ 5%
```

This ratio describes design influence, not measurable CSS values.

If a generated visual reference conflicts with this document:

**this document takes precedence.**

---

## 15. Final design test

A successful Carambi homepage should communicate, without explanation:

> a carefully authored, long-term home for independently maintained guides and reference projects

The visitor should perceive:

- individual authorship
- methodological care
- editorial refinement
- archival precision
- warmth
- stability

They should not perceive:

- a startup
- a software product
- a generic developer portfolio
- a game portal
- an over-designed branding exercise

The site should remain credible if its fundamental visual system is still in use several years from now.
