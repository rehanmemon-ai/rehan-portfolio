# Technical Architecture & Engineering Design

This document details the software architecture, design principles, rendering pipeline, and technical specifications of Rehan Memon's professional engineering portfolio.

---

## 1. Core Architectural Philosophy

The portfolio is designed as an ultra-fast, zero-dependency, static web product engineered for durability, accessibility, and high recruiter trust.

### Key Architectural Tenets
1. **Zero Runtime Framework Overhead:** No heavy single-page application framework (React, Vue, Angular) is loaded on the static portfolio pages themselves. Pages are delivered as lightweight, semantic HTML5 with modular CSS3.
2. **Determinism via Single-Script Generation:** All 17 site pages, navigation headers, metadata, schema markup, and sitemaps are deterministically synthesized by a centralized Python generator (`build_site.py`) using Python standard library modules only (`re`, `html`, `os`, `sys`).
3. **Automated Verification Gate:** No page is committed or deployed without passing an automated integrity audit (`check_site.py`) that enforces route completeness, link validity, single-H1 hierarchy, anchor consistency, and asset presence.
4. **Dark-First Modern UI:** Designed around a high-contrast dark-mode color token system inspired by modern developer platforms (Linear, GitHub, Raycast).

---

## 2. System Overview & Directory Structure

```
rehan-portfolio/
├── build_site.py          # Authoritative static site generator (17 routes)
├── check_site.py          # Automated verification suite (links, routes, anchors)
├── site.css               # Consolidated, scoped design system stylesheet
├── site.js                # Vanilla JavaScript for navigation, filters, copy actions
├── sitemap.xml            # SEO sitemap generated deterministically
├── index.html             # Homepage
├── about.html             # Candidate biography & background
├── experience.html        # Commercial internships & industry experience
├── projects.html          # Flagship projects index (4 pillars)
├── connecthub.html        # Flagship Deep Dive: ConnectHub Real-Time Messaging Engine
├── ai-research-assistant.html # Flagship Deep Dive: AI Research Assistant (RAG)
├── signature-verification.html # Flagship Deep Dive: Signature Verification ML System
├── job-search-automation.html  # Flagship Deep Dive: Autonomous Job Search Engine
├── automation.html        # n8n Workflow Automation Hub (Canonical Sequence 01..10)
├── automation-evidence.html # Automation verification logs & technical audit
├── credentials.html       # Verified Credentials & Certifications Matrix (48 items)
├── client-work.html       # Client engineering (Advfiction LMS, Girls HSS, SAHASH)
├── advfiction.html        # Commercial Case Study: Advfiction Private Limited
├── awarewolf.html         # Commercial Case Study: Awarewolf Media
├── algodevopss.html       # Commercial Case Study: AlgoDevOpss Portal
├── activities.html        # Hackathons, Leadership, University Extension (DLLE)
├── contact.html           # Professional contact channels & CV access
├── docs/                  # Engineering & maintainer documentation suite
│   ├── README.md
│   ├── ARCHITECTURE.md
│   ├── CONTENT_GUIDE.md
│   ├── RELEASE_GUIDE.md
│   └── PRIVACY_RULES.md
├── assets/                # Static images, favicon, and documents
│   ├── favicon.svg
│   ├── rehan-portrait.webp
│   └── documents/         # Privacy-safe derivative PDFs and reference offers
│       ├── iirs-outreach/ # 21 PII-redacted IIRS/ISRO participation copies
│       └── appointment-only-offers/ # 5 virtual appointment offer letters
└── diagrams/              # Custom SVG technical architecture flowcharts
    ├── connecthub-pipeline.svg
    ├── job-search-pipeline.svg
    └── signature-verification-pipeline.svg
```

---

## 3. The Generation Pipeline (`build_site.py`)

`build_site.py` functions as a headless CMS and compiler. It defines structured Python data structures and transforms them into static HTML:

```
+-----------------------------------------------------------+
|                    build_site.py                          |
|                                                           |
|  [PROJECTS]  [EXPERIENCES]  [CREDENTIALS]  [WORKFLOWS]    |
|       |             |              |            |         |
|  +----+-------------+--------------+------------+----+    |
|  |       Component Builders & Template Engine        |    |
|  |       (header, footer, card, badge, nav_group)    |    |
|  +----+----------------------------------------------+    |
|       |                                                   |
|       v                                                   |
|  17 Static HTML Files + sitemap.xml                       |
+-----------------------------------------------------------+
```

### Rendering Process
1. **Data Definitions:** Projects, credentials, work experiences, workflows, and activities are declared as typed dictionaries.
2. **Component Helpers:**
   - `header(active_href)`: Produces accessible top navigation with active-route highlighting.
   - `footer()`: Standardized global footer with timestamp, GitHub repo link, and legal privacy notices.
   - `project_card(p)`: Standardized card with category eyebrow, status badge, tech tags, and CTA buttons.
   - `credential_card(c)`: Multi-filter card supporting search by title, issuer, domain, and tags.
   - `case_row(title, text)`: Step-by-step numbered breakdown for technical case studies.
   - `explore_more(current_route)`: Contextual cross-links at the foot of deep-dive pages.
3. **File Output:** Every route in `PAGES` dictionary is written directly to the repository root with UTF-8 encoding.

---

## 4. Design System & CSS Token Architecture (`site.css`)

The stylesheet is built upon a strict design token hierarchy in `:root`:

### Color Tokens
- Background Base: `--bg: #090d16` (Deep blue-black)
- Surface Cards: `--surface: #0f172a` (Elevated slate)
- Card Elevated: `--surface-elevated: #162036` (Hover/focus state)
- Border Subtle: `--border: rgba(148, 163, 184, 0.12)`
- Accent Teal: `--accent: #14b8a6` (Primary interactive color)
- Accent Bright: `--accent-bright: #2dd4bf`
- Text Primary: `--text-primary: #f8fafc`
- Text Muted: `--text-muted: #94a3b8`

### Layout & Spacing
- Grid System: 12-column responsive fluid CSS grid (`.grid`, `.grid.two`, `.grid.three`).
- Typography Scale: Modular scale using standard fluid clamp expressions.
- Card Pinning: Flexbox-driven `.card { display: flex; flex-direction: column; }` with `.card-actions { margin-top: auto; }` ensuring visual alignment of CTA buttons regardless of card body text length.

---

## 5. Client-Side JavaScript Architecture (`site.js`)

`site.js` contains zero external dependencies. It provides 4 targeted features:
1. **Mobile Navigation Drawer:** Accessible toggle for mobile viewports with ARIA attributes (`aria-expanded`, `aria-hidden`).
2. **Interactive Filtering System:** Instant clientside filtering on `credentials.html` and `projects.html` by category, issuer, and live text search query.
3. **Email Clipboard Action:** One-click copy interaction on `contact.html` with accessible tooltip feedback.
4. **Header Scroll Elevation:** Adds subtle glassmorphism border shadow when the user scrolls down the page.

---

## 6. Accessibility & SEO Compliance

- **Semantic HTML5:** Strict use of `<main>`, `<header>`, `<nav>`, `<article>`, `<section>`, and `<footer>`.
- **Single-H1 Standard:** Enforces exactly one `<h1>` per page across all 17 routes.
- **Image Optimization:** All images specify explicit `width`, `height`, `loading="lazy"`, and descriptive `alt` attributes.
- **Structured Data:** Full `schema.org/Person` JSON-LD embedded on the homepage.
- **Target Link Security:** All outbound links include `target="_blank" rel="noopener noreferrer"`.
