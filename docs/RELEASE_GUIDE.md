# Release & Quality Assurance Guide

Runbook defining automated verification gates, CI reproducibility, and Git branch governance.

---

## 1. Release Governance & Branch Policies

### Strict Prohibitions
- **NEVER** run `git push origin main` without explicit approval.
- **NEVER** run `git commit -a`, `git reset --hard`, or `git clean -fd` autonomously.
- **NEVER** deploy automatically without review of `git status` and `git diff`.

### Standard Release Workflow
1. Work on a feature branch: `git checkout -b feat/<release-name>`
2. Edit `build_site.py`, `site.css`, `site.js`, `theme-init.js`, or docs.
3. Rebuild deterministic outputs: `python -B build_site.py`
4. Run the complete verification suite (below).
5. Inspect `git status` and `git diff`, then request release approval before staging/committing/pushing.

---

## 2. Automated Pre-Flight Verification Suite

All checks below run cleanly in CI (`.github/workflows/quality.yml` using Python `3.11` and Node.js `24`):

```bash
# 1. JavaScript syntax checks
node --check site.js
node --check theme-init.js

# 2. Deterministically rebuild all 17 routes, sitemap.xml, and robots.txt
python -B build_site.py

# 3. Verify generated files match git working tree cleanly
test -z "$(git status --porcelain -- *.html sitemap.xml robots.txt)"

# 4. Structural, SEO, CSS custom-property, privacy, and anchor integrity check
python -B check_site.py

# 5. Unit, determinism, escaping & regression tests
python -m pytest tests/

# 6. Python AST & security linting (configured in pyproject.toml)
python -m ruff check build_site.py check_site.py tests/
python -m bandit -r build_site.py check_site.py tests/ -ll -q

# 7. Strict HTML5 validation (no-inline-style: error via .htmlvalidate.json)
npm ci --ignore-scripts
npx --no-install html-validate *.html
```

### What `check_site.py` Validates
- Exactly `17` `.html` routes, `14` projects (`5 / 5 / 4` pillars), `48` credentials, `21` IIRS PDFs.
- Single `<h1>`, non-skipped heading hierarchy, `<main id="main" tabindex="-1">`, unique IDs.
- Matching `<link rel="canonical">`, `og:url`, `og:image`, non-empty `<meta name="description">`, and `noindex` on `automation-evidence.html`.
- Valid Schema.org JSON-LD payload on `index.html`.
- `sitemap.xml` canonical URL parity (`https://rehanmemon-ai.github.io/rehan-portfolio/` root + 15 routes) and `robots.txt` directives.
- Zero inline `style=` attributes, all CSS `var(--...)` defined in `site.css`, and `#credentialSubject` / `#credentialType` filter option completeness.
- Zero `javascript:`/`data:` URI schemes, zero withheld Drive IDs, and zero local filesystem paths across HTML and source/docs.

---

## 3. Browser & Accessibility Inspection

Serve locally on loopback before release approval:
```bash
python -m http.server 8765 --bind 127.0.0.1
```
Verify light/dark theme toggle, desktop & mobile responsive layout (`1280px` & `390px`), backward `Shift+Tab` focus clearance under the sticky header, `#diagramModal` keyboard trap/focus return, `credentials.html` subject/type filters, and `contact.html` email copy status announcements.
