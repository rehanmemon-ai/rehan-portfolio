# Rehan Memon Portfolio — Maintainer & Architecture Documentation

Internal engineering and maintenance documentation for Rehan Juned Memon's static portfolio repository.

## Documentation Suite

| Document | Purpose |
| :--- | :--- |
| **[ARCHITECTURE.md](ARCHITECTURE.md)** | Static generation engine (`build_site.py`), CSS design tokens, host security header guidance, and vanilla JavaScript modules (`site.js`, `theme-init.js`). |
| **[CONTENT_GUIDE.md](CONTENT_GUIDE.md)** | Exact Python dictionary schemas for `PROJECTS`, `EXPERIENCE`, `CREDENTIALS`, and canonical `WF-01..WF-10` order. |
| **[RELEASE_GUIDE.md](RELEASE_GUIDE.md)** | CI quality gates (`check_site.py`, `pytest`, `ruff`, `bandit`, `html-validate`), Git branch policies, and release verification steps. |
| **[PRIVACY_RULES.md](PRIVACY_RULES.md)** | Candidate privacy firewall, PII exclusions, withheld-ID rules, and the public-safe derivative PDF pipeline. |
| **[CONNECTHUB_DEMO_SCRIPT.md](CONNECTHUB_DEMO_SCRIPT.md)** | 3-minute ConnectHub walkthrough script and shot list for live demonstrations. |

---

## Quick Start for Maintainers

### Prerequisites
- Python 3.11 (standard library only for `build_site.py` and `check_site.py`; optional pinned dev packages in `.github/requirements-ci.txt` for `pytest`, `ruff`, and `bandit`)
- Node.js 24+ (or `>=22.22.0`) and npm (for `node --check` and pinned `html-validate` via `package-lock.json`)
- Git

### Build and Verify Commands
```bash
# 1. Regenerate all 17 routes, sitemap.xml, and robots.txt
python -B build_site.py

# 2. Run structural, link, CSS token, SEO, and privacy checks
python -B check_site.py

# 3. Run unit and determinism tests
python -m pytest tests/

# 4. Lint Python & check HTML5/JS syntax
python -m ruff check build_site.py check_site.py tests/
node --check site.js && node --check theme-init.js
npx --no-install html-validate *.html

# 5. Preview locally on loopback only
python -m http.server 8765 --bind 127.0.0.1
```

---

## Governance & Safety Guarantees
- **Branch Protection:** Never push directly to `main`. Develop on feature branches, pass all automated checks, and pause for review before committing or merging.
- **Privacy Firewall:** Never commit unredacted government identification, university roll/seat numbers, withheld Drive IDs, or private compensation details. See [PRIVACY_RULES.md](PRIVACY_RULES.md).
