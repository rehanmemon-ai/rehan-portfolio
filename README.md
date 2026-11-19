# Rehan Memon — Professional Engineering Portfolio

A dependency-free static engineering portfolio. The 17 semantic HTML pages are generated from reviewed content in `build_site.py`; `site.css`, `site.js`, and `favicon.svg` are clean local assets. Legacy Phase 1 files (`style.css`, `main.js`) have been safely archived to Central HQ.

## Architecture & Content Pillars

The portfolio is structured around three core engineering pillars:
1. **AI & Machine Learning Systems**: Computer vision, RAG and LLM systems, feature extraction and backend prototypes (Signature Verification AI, ConnectHub, AI Research Assistant).
2. **Client & Collaborative Engineering**: Publicly linked client and team work with contribution boundaries (Advfiction LMS and website, Girls HSS portal, and independent sites).
3. **AI & Workflow Automation**: Ten n8n workflow canvases in the exact owner sequence, with editor tests, partial executions, and design-stage items labeled separately.

### The 17 Semantic Routes
- `index.html`: Executive engineering overview, pillars, and flagship highlights
- `projects.html`: Comprehensive 14-project directory across 3 pillars
- `experience.html`: Direct professional internships & 5 appointment-only virtual offers
- `credentials.html`: 48 credential and recognition records, including 21 locally redacted IIRS participation documents
- `automation.html`: Canonical 10-workflow n8n automation gallery
- `about.html`: Technical biography, methodology, and engineering principles
- `contact.html`: Communication channels, direct links, and verified profiles
- `activities.html`: Extracurricular leadership, university extension, and public speaking
- `signature-verification.html`: Flagship Case Study — Offline Signature Verification AI
- `connecthub.html`: In-development real-time messaging case study
- `job-search-automation.html`: Flagship Case Study — Autonomous Job Search Engine
- `ai-research-assistant.html`: Deep Dive — AI Research Assistant Bot (ChromaDB + Groq)
- `advfiction.html`: Deep Dive — Advfiction AI Automation & Fullstack LMS
- `algodevopss.html`: Deep Dive — AlgoDevOpss & KJSIEIT Academic Portal
- `awarewolf.html`: Deep Dive — AwareWolf Media Ingestion Pipeline Remediation
- `client-work.html`: Comprehensive Institutional & Client Deliverables Index
- `automation-evidence.html`: Compatibility redirect to the canonical automation gallery

## Build, Test & Preview

Maintain the site in `build_site.py`: add projects to `PROJECTS`, employer engagements to `EXPERIENCE`, credentials to `CREDENTIALS`, and workflow cards in the `automation.html` page definition and `workflow_index()`. Update a page's `PAGES` entry for its case study. Rebuild generated HTML after each change; do not edit generated HTML alone.

Build and verify:

```powershell
python -B build_site.py
python -B check_site.py
node --check site.js
git diff --check
```

### Local Manual Review Server
To preview the site locally in any browser without external browser automation:

```powershell
python -m http.server 8765 --bind 127.0.0.1
```

Open `http://127.0.0.1:8765/` in your browser.

All page links and assets are relative to the current HTML file, and all generated pages live in the repository root. No third-party package managers, build frameworks, analytics, or external runtimes are required.

## Publication & Evidence Governance

Private evidence registers are held outside this repository. Public offer copies in `assets/documents/appointment-only-offers/` establish appointments only; they do not prove completion. The linked credential documents were matched to their source records in the local closeout review; candidate acceptance and issuer-side validation remain separate. Do not publish candidate identifiers, confidential offer terms, or private source documents. No commit, push, merge, or deployment is authorized for this local closeout work.
