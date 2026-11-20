# Rehan Memon — Professional Engineering Portfolio

[![Verification Gate](https://img.shields.io/badge/Verification%20Gate-17%2F17%20Routes%20Passing-emerald?style=flat-square)](check_site.py)
[![Architecture](https://img.shields.io/badge/Architecture-Zero--Dependency%20Static%20HTML5-blue?style=flat-square)](docs/ARCHITECTURE.md)
[![Privacy Audit](https://img.shields.io/badge/Privacy%20Firewall-PII--Sanitized-purple?style=flat-square)](docs/PRIVACY_RULES.md)

Welcome to the open-source repository for Rehan Memon's professional engineering portfolio.

The portfolio is an ultra-fast, dependency-free static web application engineered for maximum accessibility, technical clarity, and recruiter trust. All 17 semantic HTML routes are deterministically synthesized by a centralized Python generator (`build_site.py`) with zero third-party framework overhead.

---

## 🏛️ Engineering Pillars & Flagship Systems

The portfolio showcases production systems, research prototypes, and automated pipelines across three core disciplines:

### 1. AI, Machine Learning & Computer Vision
- **[Signature Verification AI](signature-verification.html):** Offline handwritten signature verification system trained on the CEDAR dataset with OpenCV preprocessing, 331 handcrafted geometric and texture features, and RBF SVM classification (65.91% baseline accuracy on writer-disjoint splits).
- **[ConnectHub Real-Time Messaging Engine](connecthub.html):** Full-stack FastAPI + PostgreSQL + WebSocket messaging engine with Google Gemini room summaries and JSONB vector similarity search. Deployed live on Render.
- **[AI Research Assistant](ai-research-assistant.html):** Context-aware multi-modal research assistant built on ChromaDB, LangChain, Groq Llama 3, and PDF ingestion.
- **[Autonomous Job Search Engine](job-search-automation.html):** Local-first multi-agent job discovery, qualification, and notification engine with local Ollama evaluation.

### 2. Client & Collaborative Engineering
- **[Advfiction LMS & AI Automation](advfiction.html):** Enterprise LMS portal and automation workflows built with React 19, Next.js, and Supabase during a 22-week commercial internship.
- **[Awarewolf Media Ingestion Pipeline](awarewolf.html):** Production remediation of high-throughput media ingestion and batch metadata workflows.
- **[AlgoDevOpss Portal](algodevopss.html):** Academic and developer resource management platform for institutional engineering coursework.
- **[Client Work Index](client-work.html):** Directory of client and institutional engineering deliverables.

### 3. AI & Workflow Automation
- **[n8n Workflow Automation Hub](automation.html):** 10 n8n workflow architectures presented in canonical sequence (WF-01 through WF-10), covering lead intelligence, social distribution, multi-agent routing, and CRM synchronization, with verified editor execution evidence for Apify Maps scraper (#wf-maps-scraper).

---

## 📚 Maintainer Documentation Suite

Complete developer documentation is located in the [`docs/`](docs/) directory:

- 🏗️ **[docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)** — In-depth technical architecture, CSS token design system, and client-side JavaScript specs.
- 📝 **[docs/CONTENT_GUIDE.md](docs/CONTENT_GUIDE.md)** — Schemas and guidelines for adding projects, credentials, and work experiences.
- 🚀 **[docs/RELEASE_GUIDE.md](docs/RELEASE_GUIDE.md)** — Quality gates, automated test execution, and Git branch policies.
- 🔒 **[docs/PRIVACY_RULES.md](docs/PRIVACY_RULES.md)** — Privacy firewall rules, PII redaction pipeline, and credential storage policies.

---

## 🛠️ Build, Test & Local Preview

The site requires only Python 3.10+ standard library:

```powershell
# 1. Regenerate all 17 HTML routes
python build_site.py

# 2. Run automated structural and link verification suite
python check_site.py

# 3. Run regression unit test suite
python -m pytest tests/

# 4. Validate W3C HTML5 compliance across all 17 routes
npx html-validate *.html

# 5. Run Python linter & security scans
python -m ruff check build_site.py check_site.py tests/
python -m bandit -r build_site.py check_site.py tests/ -ll -q

# 6. Validate JavaScript syntax
node --check site.js

# 7. Preview locally
python -m http.server 8765 --bind 127.0.0.1
# Open http://127.0.0.1:8765 in your browser
```

---

## 📄 Verified Evidence & Document Traceability

All 48 credentials, certifications, and academic records displayed across the portfolio are cataloged with end-to-end traceability:
- **Cloud Certificates:** Backed by authenticated Google Drive links with public anonymous viewer access.
- **IIRS / ISRO Outreach:** Public-safe derivatives located in `assets/documents/iirs-outreach/` with personal identifiers stripped for privacy.
- **Central Storage Inventory:** Master ledger maintained in Central Portfolio HQ (`D:\_Rehan_Antigravity_HQ\PORTFOLIO_CENTRAL\`).
