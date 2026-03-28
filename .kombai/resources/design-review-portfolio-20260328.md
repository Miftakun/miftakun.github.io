# Design Review Results: Miftakun Niam Portfolio

**Review Date**: 2026-03-28  
**Route**: `/` (Single-page portfolio — miftakun.github.io)  
**Focus Areas**: Visual Design · UX/Usability · Responsive/Mobile · Accessibility · Micro-interactions/Motion · Consistency

---

## Summary

The portfolio has a strong monochromatic foundation with good interactive touches (particles, tilt, smooth scroll, dark mode). However, several critical bugs (broken viewport meta, duplicate IDs, empty aria-labels) hurt accessibility and mobile rendering. The overall structure suffers from content duplication, an underutilised Contact section, and significant CSS bloat from duplicated rule blocks that inflate file size without benefit.

---

## Issues

| # | Issue | Criticality | Category | Location |
|---|-------|-------------|----------|----------|
| 1 | **Broken viewport meta tag** — missing comma between `width=device-width` and `initial-scale=1` causes `initial-scale` to be silently ignored on many mobile browsers, breaking mobile zoom behavior | 🔴 Critical | Responsive | `index.html:6` |
| 2 | **Empty `aria-label` attributes on card action links** — `aria-label="Visit "` provides no meaningful description for screen readers on multiple project card buttons | 🔴 Critical | Accessibility | `index.html:601, 607, 640, 645, 676, 681` |
| 3 | **Duplicate `id="logo-container"`** — the same id is used in both the desktop sidebar and mobile nav, which is invalid HTML and can break JS and accessibility tooling | 🔴 Critical | Accessibility | `index.html:100, 196` |
| 4 | **INP score 352ms** (threshold for "Good" is ≤200ms) — excessive concurrent JS (particles + vanilla-tilt + magnetic effect + Lenis RAF + scroll listeners) causes slow interaction responsiveness, especially on mid-range Android | 🟠 High | Performance | `index.html:1192–1651` |
| 5 | **Total page payload ~5.75MB** — all project images are unoptimised JPG/PNG; converting to WebP with `loading="lazy"` and `width`/`height` attributes would reduce this by 60–70% | 🟠 High | Performance | `assets/img/*.png, *.jpg` |
| 6 | **Dark overlay (rgba 0,0,0,0.4) over a light dotted hero** — the result is a mid-grey hero (#888 equivalent) with dark `#121212` text, producing ~2.5:1 contrast ratio — below the WCAG AA minimum of 4.5:1 for normal text | 🟠 High | Accessibility | `style.css:387–393`, `index.html:250` |
| 7 | **Entire CSS rule blocks duplicated in `monochrome.css`** — `.reveal-item`, `.filter-controls`, `.filter-btn`, `.filter-item`, `.back-to-top`, `#particles-js`, dark mode overrides, `.theme-toggle-fab` and `.music-toggle-btn` are all defined twice (lines ~948–1030 and again ~1322–1415+), adding ~600 lines of dead CSS | 🟠 High | Consistency | `assets/css/monochrome.css:948–1030, 1322–1415` |
| 8 | **Contact section is a full-height section with only 4 links** — the remaining 60%+ of the viewport is empty white space. No contact form exists; visitors cannot message directly from the site | 🟠 High | UX/Usability | `index.html:1045–1089` |
| 9 | **Experience role title uses `position: absolute; right: 38px; top: 35px`** — on viewports 768–992px the role title and company name overlap due to absolute positioning not accounting for the logo column | 🟠 High | Responsive | `style.css:405–409` |
| 10 | **Hero content not vertically centred** — `.intro-content` is top-aligned inside the `full-height` hero section; the bottom ~40% of the hero is empty on all screen sizes, wasting prime above-the-fold space | 🟡 Medium | Visual Design | `monochrome.css:333–338`, `index.html:253` |
| 11 | **Both "Project Designs" and "Project Apps" nav items share the same icon** (`mdi-av-my-library-books`) — no visual distinction between two major portfolio sections in the sidebar | 🟡 Medium | Consistency | `index.html:122, 129` (desktop nav), `index.html:213, 219` (mobile nav) |
| 12 | **Section heading style (black bar h3) clashes with the rest of the minimal design** — uppercase white text on a full-width solid black bar reads like a legacy Materialize default, inconsistent with the refined card/sidebar aesthetic established elsewhere | 🟡 Medium | Visual Design | `style.css:324–330`, all `<h3 class="page-title white-text teal">` in `index.html` |
| 13 | **Nested cards in Skills section** — three `<div class="card">` elements are nested inside a parent `<div class="card">`, creating an invalid Materialize structure and a visually confusing indent of card shadows | 🟡 Medium | Visual Design | `index.html:844–971` |
| 14 | **About section duplicates the Skills section's content** — the unordered list (Languages, Databases, Libraries, Frameworks, Tools) appears verbatim in About and is then repeated in the dedicated Skills section | 🟡 Medium | UX/Usability | `index.html:351–357` |
| 15 | **`small { display: none }` globally hides all `<small>` elements** — this removes the "Accomplishments" label inside card reveals, leaving only an orphaned close icon with no context | 🟡 Medium | UX/Usability | `style.css:569–571` |
| 16 | **No `focus-visible` outline on interactive elements** — clicking or tabbing to `.readme`, `.contactme`, `.icon-btn`, and nav links shows no visible focus ring, blocking keyboard-only navigation | 🟡 Medium | Accessibility | `assets/css/monochrome.css` (global button overrides) |
| 17 | **Code snippet `<div>` is not `aria-hidden="true"`** — the decorative code block in the hero is read aloud by screen readers as raw code text, creating a confusing experience | 🟡 Medium | Accessibility | `index.html:264–282` |
| 18 | **jQuery v1.11.2 (2014) & Materialize CSS v0.95.3 (2015)** — both libraries are a decade old and unmaintained; jQuery v1 has known security issues and Materialize 0.95 pre-dates Material Design 2/3 | 🟡 Medium | Consistency | `index.html:1141, 1144` |
| 19 | **LinkedIn contact link shows raw URL** (`https://id.linkedin.com/in/miftakun-niam`) instead of a clean handle — inconsistent with the other contact links which use short display text | ⚪ Low | Visual Design | `index.html:1084–1086` |
| 20 | **Font Awesome v4.3.0 is significantly outdated** — FA6 Free has 2000+ additional icons, improved accessibility attributes, and CDN performance improvements | ⚪ Low | Consistency | `index.html:33` |
| 21 | **Music toggle button and back-to-top button can visually stack on mobile** — the sibling CSS selector `.back-to-top.show ~ .music-toggle-btn` only works if the elements are adjacent siblings in the DOM, but they are not — a `<button>` and `<a>` separated by the `<audio>` element, so the selector may never fire | ⚪ Low | Responsive | `monochrome.css:1834`, `index.html:1102–1122` |
| 22 | **No "skip to main content" link** — keyboard and screen reader users must tab through the entire 8-item sidebar before reaching the main content on every page load | ⚪ Low | Accessibility | `index.html:88` (before `<body>` children) |
| 23 | **`bg.png` tiled grid on `<main>` background is invisible on top of section backgrounds** — it adds an HTTP request with no visible design benefit in the current light theme | ⚪ Low | Performance | `style.css:227–229` |

---

## Criticality Legend

| Level | Meaning |
|---|---|
| 🔴 **Critical** | Breaks functionality or violates accessibility / web standards |
| 🟠 **High** | Significantly impacts user experience, performance, or design quality |
| 🟡 **Medium** | Noticeable issue that should be addressed |
| ⚪ **Low** | Nice-to-have improvement with minimal impact |

---

## Next Steps (Recommended Priority Order)

### Immediate fixes (Critical — no design changes needed)
1. **Fix viewport meta**: Add the missing comma → `content="width=device-width, initial-scale=1"`
2. **Fix empty aria-labels**: Replace `aria-label="Visit "` with descriptive text on all 6 project card action links
3. **Remove duplicate `id="logo-container"`**: Change one to `id="logo-container-mobile"`

### Short-term (High impact)
4. **Deduplicate monochrome.css**: Remove the ~600 lines of duplicated CSS (items #7)
5. **Fix hero contrast**: Remove the `.overlay` div in the hero or change hero background to a dark pattern so the overlay makes sense — or switch to light text throughout the hero
6. **Centre hero content vertically**: Add `display: flex; align-items: center; min-height: 100vh` to `#intro.section .container`
7. **Replace absolute role title** with `display: flex; justify-content: space-between` in the experience card header row
8. **Add contact form** to the Contact section (name, email, message + submit button using Formspree or similar static-site form service)

### Medium-term (Design polish)
9. **Redesign section headings** — replace the black bar `h3` with an inline accent-bordered heading (already partially done via the `border-left` style in monochrome.css — remove the `.teal` class and rely solely on monochrome styles)
10. **Redesign Skills section** — flatten the nested card structure into a single card with grouped pill/tag chips per category
11. **Remove skill list from About** — let the About section focus purely on narrative; the Skills section handles the technical list
12. **Add `aria-hidden="true"` and `role="presentation"`** to the code snippet decoration div
13. **Add `focus-visible` styles** for keyboard navigation

### Future upgrades
14. Convert all project images to WebP and add explicit `width`/`height`
15. Remove jQuery and replace Materialize side-nav initialisation with ~20 lines of vanilla JS
16. Upgrade Font Awesome to v6 Free CDN
17. Add a "Skip to main content" `<a>` as the first child of `<body>`

---

## Strengths Worth Preserving

- ✅ Dark mode with `prefers-color-scheme` detection + localStorage persistence
- ✅ View Transitions API for smooth theme toggle animation
- ✅ Lenis smooth scroll with Awwwards-quality easing
- ✅ Magnetic button effect on CTAs and social icons
- ✅ Intersection Observer scroll reveal with staggered card delays
- ✅ Custom SVG cursor with `mix-blend-mode: difference`
- ✅ Project filter system with animated show/hide
- ✅ Particle density adapts to mobile viewport
- ✅ Responsive sidebar → hamburger menu switch
- ✅ Good SEO meta tags, Open Graph, and Twitter Card
