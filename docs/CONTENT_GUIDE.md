# Content & Data Guide for Maintainers

This guide provides schemas, conventions, and procedures for updating content across the portfolio using `build_site.py`.

---

## 1. Adding or Modifying a Flagship Project

Projects are defined in the `PROJECTS` list in `build_site.py`:

```python
{
    "name": "Project Display Name",
    "pillar": "AI & Machine Learning Systems",  # One of 4 core pillars
    "category": "Sub-Category · Architecture Focus",
    "status": "Production · Live / Active development",
    "summary": "Concise 2-3 sentence overview of the architecture, stack, and outcomes.",
    "route": "project-slug.html",              # Dedicated page or anchor link
    "repo": "https://github.com/...",           # Public GitHub repository URL
    "live": "https://...",                      # Deployed live demo (or empty string)
    "highlight": "Recruiter takeaway summarizing engineering depth or test coverage.",
    "tags": ["FastAPI", "Python", "PostgreSQL", "React 19"],
}
```

### Content Conventions for Projects
- **Truthful Status:** Always specify if a project is in active development, a prototype, or deployed to production.
- **Accurate Test Accounting:** Explicitly cite the test harness (e.g. `97 pytest unit tests, 21 frontend vitest tests`). Never inflate numbers.
- **Dedicated Route:** If adding a new deep-dive page, declare its route in `PAGES` dictionary and add it to `sitemap.xml` entries.

---

## 2. Adding a Credential or Certificate

Credentials are registered in `CREDENTIALS` list in `build_site.py`:

```python
{
    "title": "Full Name of Certificate / Course",
    "issuer": "Issuing Organization or Platform",
    "date": "15 Sep 2025",
    "kind": "Commercial Internship Certificate / Skill Assessment / Course Certification",
    "subject": "Generative AI / Computer Vision / Full-Stack",
    "domain": "AI, ML & Data Science / Web Development / Governance",
    "tags": ["GenAI", "Prompt Engineering"],
    "detail": "Description of curriculum, projects completed, and hours invested.",
    "status": "Verified Credential",
    "drive_id": "1VZPcWKt4f5I_vRD8REPQYADvNDZ_WsIL",  # For Drive-backed credentials
    "verify_url": "",                                  # For Coursera/external links
}
```

### Storage and Privacy Rules for Credentials:
1. **Google Drive Credentials:**
   - Must have file-level viewer access: `gdrive mutate share <file_id> --type anyone --role reader`.
   - Never share parent folders publicly.
2. **IIRS/ISRO Outreach Copies:**
   - Never link original documents with candidate registration numbers or serial numbers.
   - Use public-safe derivatives located in `assets/documents/iirs-outreach/`.
3. **Traceability:**
   - Record every new credential in `D:\_Rehan_Antigravity_HQ\PORTFOLIO_CENTRAL\CREDENTIAL_LINK_TRACEABILITY.csv`.

---

## 3. Adding an Internship or Work Experience

Experiences are declared in `EXPERIENCES` in `build_site.py`:

```python
{
    "role": "Job Title",
    "company": "Company Name",
    "period": "Jun 2025 – Present",
    "location": "Mumbai, India (Remote / Hybrid)",
    "description": "High-level summary of responsibilities and technical domain.",
    "points": [
        "First-person singular action verb bullet point detailing engineering accomplishments.",
        "Include metrics, tools, and technical outcomes.",
    ],
    "skills": ["Python", "FastAPI", "Docker", "n8n"],
    "certificate_link": "https://drive.google.com/...",  # Optional verified completion link
}
```

### Style Rules for Work Experience:
- **Active First-Person Singular:** Use "Engineered", "Designed", "Architected", "Implemented", "Refactored".
- **Omit Internal Personnel:** Do not mention collaborator names, internal team conflicts, or apologetic qualifiers.

---

## 4. Canonical n8n Workflow Order (`automation.html`)

The sequence of the 10 n8n workflows in `automation.html` is fixed and must be maintained:
1. `WF-01`: Multi-Source Technical Intelligence Dispatcher
2. `WF-02`: Real-Time Autonomous Market Lead Ingestion & Qualification
3. `WF-03`: Webhook-Driven Incident Alert & Triage Pipeline
4. `WF-04`: Multi-Agent Autonomous Code Review & CI Triage
5. `WF-05`: Cross-Platform Social Intelligence & Automated Syndication
6. `WF-06`: Automated Invoice Processing & Financial Ledger Reconciliation
7. `WF-07`: Autonomous Candidate Ingestion & Resume Parsing Pipeline
8. `WF-08`: Enterprise Knowledge Graph Synchronization & RAG Pipeline
9. `WF-09`: Automated Customer Feedback Sentiment Analysis & CRM Escalation
10. `WF-10`: Autonomous Multi-Channel Content Repurposing & Publishing Engine
