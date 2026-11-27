# Technical Architecture & Engineering Design

This document details the software architecture, static generation pipeline, design system tokens, client-side JavaScript modules, and hosting security trade-offs of Rehan Juned Memon's portfolio.

---

## 1. Core Architectural Philosophy

The portfolio is a dependency-free static web application built for fast initial load, WCAG 2.2 AA accessibility, deterministic output, and evidence-backed technical clarity.

### Key Architectural Tenets
1. **Zero Runtime Framework Overhead:** Plain semantic HTML5 and vanilla CSS3/ES6+ JavaScript (`site.js`, `theme-init.js`) with zero external UI frameworks or third-party font/analytics requests.
2. **Deterministic Static Compilation:** All 17 HTML routes, `sitemap.xml`, and `robots.txt` are generated deterministically by `build_site.py` using Python standard library modules (`html.escape`, `json`, `pathlib.Path`, `urllib.parse.urlsplit`).
3. **Automated Quality Gate:** Generated pages must pass `check_site.py`, `pytest`, `ruff`, `bandit`, `node --check`, and strict `html-validate` (`no-inline-style: error`).
4. **Dark-First Dual-Theme UI:** High-contrast dark palette in `:root` / `html.dark` paired with an accessible light palette in `html.light`.

---

## 2. System Overview & Directory Structure

```
rehan-portfolio/
├── build_site.py                  # Authoritative static generator (17 routes, sitemap.xml, robots.txt)
├── check_site.py                  # Automated structural, link, CSS var, SEO & privacy verifier
├── site.css                       # Consolidated design system & responsive layout stylesheet
├── site.js                        # Theme toggle, mobile drawer, filter controls, lightbox modal, copy button
├── theme-init.js                  # Early head script preventing dark/light theme FOUC under strict CSP
├── package.json                   # Pinned html-validate devDependency (v11.22.1)
├── package-lock.json              # Exact Node dependency lockfile
├── .htmlvalidate.json             # Strict HTML5 validation config (no-inline-style: error)
├── pyproject.toml                 # Ruff rule configuration (E4, E7, E9, F, B, W, S)
├── vercel.json                    # HTTP security headers for optional Vercel deployment
├── .github/
│   ├── requirements-ci.txt        # Pinned Python CI dependencies (pytest, ruff, bandit, etc.)
│   └── workflows/quality.yml      # GitHub Actions CI verification gate (Python 3.11 + Node 24)
├── tests/
│   └── test_portfolio.py          # Pytest regression, schema, determinism & escaping tests
├── docs/                          # Maintainer guides (ARCHITECTURE, CONTENT_GUIDE, RELEASE_GUIDE, PRIVACY_RULES, CONNECTHUB_DEMO_SCRIPT)
├── assets/
│   ├── social-card.png            # 1200x630 Open Graph / Twitter card image
│   ├── workflows/                 # 12 sanitized n8n editor captures
│   └── documents/
│       ├── iirs-outreach/         # 21 PII-redacted IIRS/ISRO participation PDFs
│       └── appointment-only-offers/ # 5 sanitized internship reference offer PDFs
├── diagrams/
│   ├── connecthub-pipeline.svg
│   ├── job-search-pipeline.svg
│   ├── research-pipeline.svg
│   └── signature-pipeline.svg
├── favicon.svg / favicon.ico / favicon-16x16.png / favicon-32x32.png / apple-touch-icon.png
├── index.html .. contact.html     # 17 generated static HTML5 pages (including automation-evidence.html consolidation notice)
├── robots.txt                     # Search crawler rules + Sitemap URL
└── sitemap.xml                    # Canonical indexable route list (16 indexable URLs)
```

---

## 3. Generation Pipeline (`build_site.py`)

`build_site.py` stores structured lists (`PROJECTS`, `EXPERIENCE`, `CREDENTIALS`, `N8N_AUTOMATION_FEATURED`, `NAV`, `PAGES`) and renders each page via shared template helpers:

