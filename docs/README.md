# Rehan Memon Portfolio — Maintainer & Architecture Documentation

Welcome to the internal engineering and maintenance documentation for Rehan Memon's professional engineering portfolio.

## Documentation Suite

This folder provides a complete reference for managing, extending, building, and deploying the portfolio:

| Document | Purpose |
| :--- | :--- |
| **[ARCHITECTURE.md](ARCHITECTURE.md)** | Technical design, static generation engine (`build_site.py`), CSS design system, typography, accessibility, and client-side JavaScript architecture. |
| **[CONTENT_GUIDE.md](CONTENT_GUIDE.md)** | Schema definitions and step-by-step instructions for adding new projects, commercial internships, certifications, university coursework, and activities. |
| **[RELEASE_GUIDE.md](RELEASE_GUIDE.md)** | Pre-flight release verification checklists, automated integrity tests (`check_site.py`), Git branch protection policies, and deployment workflows. |
| **[PRIVACY_RULES.md](PRIVACY_RULES.md)** | Candidate privacy firewall, mandatory PII exclusions (Aadhaar, PAN, registration/roll numbers), and the public-safe document sanitization pipeline. |
| **[CONNECTHUB_DEMO_SCRIPT.md](CONNECTHUB_DEMO_SCRIPT.md)** | 3-minute technical walkthrough presentation script and demonstration shot list for recruiter showcases. |

---

## Quick Start for Maintainers

### Prerequisites
- Python 3.10+ (standard library only; no third-party package dependencies required for core build)
- Node.js 18+ (for JavaScript syntax validation)
- Git

### Build and Verify Commands
```bash
# 1. Regenerate all 17 portfolio routes and sitemap
python build_site.py

# 2. Run automated structural, route, anchor, asset, and accessibility checks
python check_site.py

# 3. Validate client-side JavaScript syntax
node --check site.js

# 4. Preview the local site
python -m http.server 8765
# Open http://127.0.0.1:8765 in your browser
```

---

## Governance & Safety Guarantees
- **Branch Protection:** Never push directly to `main`. All releases must be developed on feature branches, pass `check_site.py` with zero errors, and undergo explicit review.
- **Privacy Firewall:** Never commit raw, unredacted government identification, university roll/seat numbers, or private offer compensation letters to the public repository. Consult [PRIVACY_RULES.md](PRIVACY_RULES.md).
