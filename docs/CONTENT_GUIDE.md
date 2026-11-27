# Content & Data Guide for Maintainers

Authoritative schemas and rules for maintaining data in `build_site.py`.

---

## 1. Adding or Modifying a Project (`PROJECTS`)

Projects live in the `PROJECTS` list in `build_site.py`:

```python
{
    "name": "Project Display Name",
    "pillar": "AI & Machine Learning Systems",  # One of 3 exact pillars
    "category": "Sub-Category · Architecture Focus",
    "status": "Prototype / Active development / Live deployment",
    "summary": "Concise factual overview of architecture and scope.",
    "route": "project-slug.html",              # Route or anchor (e.g. client-work.html#id)
    "repo": "https://github.com/...",           # Verified public repo or ""
    "live": "https://...",                      # Verified live deployment or ""
    "evidence": "page.html#anchor",            # Optional secondary evidence link
    "evidence_label": "Test Evidence →",        # Optional custom label (default: "Workflow Canvas →")
    "highlight": "Recruiter takeaway grounded in inspected source/test outputs.",
    "tags": ["Python", "FastAPI", "PostgreSQL"],
}
```

### Required Consistency Updates
- Pillar allocation is currently enforced in `check_site.py` (`EXPECTED_PILLARS`) and `tests/test_portfolio.py` (`5 / 5 / 4` = `14` total projects). Update those checks only if intentionally changing pillar counts.
- `sitemap.xml` and `robots.txt` are generated automatically by `build_site.py` from `PAGES` (no manual XML edits needed).

---

## 2. Adding a Credential (`CREDENTIALS`)

Credentials are registered in `CREDENTIALS` in `build_site.py`:

```python
{
    "title": "Exact Certificate / Record Title",
    "issuer": "Issuing Organization",
    "date": "15 Sep 2025",
    "kind": "Course Certification",
    "subject": "Generative AI",
    "domain": "generative ai & automation",  # Must match one of the 6 filter pills below
    "tags": ["GenAI", "Certification"],
    "detail": "Factual summary matching the inspected certificate.",
    "status": "Verified Credential",
    "drive_id": "...",      # Optional: public read-only Drive file ID
    "public_pdf": "...",    # Optional: local redacted PDF path (set automatically for IIRS)
    "verify_url": "...",    # Optional: third-party issuer verification URL
}
```

### Valid `domain` Values (`credentials.html` filter pills)
- `geospatial & remote sensing`
- `ai, ml & data science`
- `generative ai & automation`
- `software engineering`
- `professional development`
- `academic & extension honors`

### Storage & Traceability Rules
1. Keep any public Google Drive links file-level `anyone/reader` only; never expose withheld/confidential file IDs.
2. Link IIRS/ISRO records via privacy-safe copies in `assets/documents/iirs-outreach/` (`IIRS_PUBLIC_KEYS`).
3. `#credentialType` and `#credentialSubject` `<select>` options are generated dynamically from `CREDENTIALS` and verified by `check_site.py`. If intentionally changing record count (`48`), update `check_site.py` and `tests/test_portfolio.py`.

---

## 3. Adding an Experience Entry (`EXPERIENCE`)

Commercial/team experience cards live in `EXPERIENCE` in `build_site.py`:

```python
{
    "name": "Organization Name",
    "role": "Role Title · Employment Type",
    "dates": "May–Oct 2026 · 22 Weeks",
    "badge": "Commercial Internship",
    "status_note": "Optional concise engagement status",
    "summary": "First-person singular summary of verified deliverables.",
    "route": "org-page.html",
}
```

- Document proof buttons in `experience_card()` map explicitly by `item["name"]` to verified public Drive links.

---

## 4. Canonical n8n Workflow Order (`automation.html`)

The sequence `#wf-instagram-api` through `#wf-telegram-bot` is strictly enforced by `check_site.py`:
1. `WF-01`: Instagram Scheduled Publishing — `#wf-instagram-api`
2. `WF-02`: News Sources to AI Summary — `#wf-news-prompt`
3. `WF-03`: PostgreSQL to AI Social Publisher — `#wf-social-publisher`
4. `WF-04`: AI Outreach & Team Notification — `#wf-subworkflow-router`
5. `WF-05`: Caption to Image Asset — `#wf-social-orchestrator`
6. `WF-06`: AI Itinerary & PDF Proposal — `#wf-itinerary-proposal`
7. `WF-07`: Apify Maps to Google Sheets — `#wf-maps-scraper`
8. `WF-08`: Lead Row to PDF Brief — `#wf-lead-dossier`
9. `WF-09`: PostgreSQL Search & AI Enrichment — `#wf-postgres-research`
10. `WF-10`: Telegram Review & Approval — `#wf-telegram-bot`