- `validate_href(href)` / `link(href, label, css, external)`: Enforces safe URI schemes (`https`, `http`, `mailto`, relative) and enforces `rel="noopener noreferrer"` on `target="_blank"`.
- `intro(...)`, `section(...)`, `case_row(...)`, `explore_more(current)`: Shared layout sections, headings, and contextual navigation blocks.
- `project_card(item)`, `experience_card(item)`, `credential_card(item)`: Card renderers for the homepage, `projects.html`, `experience.html`, and `credentials.html`.
- `workflow_index()`, `evidence_status_legend()`, `workflow_example(...)`, `workflow_image(...)`: Canonical `01..10` n8n gallery builders for `automation.html`.
- `_SCHEMA_PAYLOAD` / `SCHEMA_JSON_LD`: Serialized with `json.dumps` (`Person` + `CollegeOrUniversity` `affiliation`) and embedded only on `index.html`.
- `render(filename, item)` + `generate_sitemap()` + `generate_robots()`: Writes all 17 `.html` files, `sitemap.xml` (canonical root `https://rehanmemon-ai.github.io/rehan-portfolio/` plus 15 other routes, excluding `noindex` `automation-evidence.html`), and `robots.txt`.

---

## 4. Design System & CSS Tokens (`site.css`)

- Dark-first tokens (`:root` / `html.dark`): `--paper: #0d171c`, `--surface: #17242a`, `--ink: #eef4f0`, `--muted: #b4c6c5`, `--line: #384e54`, `--accent: #70d8d0`, `--soft: #163436`, `--focus: #a6f1eb`, `--input-border: #5c7981`.
- Light theme (`html.light`): `--paper: #f7f7f2`, `--surface: #ffffff`, `--ink: #142029`, `--muted: #53616a`, `--accent: #077077`, `--soft: #eaf5f3`, `--input-border: #7c8e88`.
- Sticky-header focus clearance: `html { scroll-padding-top: 5.5rem; }` and `[id] { scroll-margin-top: 5.5rem; }` satisfy WCAG 2.2 SC 2.4.11 Focus Not Obscured during backward `Shift+Tab` and fragment navigation.
- Card action alignment: `.card { display: flex; flex-direction: column; }` with `.card-actions { margin-top: auto; }`.

---

## 5. Client-Side JavaScript Architecture (`theme-init.js` & `site.js`)

1. **`theme-init.js` (synchronous `<head>` loader):** Reads `localStorage.getItem('theme')` cleanly inside `try/catch` before paint so light-mode users see no dark-theme flash without requiring `'unsafe-inline'` in CSP.
2. **Theme Toggle (`#themeToggle`):** Switches `html.dark` / `html.light`, updates `meta[name="theme-color"]` and button `aria-label`.
3. **Mobile Navigation Drawer (`#mobileMenuBtn` / `#mobileMenu`):** Toggles `hidden`, `aria-expanded`, and closes on link click, `Escape`, or `focusout` outside `.site-header`.
4. **Interactive Directory Filters (`[data-filter-list]`):** Instant clientside filtering on `projects.html` (pillar pills, search input, pillar `<select>`) and `credentials.html` (domain pills, search input, type `<select>`, subject `<select>`) with `role="status" aria-live="polite"` count updates.
5. **Accessible Lightbox Modal (`#diagramModal`):** Traps focus (`Tab`/`Shift+Tab`), marks background landmarks `inert` while open, closes on `Escape`/backdrop click, and restores focus to the invoking trigger on close.
6. **Clipboard Copy (`.copy-email-btn`):** Dual-tier async `navigator.clipboard.writeText` + `document.execCommand('copy')` fallback that restores prior focus, clears overlapping timers cleanly, and announces success/failure in `.copy-email-status` (`role="status"`).

---

## 6. Security Headers, SEO & Hosting Constraints

- **Meta CSP & Referrer Policy:** Every HTML page enforces `default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self' data:; object-src 'none'; base-uri 'self'; form-action 'none'` via `<meta http-equiv="Content-Security-Policy">` plus `<meta name="referrer" content="strict-origin-when-cross-origin">`.
- **GitHub Pages Limitation vs Vercel:** GitHub Pages serves static files without custom HTTP response headers, so `X-Frame-Options`, `X-Content-Type-Options`, `Permissions-Policy`, and HTTP CSP `frame-ancestors 'none'` cannot be set on GitHub Pages alone (browsers ignore `<meta http-equiv="X-Frame-Options">`). `vercel.json` configures those full HTTP response headers when hosted on Vercel.
- **Canonicalization:** `automation-evidence.html` emits `<meta name="robots" content="noindex, follow">`, sets canonical/OG URL to `automation.html`, and is omitted from `sitemap.xml` while `robots.txt` retains `Allow: /` so crawlers can observe the `noindex` tag.
