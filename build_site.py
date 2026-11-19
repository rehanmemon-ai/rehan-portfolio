"""Render the static portfolio pages from reviewed, evidence-backed content. Dependency-free."""

from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent
GITHUB = "https://github.com/rehanmemon-ai"
SIGNATURE = f"{GITHUB}/signature-verification"
RESEARCH = f"{GITHUB}/Assistant_Bot-Research"
# These projects are local work in progress; public repository destinations are unverified.
CONNECT_HUB = ""
JOB_SEARCH = ""
EMAIL = "memon18rehan@gmail.com"
LINKEDIN = "https://www.linkedin.com/in/rehan-memon-b1803b334"
LEETCODE = "https://leetcode.com/u/rehanmemon-ai/"
KAGGLE = "https://www.kaggle.com/rehanjunedmemon"
RESUME_DOC_ID = "1aXDe4hqYjGSrUSUdmjhXPUbHVSO_6Em_5VP4u_72Kfg"
RESUME_URL = f"https://docs.google.com/document/d/{RESUME_DOC_ID}/edit"
RESUME_PDF_URL = f"https://docs.google.com/document/d/{RESUME_DOC_ID}/export?format=pdf"
SITE_URL = "https://rehanmemon-ai.github.io/rehan-portfolio"

# Official College Affiliation & Identity
COLLEGE_NAME_FULL = "Vivekanand Education Society’s College of Arts, Science & Commerce (Autonomous)"
COLLEGE_NAME_SHORT = "VESASC (Autonomous)"
COLLEGE_URL = "https://ves.ac.in/vesasc/"
AI_DEPT_URL = "https://ves.ac.in/vesasc/department-of-ai/"
DEGREE_NAME = "B.Sc. in Artificial Intelligence"


def link(href, label, css="text-link", external=False):
    extra = ' target="_blank" rel="noopener noreferrer"' if external else ""
    return f'<a class="{css}" href="{escape(href, quote=True)}"{extra}>{escape(label)}</a>'


def eyebrow(label):
    return f'<p class="eyebrow">{escape(label)}</p>'


def badge(text, kind="status"):
    css_class = "badge badge-status" if kind == "status" else "badge badge-pillar"
    return f'<span class="{css_class}">{escape(text)}</span>'


def breadcrumb(href, label):
    return f'<nav class="breadcrumb" aria-label="Breadcrumb"><a href="{escape(href, quote=True)}">← Back to {escape(label)}</a></nav>'


def intro(label, title, summary, back_href="", back_label="", css_class=""):
    back_html = breadcrumb(back_href, back_label) if back_href and back_label else ""
    classes = f"page-intro container {css_class}".strip()
    return f'<section class="{classes}">{back_html}{eyebrow(label)}<h1>{escape(title)}</h1><p class="lead">{escape(summary)}</p></section>'


def section(title, body, sid="", extra_attrs=""):
    ident = f' id="{sid}"' if sid else ""
    extra = f' {extra_attrs}' if extra_attrs else ""
    return f'<section class="section container"{ident}{extra}><h2>{escape(title)}</h2>{body}</section>'


def case_row(step, text):
    return f'<li><div class="flow-step-num">{escape(step)}</div><div class="flow-step-body">{text}</div></li>'


def explore_more(current=""):
    items = [
        ("projects.html", "Technical Projects →", "Computer Vision, RAG & Full-Stack Systems"),
        ("experience.html", "Internship Experience →", "AwareWolf, Advfiction & AlgoDevOpss"),
        ("automation.html", "AI & Workflow Automation →", "10 n8n workflow architectures with execution evidence"),
        ("client-work.html", "Client Deployments →", "LMS, Corporate Portals & Web APIs"),
        ("credentials.html", "Credential Library →", "ISRO, Nasscom, PW Skills & Academic Certs"),
        ("contact.html", "Get In Touch →", "Direct Email, LinkedIn & GitHub"),
    ]
    selected = [item for item in items if item[0] != current][:4]
    grid_html = "".join(
        f'<a href="{href}" class="explore-link">'
        f'<span class="explore-title">{escape(title)}</span>'
        f'<span class="explore-desc">{escape(desc)}</span>'
        f'</a>'
        for href, title, desc in selected
    )
    return (
        f'<nav class="explore-more-nav container" aria-label="Explore Portfolio">'
        f'<div class="explore-more-card">'
        f'<p class="eyebrow">Continue Exploring</p>'
        f'<div class="explore-grid">{grid_html}</div>'
        f'</div>'
        f'</nav>'
    )


# Comprehensive Project Portfolio across Three Core Pillars
PROJECTS = [
    # PILLAR 1: AI & Machine Learning Systems
    {
        "name": "ConnectHub — Real-Time AI Messaging Engine",
        "pillar": "AI & Machine Learning Systems",
        "category": "Real-Time Messaging · AI Summarization",
        "status": "Deployed demo & active development",
        "summary": "Full-stack messaging application using FastAPI, async SQLAlchemy, Psycopg, and PostgreSQL. Implements WebSocket messaging, typing indicators, read receipts, in-memory presence, Gemini-assisted room summaries, and room-scoped semantic search using JSONB embeddings and Python cosine similarity.",
        "route": "connecthub.html",
        "repo": CONNECT_HUB,
        "live": "https://connecthub-web-w89e.onrender.com",
        "highlight": "Single-process WebSocket service with PostgreSQL persistence, room summaries, and live Render deployment. Verified by 97 backend tests, 21 frontend tests, and 3 Playwright E2E scenarios.",
        "tags": ["FastAPI", "Python", "SQLAlchemy 2.1", "PostgreSQL", "WebSockets", "Google Gemini API", "React 19", "TypeScript"],
    },
    {
        "name": "Signature Verification AI",
        "pillar": "AI & Machine Learning Systems",
        "category": "Computer Vision · Machine Learning",
        "status": "Working prototype",
        "summary": "Offline signature verification prototype using grayscale conversion, Gaussian blur, Otsu thresholding, contour crop, 331 handcrafted features, StandardScaler and an RBF SVM evaluated with writer-disjoint splits.",
        "route": "signature-verification.html",
        "repo": SIGNATURE,
        "live": "",
        "highlight": "Extracts 331 handcrafted features (Hu moments, projection profiles, ink density) with FastAPI and React demo interface.",
        "tags": ["Python", "OpenCV", "Scikit-Learn", "SVM", "FastAPI", "React"],
    },
    {
        "name": "AI Research Assistant",
        "pillar": "AI & Machine Learning Systems",
        "category": "Generative AI · Retrieval-Augmented Generation",
        "status": "Currently developing",
        "summary": "Document question-answering prototype featuring token-aware text chunking, dense Chroma vector database indexing, workspace-scoped similarity retrieval, transparent source citation mapping, and a local FastAPI service harness.",
        "route": "ai-research-assistant.html",
        "repo": RESEARCH,
        "live": "",
        "highlight": "Modular Python ingestion prototype with Chroma dense embeddings, workspace-scoped retrieval, and source citation mapping.",
        "tags": ["Python", "ChromaDB", "Vector Search", "FastAPI", "RAG", "Embeddings"],
    },
    {
        "name": "KARIGAR-SETU — Artisan Smart Cataloging",
        "pillar": "AI & Machine Learning Systems",
        "category": "Multimodal AI · On-Device Vision",
        "status": "Design-stage architecture",
        "summary": "Team design for an artisan cataloging and market-linkage app (Problem Statement SIH26090). The proposal considers MobileNet/TensorFlow.js, Gemini-generated descriptions, and Web Speech API voice interaction; implementation of those components has not been established.",
        "route": "activities.html#karigar-setu",
        "repo": "",
        "live": "",
        "highlight": "Design-stage team architecture for product imagery, catalog text, and multilingual interaction.",
        "tags": ["Design Stage", "TensorFlow.js Proposal", "MobileNet Proposal", "Gemini Proposal", "Voice UI Proposal"],
    },
    {
        "name": "National Scholarship Portal AI Assistant",
        "pillar": "AI & Machine Learning Systems",
        "category": "Conversational AI · Hackathon Proposal",
        "status": "College-round entry",
        "summary": "Team DBTDecoders proposed a National Scholarship Portal (NSP / DBT scheme) conversational assistant and received a documented college-round recognition and Principal nomination for SIH 2025. The available deck describes intended eligibility guidance; chatbot implementation has not been independently verified.",
        "route": "activities.html#sih-dbtdecoders",
        "repo": "",
        "live": "",
        "highlight": "College-round recognition and Principal nomination; public technical implementation evidence remains limited.",
        "tags": ["Conversational AI", "Hackathon Proposal", "SIH 2025", "NSP DBT"],
    },

    # PILLAR 2: Client & Collaborative Engineering
    {
        "name": "SAHASH NGO Voice & Conversational Assistant",
        "pillar": "Client & Collaborative Engineering",
        "category": "Conversational AI · NGO Community Support",
        "status": "Prototype; deployment unverified",
        "summary": "Conversational assistant developed for SAHASH India via ConnectFor to help visitors find organization information. The Node.js/Express service retrieves FAQ and organization documents using keyword and intent scoring, passes context to Gemini, and supports session history and a Web Speech API voice interface.",
        "route": "client-work.html#sahash-chatbot",
        "repo": "",
        "live": "",
        "highlight": "Voice-enabled interface with local FAQ/document lookup and Gemini response generation; factual answer faithfulness has not been measured.",
        "tags": ["Node.js", "Express", "Google Gemini API", "Keyword Retrieval", "Web Speech API", "Voice UI"],
    },
    {
        "name": "Advfiction Enterprise Lead LMS",
        "pillar": "Client & Collaborative Engineering",
        "category": "Full-Stack Web & API Engineering",
        "status": "Live deployment",
        "summary": "Collaborative lead management system for marketing operations. Contributed a public Node/Express lead endpoint with required-field and email checks, Supabase PostgreSQL insertion, and an allowed-origin CORS configuration for the website and LMS frontends.",
        "route": "client-work.html#advfiction-lms",
        "repo": "",
        "live": "https://advfiction-lms.vercel.app/pages/login.html",
        "highlight": "Public Vercel frontend and Render API are linked; live lead submission and database persistence were not independently tested for this portfolio.",
        "tags": ["Node.js", "Express", "Supabase", "PostgreSQL", "REST API", "Vercel"],
    },
    {
        "name": "LMS Girls Higher Secondary School",
        "pillar": "Client & Collaborative Engineering",
        "category": "Full-Stack Portal · Next.js 16 & Supabase SSR",
        "status": "Live deployment",
        "summary": "Institutional school website and administrative portal built with Next.js 16.2.6, React 19.2.4, TypeScript, Tailwind CSS, and Supabase. Engineered administrative content management modules for news, events, faculty rosters, photo galleries, and achievements, with server-side Supabase data queries.",
        "route": "client-work.html#girls-hss",
        "repo": "",
        "live": "https://girlshss.netlify.app/",
        "highlight": "Architected administrative content management suite and Supabase SSR integration on Next.js 16 App Router.",
        "tags": ["Next.js 16", "React 19", "TypeScript", "Tailwind CSS", "Supabase", "REST API"],
    },
    {
        "name": "Marthandam Star Honey Platform",
        "pillar": "Client & Collaborative Engineering",
        "category": "E-Commerce Showcase & API Integration",
        "status": "Live deployment",
        "summary": "Commercial product showcase built with React 19, Vite, Tailwind CSS, and Framer Motion. A separate Express-to-Google-Sheets inquiry integration exists in the local source; the deployed form's submission path is not independently verified.",
        "route": "client-work.html#msh-honey",
        "repo": "",
        "live": "https://msh-website.netlify.app/",
        "highlight": "Live product showcase; end-to-end inquiry delivery remains unverified.",
        "tags": ["React 19", "Vite", "Tailwind CSS", "Express", "Google Sheets API"],
    },
    {
        "name": "Advfiction Corporate Website Revamp",
        "pillar": "Client & Collaborative Engineering",
        "category": "Collaborative Web Engineering",
        "status": "Live deployment",
        "summary": "Revamp of the primary corporate web presence for Advfiction Private Limited. Implemented responsive interface layouts, interactive service presentations, and contact form integrations routing inquiries directly to the company's backend lead pipeline.",
        "route": "client-work.html#advfiction-website",
        "repo": "",
        "live": "https://advfiction.vercel.app/",
        "highlight": "Live company website featuring mobile-responsive UI and connected contact intake.",
        "tags": ["JavaScript", "HTML5/CSS3", "API Integration", "Vercel"],
    },

    # PILLAR 3: AI & Workflow Automation Systems
    {
        "name": "Autonomous Job Search Engine",
        "pillar": "AI & Workflow Automation",
        "category": "Local-First Automation · Public ATS Ingestion",
        "status": "Active development",
        "summary": "Local-first job discovery prototype with Python adapters for Greenhouse, Lever, Ashby, Himalayas, Remotive, and Arbeitnow, plus a Schema.org structured-data parser. Adzuna remains a stub. Streamlit supports review and deterministic matching; a PREPARATION_ONLY hard lock prevents external application submission.",
        "route": "job-search-automation.html",
        "repo": JOB_SEARCH,
        "live": "",
        "evidence": "job-search-automation.html#verification",
        "highlight": "Local-first ingestion and deterministic matching with a preparation-only safety boundary. A current offline suite run passed 450 tests, failed one scoring E2E assertion, and skipped one Windows symlink test.",
        "tags": ["Python", "Streamlit", "Greenhouse API", "Lever API", "Deterministic Matching", "Pytest"],
    },
    {
        "name": "Apify-to-Sheets Lead Pipeline",
        "pillar": "AI & Workflow Automation",
        "category": "Map Data Ingestion",
        "status": "Editor execution shown",
        "summary": "An n8n canvas connects an Apify map scraper to dataset retrieval, a filter, and Google Sheets row insertion. The published editor capture shows five items at the final append node.",
        "route": "automation.html#wf-maps-scraper",
        "repo": "",
        "live": "",
        "evidence": "automation.html#wf-maps-scraper",
        "highlight": "One small editor run is visible; ongoing deployment and larger-scale output are not established.",
        "tags": ["n8n", "Apify Actors", "Google Sheets API", "Data Filtering", "ETL"],
    },
    {
        "name": "Company Research & AI Enrichment Canvas",
        "pillar": "AI & Workflow Automation",
        "category": "Database Research Canvas",
        "status": "Partial execution shown",
        "summary": "A PostgreSQL research canvas fetches rows, batches them, checks prior processing and routes search results toward an AI request and database save step.",
        "route": "automation.html#wf-postgres-research",
        "repo": "",
        "live": "",
        "evidence": "automation.html#wf-postgres-research",
        "highlight": "Early nodes completed in the editor; the AI request shows a warning and the save step is not shown completing.",
        "tags": ["n8n", "PostgreSQL", "AI Prompts", "SerpApi", "Batch Processing"],
    },
    {
        "name": "Lead Brief & PDF Workflow Design",
        "pillar": "AI & Workflow Automation",
        "category": "Document Automation Design",
        "status": "Design-stage architecture",
        "summary": "Two n8n canvas views show a sheet-triggered lead brief: format fields, create a Google Doc, export a PDF and route a Gmail notification. A later view adds a filter.",
        "route": "automation.html#wf-lead-dossier",
        "repo": "",
        "live": "",
        "evidence": "automation.html#wf-lead-dossier",
        "highlight": "The captures show design/configuration, without a completed PDF or delivered email.",
        "tags": ["n8n", "Google Sheets", "Google Docs", "PDF Export", "Gmail"],
    },
]



def get_project(name):
    for p in PROJECTS:
        if p["name"] == name:
            return p
    raise ValueError(f"Project not found: {name}")


# Experience Chronology - Ordered: AwareWolf (1st), Advfiction (2nd), AlgoDevOpss (3rd)
EXPERIENCE = [
    {
        "name": "AwareWolf",
        "role": "Content Operating System Intern",
        "badge": "PAID INTERNSHIP",
        "dates": "Offer Term: Sep 2026–Mar 2027",
        "status_note": "Paid Internship · Workstream paused in November 2026",
        "summary": "Engineered media workflow prototyping in React/TypeScript and FastAPI: built five-scene JSONL storyboards (263 backend / 27 frontend tests passing in verified local snapshot), engineered Pillow/SHA-256 image ingestion (7 integration tests), investigated legacy FFmpeg stream drift, and benchmarked generative-video models on Kaggle.",
        "route": "awarewolf.html",
    },
    {
        "name": "Advfiction Private Limited",
        "role": "Web Developer Intern & AI Automation Developer (Dual Track)",
        "badge": "DUAL TRACK VERIFIED",
        "dates": "Apr–Sep 2026 · Extended 22-Week Appointment",
        "status_note": "Both tracks extended by 2 additional months · 22-week completion certs & joint LOR verified",
        "summary": "Operated across two concurrent engineering workstreams: built full-stack lead intake APIs (Node/Express, Supabase) and responsive interfaces on the web team, while architecting multi-stage n8n workflows for automated lead capture, PostgreSQL research, and document generation. Both tracks verified by primary offer letters, extension letters, completion certificates, and a joint Letter of Recommendation.",
        "route": "advfiction.html",
    },
    {
        "name": "AlgoDevOpss",
        "role": "Full-Stack Development Intern",
        "badge": "DOCUMENTED TERM",
        "dates": "May–Aug 2026 · Documented Term (Extension Pending)",
        "status_note": "Documented appointment: May–Aug 2026; informal extension through Dec 2026 (in progress as of November 2026; formal letter pending)",
        "summary": "Collaborated on departmental web modules for the KJSIEIT EXTC website in Next.js and TypeScript, engineering the dedicated Pedagogy showcase route and the typed results-data.ts performance module, alongside database-backed CMS prototyping.",
        "route": "algodevopss.html",
    },
]

# Full Curated Credential Records across 6 Domains
CREDENTIALS = [

    # Domain: Generative AI & Automation
    {
        "title": "GenAI Job Simulation",
        "issuer": "BCG X via Forage",
        "date": "15 Sep 2025",
        "kind": "Enterprise Simulation",
        "subject": "Generative AI",
        "domain": "Generative AI & Automation",
        "tags": ["Generative AI", "Python", "LLMs", "RAG", "Data Extraction"],
        "detail": "BCG X GenAI job simulation completed through Forage. This is a training simulation, not direct BCG X employment.",
        "status": "Verified Simulation",
        "drive_id": "1VZPcWKt4f5I_vRD8REPQYADvNDZ_WsIL",
    },
    {
        "title": "AI Automation Developer Internship Certificate",
        "issuer": "Advfiction Private Limited",
        "date": "01 Oct 2026",
        "kind": "Commercial Internship Certificate",
        "subject": "AI & Automation",
        "domain": "Generative AI & Automation",
        "tags": ["AI Automation", "n8n", "Apify", "Workflows", "PostgreSQL"],
        "detail": "Verified 22-week commercial internship completion certificate across AI workflow engineering, automated scraping pipelines, and multi-stage n8n integrations, signed by Managing Director Rojer R V.",
        "status": "Verified Commercial Credential",
        "drive_id": "1T_3ZDXAFRpxJ6-GDZAkyCPVchJdR7815",
    },
    {
        "title": "5-Day AI & Computer Vision Bootcamp: Face Tracking with Cursor.AI",
        "issuer": "SmartEd Innovations / Tech Partner",
        "date": "19 Jun 2025",
        "kind": "Hands-on Bootcamp",
        "subject": "Computer Vision",
        "domain": "Generative AI & Automation",
        "tags": ["Computer Vision", "Face Tracking", "Cursor.AI", "JavaScript"],
        "detail": "Certificate of attendance and active participation in a five-day bootcamp on building web-based face tracking with Cursor.AI; individual implementation is not established by the certificate.",
        "status": "Verified Credential",
        "drive_id": "1-LhAUvxdgmSkQXRnxU5B1QlfKnNHK_LW",
    },

    # Domain: AI, ML & Data Science
    {
        "title": "Application of AI/ML Model for Specific Crop Acreage Mapping — Workshop",
        "issuer": "IIRS / ISRO Outreach",
        "date": "29 May 2025",
        "kind": "Workshop Participation",
        "subject": "AI / ML",
        "domain": "AI, ML & Data Science",
        "tags": ["AI/ML", "Crop Acreage Mapping", "IIRS Workshop"],
        "detail": "Workshop conducted: 2 April 2025 · Certificate issued: 29 May 2025. One-day online workshop on specific crop acreage mapping; privacy-safe public copy is linked.",
        "status": "Participation confirmed",
        "drive_id": "",
    },
    {
        "title": "Machine Learning and Image Processing",
        "issuer": "thingQbator / Nasscom Foundation (Zikshaa training partner)",
        "date": "Academic Year 2024\u20132025",
        "kind": "Certificate of Excellence",
        "subject": "AI / ML",
        "domain": "AI, ML & Data Science",
        "tags": ["Machine Learning", "Image Processing", "OpenCV", "Scikit-Learn"],
        "detail": "Certificate of Excellence for completing the Machine Learning and Image Processing program; the document does not verify each individual technique listed in a curriculum.",
        "status": "Verified Credential",
        "drive_id": "1SmZrm_eHCRN9N_AQEsoNjetVF1_0NfNu",
    },
    {
        "title": "Data Science Career Track Masterclass",
        "issuer": "PW Skills (PhysicsWallah)",
        "date": "10 Nov 2024",
        "kind": "Technical Masterclass",
        "subject": "Data Science",
        "domain": "AI, ML & Data Science",
        "tags": ["Data Science", "Python", "Pandas", "EDA", "Statistical Modeling"],
        "detail": "Participation in a PW Skills data science career-track masterclass; the certificate does not document practical project outcomes.",
        "status": "Verified Credential",
        "drive_id": "1ySPaVCsj16lXjWuWlykIet3BGYmspFxZ",
    },
    {
        "title": "Artificial Intelligence Beginner Skill Certification",
        "issuer": "Guru Skill Assessment",
        "date": "03 Jun 2025",
        "kind": "Skill Assessment",
        "subject": "AI / ML",
        "domain": "AI, ML & Data Science",
        "tags": ["AI Fundamentals", "Knowledge Representation", "Search Algorithms"],
        "detail": "Guru beginner-level Artificial Intelligence skill test certificate, issued 3 June 2025; it does not specify the individual topics assessed.",
        "status": "Verified Credential",
        "drive_id": "1U35ipX3-BdCIUFcU4O92I11Ghy7ZT5oq",
    },
    {
        "title": "Machine learning for Healthcare by MIT (on Cursa)",
        "issuer": "Cursa Educational Platform",
        "date": "Academic Year 2024\u20132025",
        "kind": "Course Certification",
        "subject": "AI / ML",
        "domain": "AI, ML & Data Science",
        "tags": ["Machine Learning", "Healthcare Analytics", "Predictive Modeling"],
        "detail": "Cursa course certificate for a course labelled as MIT material; MIT is not the credential issuer.",
        "status": "Verified Credential",
        "drive_id": "1Sx8qfEb64mIzZoclOfvfgZsaSeHj4E9E",
    },
    {
        "title": "Fundamentals of Artificial Intelligence by NPTEL (on Cursa)",
        "issuer": "Cursa Educational Platform",
        "date": "Academic Year 2024\u20132025",
        "kind": "Course Certification",
        "subject": "AI / ML",
        "domain": "AI, ML & Data Science",
        "tags": ["AI Concepts", "Neural Networks", "NLP Basics", "Computer Vision"],
        "detail": "Cursa course certificate for a course labelled as NPTEL material; NPTEL is not the credential issuer.",
        "status": "Verified Credential",
        "drive_id": "1_C0hkI5_jqNVMKQaAsgik5oSqtHqmhb8",
    },
    {
        "title": "AI/ML Automation Using Python & ChatGPT",
        "issuer": "LCM",
        "date": "07 Jun 2025",
        "kind": "Workshop Participation",
        "subject": "AI / ML",
        "domain": "AI, ML & Data Science",
        "tags": ["Artificial Intelligence", "Machine Learning", "Python", "Algorithms"],
        "detail": "Workshop participation, as stated on the original LCM certificate. The document does not establish assessed proficiency.",
        "status": "Verified Credential",
        "drive_id": "1vSQ93mfl7I1jfTa16_zPKV1xN8_Sas2k",
    },
    {
        "title": "Artificial Intelligence & Deep Learning Workshop",
        "issuer": "FirstBit Solutions",
        "date": "19 Jul 2025",
        "kind": "Technical Workshop",
        "subject": "AI / ML",
        "domain": "AI, ML & Data Science",
        "tags": ["Deep Learning", "Neural Networks", "AI Workshop", "FirstBit Solutions"],
        "detail": "Participation in FirstBit Solutions' AI & Deep Learning workshop conducted 19 July 2025; the certificate does not document an implementation project.",
        "status": "Verified Credential",
        "drive_id": "1aLkavLeWI0aLzu42KX9ehcM27Tppe27T",
    },

    # Domain: Software Engineering
    {
        "title": "Full-Stack Web Development Internship Certification",
        "issuer": "AlgoDevOpss",
        "date": "31 Aug 2026",
        "kind": "Internship Credential",
        "subject": "Web Development",
        "domain": "Software Engineering",
        "tags": ["Next.js", "TypeScript", "React", "Full-Stack Web", "API Design"],
        "detail": "AlgoDevOpss certificate confirms a Full-Stack Development Intern term from 1 May to 31 August 2026 and contributions across MERN, Next.js, PHP and machine-learning projects; individual code contributions require repository evidence.",
        "status": "Primary Document Verified",
        "drive_id": "1yZyBwiDStZatvvD9oj5rlM1WUTBkz9BV",
    },
    {
        "title": "Building E-Commerce Applications with React",
        "issuer": "PW Skills (PhysicsWallah)",
        "date": "23 Nov 2024",
        "kind": "Technical Masterclass",
        "subject": "Frontend Engineering",
        "domain": "Software Engineering",
        "tags": ["React", "JavaScript", "State Management", "Component Architecture"],
        "detail": "Participation in a PW Skills masterclass about building e-commerce applications with React; an implemented application is not established by the certificate.",
        "status": "Verified Credential",
        "drive_id": "1rOWubhh80jgrXJtHXP2ArUu2QnBwcqXA",
    },
    {
        "title": "Web Development Internship Completion Certificate",
        "issuer": "Advfiction Private Limited",
        "date": "01 Oct 2026",
        "kind": "Commercial Internship Certificate",
        "subject": "Software Engineering",
        "domain": "Software Engineering",
        "tags": ["Full-Stack", "Node.js", "Express", "Supabase", "REST API", "Vercel"],
        "detail": "Verified 22-week commercial internship completion certificate for full-stack API engineering, Enterprise LMS development, and corporate platform revamps, signed by Managing Director Rojer R V.",
        "status": "Verified Commercial Credential",
        "drive_id": "1Q_zS8HQjH03CE4nwsZyvVjkP3t1EI6hn",
    },
    {
        "title": "Data Structures & Algorithms with C++",
        "issuer": "SmartEd Innovations / USNG Learnspace Edtech",
        "date": "10 Jul 2025",
        "kind": "Technical Bootcamp",
        "subject": "Programming",
        "domain": "Software Engineering",
        "tags": ["C++", "DSA", "Algorithms", "Time Complexity", "Memory Management"],
        "detail": "Data Structures and Algorithms with C++ bootcamp credential; the document does not verify particular algorithms implemented.",
        "status": "Verified Credential",
        "drive_id": "1sNljgYyn666CdnDucWRL0i__hq5DWQ9W",
    },
    {
        "title": "Python for complete beginners by Corey Schafer (on Cursa)",
        "issuer": "Cursa Educational Platform",
        "date": "Academic Year 2024\u20132025",
        "kind": "Course Certification",
        "subject": "Programming",
        "domain": "Software Engineering",
        "tags": ["Python 3", "OOP", "Decorators", "File I/O", "Data Structures"],
        "detail": "Cursa course certificate for beginner Python video material; Corey Schafer is named as the course source, not the credential issuer.",
        "status": "Verified Credential",
        "drive_id": "1M9pHTaObCq94-pDeeClqlROfzj3No0C9",
    },
    {
        "title": "Operating Systems and Systems Programming by John Kubiatowicz (on Cursa)",
        "issuer": "Cursa Educational Platform",
        "date": "Academic Year 2024\u20132025",
        "kind": "Course Certification",
        "subject": "Systems Engineering",
        "domain": "Software Engineering",
        "tags": ["Operating Systems", "Process Management", "Concurrency", "Memory Paging"],
        "detail": "Cursa course certificate for operating systems video material; it does not document a systems project or assessment.",
        "status": "Verified Credential",
        "drive_id": "1FAzedgR0ARUsWZJPZUwqrK6QdV_ejUmP",
    },
    {
        "title": "Excel Skill Certification",
        "issuer": "One Roadmap Skill Certification",
        "date": "13 May 2025",
        "kind": "Skill Assessment",
        "subject": "Data Tools",
        "domain": "Software Engineering",
        "tags": ["Excel", "Data Modeling", "Lookup Formulas", "Pivot Tables"],
        "detail": "One Roadmap Excel skill certification; the certificate does not specify advanced spreadsheet engineering topics.",
        "status": "Verified Credential",
        "drive_id": "1TMSGrC1wqNXOP72kYDwy9xBZkB-1-4IJ",
    },
    {
        "title": "Cloud computing - beginner to advance by University of Illinois (on Cursa)",
        "issuer": "Cursa Educational Platform",
        "date": "11 Feb 2026",
        "kind": "Course Certification",
        "subject": "Systems Engineering",
        "domain": "Software Engineering",
        "tags": ["Cloud Computing", "Virtualization", "IaaS/PaaS", "Infrastructure"],
        "detail": "Cursa course certificate for cloud computing video material; University of Illinois is named as the source, not the credential issuer.",
        "status": "Verified Credential",
        "drive_id": "1QNqhpqt-UUg2Wt07VuncV5uyBPJPqpY0",
    },
    {
        "title": "Web Development Full course by Edureka (on Cursa)",
        "issuer": "Cursa Educational Platform",
        "date": "11 Feb 2026",
        "kind": "Course Certification",
        "subject": "Web Development",
        "domain": "Software Engineering",
        "tags": ["HTML5", "CSS3", "JavaScript", "DOM Manipulation", "Responsive Design"],
        "detail": "Cursa course certificate for web development video material; Edureka is named as the source, not the credential issuer.",
        "status": "Verified Credential",
        "drive_id": "12id3nL_XH3DHTNrB8ArVvMvLTcJxgb36",
    },

    # Domain: Geospatial & Remote Sensing
    {
        "title": "Advanced Image Analysis for Geospatial Professionals — Workshop",
        "issuer": "IIRS / ISRO Outreach",
        "date": "12 Nov 2025",
        "kind": "Workshop Participation",
        "subject": "Image Analysis",
        "domain": "Geospatial & Remote Sensing",
        "tags": ["Image Analysis", "Geospatial", "IIRS Workshop"],
        "detail": "One-day online workshop participation, as printed on the original IIRS document. A privacy-safe public copy is linked.",
        "status": "Participation confirmed",
        "drive_id": "",
    },
    {
        "title": "Advances in Thermal Infrared Remote Sensing for Ecological Studies (Course 1047)",
        "issuer": "IIRS / ISRO Outreach",
        "date": "3 Nov 2025",
        "kind": "Workshop Participation",
        "subject": "Remote Sensing",
        "domain": "Geospatial & Remote Sensing",
        "tags": ["Thermal Infrared", "Ecological Modeling", "Surface Temperature", "ISRO"],
        "detail": "IIRS outreach online-course participation document. The linked public copy removes enrollment and verification identifiers.",
        "status": "Participation documented",
        "drive_id": "",
    },
    {
        "title": "Aerosols Measurement, Retrieval and Impacts (Course 1052)",
        "issuer": "IIRS / ISRO Outreach",
        "date": "12 Jan 2026",
        "kind": "Workshop Participation",
        "subject": "Remote Sensing",
        "domain": "Geospatial & Remote Sensing",
        "tags": ["Aerosol Optical Depth", "Atmospheric Remote Sensing", "MODIS", "ISRO"],
        "detail": "IIRS outreach online-course participation document. The linked public copy removes enrollment and verification identifiers.",
        "status": "Participation documented",
        "drive_id": "",
    },
    {
        "title": "Basics of Remote Sensing, GIS and Global Navigation Satellite Systems (Course 169)",
        "issuer": "IIRS / ISRO Outreach",
        "date": "7 Feb 2026",
        "kind": "Online Course Participation",
        "subject": "GIS & Satellite Systems",
        "domain": "Geospatial & Remote Sensing",
        "tags": ["Remote Sensing", "GIS", "GNSS", "Coordinate Systems", "ISRO"],
        "detail": "IIRS outreach online-course participation document. The linked public copy removes enrollment and verification identifiers.",
        "status": "Participation documented",
        "drive_id": "",
    },
    {
        "title": "Geospatial Technology for Modelling of Urban Environments (Course 162)",
        "issuer": "IIRS / ISRO Outreach",
        "date": "28 Jun 2025",
        "kind": "Online Course Participation",
        "subject": "Urban GIS",
        "domain": "Geospatial & Remote Sensing",
        "tags": ["Urban Modeling", "3D GIS", "Land Cover Change", "Spatial Planning", "ISRO"],
        "detail": "IIRS outreach online-course participation document. The linked public copy removes enrollment and verification identifiers.",
        "status": "Participation documented",
        "drive_id": "",
    },
    {
        "title": "Overview of Geocomputation and Geo-Web Services (Course 173)",
        "issuer": "IIRS / ISRO Outreach",
        "date": "12 Jan 2026",
        "kind": "Online Course Participation",
        "subject": "Spatial Web Services",
        "domain": "Geospatial & Remote Sensing",
        "tags": ["Geocomputation", "OGC Web Services", "WMS/WFS", "Spatial Databases", "ISRO"],
        "detail": "IIRS outreach online-course participation document. The linked public copy removes enrollment and verification identifiers.",
        "status": "Participation documented",
        "drive_id": "",
    },
    {
        "title": "Overview of Geographical Information Systems (Course 150)",
        "issuer": "IIRS / ISRO Outreach",
        "date": "22 Nov 2024",
        "kind": "Online Course Participation",
        "subject": "GIS Foundations",
        "domain": "Geospatial & Remote Sensing",
        "tags": ["GIS", "Spatial Projections", "Cartography", "ISRO"],
        "detail": "IIRS outreach online-course participation document. The linked public copy removes enrollment and verification identifiers.",
        "status": "Participation documented",
        "drive_id": "",
    },
    {
        "title": "Overview of Geographical Information Systems (Course 172)",
        "issuer": "IIRS / ISRO Outreach",
        "date": "17 Nov 2025",
        "kind": "Online Course Participation",
        "subject": "GIS Topology",
        "domain": "Geospatial & Remote Sensing",
        "tags": ["GIS", "Spatial Analysis", "Overlay Operations", "Database Design", "ISRO"],
        "detail": "IIRS outreach online-course participation document. The linked public copy removes enrollment and verification identifiers.",
        "status": "Participation documented",
        "drive_id": "",
    },
    {
        "title": "Overview of Global Navigation Satellite Systems (Course 170)",
        "issuer": "IIRS / ISRO Outreach",
        "date": "3 Nov 2025",
        "kind": "Online Course Participation",
        "subject": "GNSS Navigation",
        "domain": "Geospatial & Remote Sensing",
        "tags": ["GNSS", "NavIC", "GPS", "Differential Positioning", "ISRO"],
        "detail": "IIRS outreach online-course participation document. The linked public copy removes enrollment and verification identifiers.",
        "status": "Participation documented",
        "drive_id": "",
    },
    {
        "title": "RS & GIS Applications in Natural Resource Management (Course 174)",
        "issuer": "IIRS / ISRO Outreach",
        "date": "12 Jan 2026",
        "kind": "Online Course Participation",
        "subject": "Resource Management",
        "domain": "Geospatial & Remote Sensing",
        "tags": ["Natural Resources", "Watershed Delineation", "Forestry", "ISRO"],
        "detail": "IIRS outreach online-course participation document. The linked public copy removes enrollment and verification identifiers.",
        "status": "Participation documented",
        "drive_id": "",
    },
    {
        "title": "Remote Sensing and Numerical Ocean Modelling for Oceanic Processes",
        "issuer": "IIRS / ISRO Outreach",
        "date": "3 Nov 2025",
        "kind": "Online Course Participation",
        "subject": "Ocean Remote Sensing",
        "domain": "Geospatial & Remote Sensing",
        "tags": ["Oceanography", "Altimetry", "Sea Surface Temperature", "Hydrodynamics", "ISRO"],
        "detail": "IIRS outreach online-course participation document. The linked public copy removes enrollment and verification identifiers.",
        "status": "Participation documented",
        "drive_id": "",
    },
    {
        "title": "Remote Sensing Data Analytics for Crop Production Forecasting (Course 168)",
        "issuer": "IIRS / ISRO Outreach",
        "date": "17 Jul 2025",
        "kind": "Online Course Participation",
        "subject": "Agricultural Analytics",
        "domain": "Geospatial & Remote Sensing",
        "tags": ["Crop Forecasting", "NDVI Time Series", "Yield Modeling", "ISRO"],
        "detail": "IIRS outreach online-course participation document. The linked public copy removes enrollment and verification identifiers.",
        "status": "Participation documented",
        "drive_id": "",
    },
    {
        "title": "Advances in Remote Sensing Techniques for Geological Applications (Course 171)",
        "issuer": "IIRS / ISRO Outreach",
        "date": "3 Nov 2025",
        "kind": "Online Course Participation",
        "subject": "Planetary Geology",
        "domain": "Geospatial & Remote Sensing",
        "tags": ["Planetary Geology", "Hyperspectral", "Mineral Mapping", "ISRO"],
        "detail": "IIRS outreach online-course participation document. The linked public copy removes enrollment and verification identifiers.",
        "status": "Participation documented",
        "drive_id": "",
    },
    {
        "title": "Research and Career Opportunities for Space Science & Technology in India (Course 175)",
        "issuer": "IIRS / ISRO Outreach",
        "date": "12 Jan 2026",
        "kind": "Online Course Participation",
        "subject": "Space Science",
        "domain": "Geospatial & Remote Sensing",
        "tags": ["Space Tech", "Mission Payloads", "Satellite Systems", "ISRO"],
        "detail": "IIRS outreach online-course participation document. The linked public copy removes enrollment and verification identifiers.",
        "status": "Participation documented",
        "drive_id": "",
    },
    {
        "title": "Space Exploration Technology: An Overview (Course 159)",
        "issuer": "IIRS / ISRO Outreach",
        "date": "1 Jun 2025",
        "kind": "Online Course Participation",
        "subject": "Space Technology",
        "domain": "Geospatial & Remote Sensing",
        "tags": ["Launch Vehicles", "Orbital Mechanics", "Spacecraft Subsystems", "ISRO"],
        "detail": "IIRS outreach online-course participation document. The linked public copy removes enrollment and verification identifiers.",
        "status": "Participation documented",
        "drive_id": "",
    },
    {
        "title": "Space Inputs for Village-Level Crop Assessment (Course 1041)",
        "issuer": "IIRS / ISRO Outreach",
        "date": "26 Mar 2025",
        "kind": "Workshop Participation",
        "subject": "Agricultural Remote Sensing",
        "domain": "Geospatial & Remote Sensing",
        "tags": ["Cadastral Mapping", "High-Resolution Imagery", "Agritech", "ISRO"],
        "detail": "IIRS outreach online-course participation document. The linked public copy removes enrollment and verification identifiers.",
        "status": "Participation documented",
        "drive_id": "",
    },
    {
        "title": "Recent Trends in Ecological Modelling & Simulation (Course 161)",
        "issuer": "IIRS / ISRO Outreach",
        "date": "28 Jun 2025",
        "kind": "Online Course Participation",
        "subject": "Ecological GIS",
        "domain": "Geospatial & Remote Sensing",
        "tags": ["Ecological Simulation", "Habitat Suitability", "Biodiversity GIS", "ISRO"],
        "detail": "IIRS outreach online-course participation document. The linked public copy removes enrollment and verification identifiers.",
        "status": "Participation documented",
        "drive_id": "",
    },
    {
        "title": "Archival and Access of Space Science Data",
        "issuer": "IIRS / ISRO Outreach",
        "date": "17 Jul 2025",
        "kind": "Online Course Participation",
        "subject": "Space Data Science",
        "domain": "Geospatial & Remote Sensing",
        "tags": ["ISDA Portal", "Data Archival", "PDS4 Standard", "Metadata", "ISRO"],
        "detail": "IIRS outreach online-course participation document. The linked public copy removes enrollment and verification identifiers.",
        "status": "Participation documented",
        "drive_id": "",
    },
    {
        "title": "The Method of Space Science Research (Course 160)",
        "issuer": "IIRS / ISRO Outreach",
        "date": "28 Jun 2025",
        "kind": "Online Course Participation",
        "subject": "Research Methodology",
        "domain": "Geospatial & Remote Sensing",
        "tags": ["Research Methodology", "Scientific Computing", "Data Calibration", "ISRO"],
        "detail": "IIRS outreach online-course participation document. The linked public copy removes enrollment and verification identifiers.",
        "status": "Participation documented",
        "drive_id": "",
    },
    {
        "title": "Origin of the Universe and Solar System Exploration (Course 1053)",
        "issuer": "IIRS / ISRO Outreach",
        "date": "21 Jan 2026",
        "kind": "Workshop Participation",
        "subject": "Astrophysics",
        "domain": "Geospatial & Remote Sensing",
        "tags": ["Astrophysics", "Solar Physics", "Planetary Science", "ISRO"],
        "detail": "IIRS outreach online-course participation document. The linked public copy removes enrollment and verification identifiers.",
        "status": "Participation documented",
        "drive_id": "",
    },

    # Domain: Professional Development
    {
        "title": "Coding-Track Micro-Internship Program",
        "issuer": "Talerang \u00b7 Cloudwrk Partner",
        "date": "Academic Year 2025",
        "kind": "Micro-Internship",
        "subject": "Industry Readiness",
        "domain": "Professional Development",
        "tags": ["Software Engineering", "Workplace Readiness", "Code Quality", "Collaboration"],
        "detail": "Talerang coding-track micro-internship career-readiness program in association with Cloudwrk. The certificate records a PASS grade; it does not document a client software deliverable.",
        "status": "Verified Credential",
        "drive_id": "1SDGQMPSTE_5jUZa7LCSEt7mX60VeqxhH",
    },
    {
        "title": "Master Social Media Ads webinar",
        "issuer": "SkillEcted Campus Program",
        "date": "28 Nov 2024",
        "kind": "Webinar Participation",
        "subject": "Marketing Tech",
        "domain": "Professional Development",
        "tags": ["Digital Campaigns", "Analytics", "Audience Segmentation", "Optimization"],
        "detail": "Certificate of participation in the Master Social Media Ads webinar; no campaign results or assessed competency are documented.",
        "status": "Verified Credential",
        "drive_id": "1fo5fOsJi1Ut5xiPGzZSyBNHMevf-0CzV",
    },

    # Domain: Academic & Extension Honors
    {
        "title": "Certificate of Extension Work (120+ Documented Field Hours)",
        "issuer": "University of Mumbai DLLE",
        "date": "30 Apr 2026",
        "kind": "University Extension Award",
        "subject": "Community Leadership",
        "domain": "Academic & Extension Honors",
        "tags": ["DLLE", "University of Mumbai", "Community Service", "Social Impact"],
        "detail": "Awarded by the Department of Lifelong Learning and Extension (DLLE), University of Mumbai, for completing over 120 verified field hours of institutional outreach and community initiatives.",
        "status": "University Award",
        "drive_id": "1TiYoTYAcfwcNY4Q1iIRXUk5O0zbKXJGx",
    },
    {
        "title": "World Sparrow Day 2025 Online Quiz",
        "issuer": "Indian Biodiversity Conservation Society",
        "date": "20 Mar 2025",
        "kind": "Quiz Participation",
        "subject": "Environmental Science",
        "domain": "Academic & Extension Honors",
        "tags": ["Biodiversity", "Conservation", "Seminar", "Environmental Science"],
        "detail": "Participation in an online World Sparrow Day quiz; this document does not establish a seminar or academic distinction.",
        "status": "Participation",
        "drive_id": "1VcULmKLt7SwKXghQQ2mHj7gsMjnxjTGB",
    },
    {
        "title": "Environment Management System Audit (EMSA)",
        "issuer": "SYNERGY Consultants (P) Ltd & Hansraj Jivandas College",
        "date": "Academic Year 2024\u20132025",
        "kind": "Certified Course (2 Credits)",
        "subject": "Environmental Systems & Auditing",
        "domain": "Academic & Extension Honors",
        "tags": ["ISO 14001", "EMSA", "Environmental Audit", "Compliance"],
        "detail": "Completed the two-credit Environment Management System Audit course in 2024–25, as printed on the certificate; specific ISO standards and corporate methods are not documented.",
        "status": "Certified Course",
        "drive_id": "1QSQ-c0bWeYErjKTuJ6SFWyr1t2xN-0bG",
    },
    {
        "title": "National Financial Literacy Certification (World Investor Week)",
        "issuer": "NISM / SEBI (VESASC Examination)",
        "date": "19 Oct 2024",
        "kind": "National Examination",
        "subject": "Financial Literacy",
        "domain": "Academic & Extension Honors",
        "tags": ["SEBI", "NISM", "Financial Literacy", "Regulation"],
        "detail": "Scored a perfect 100% on the national investor financial literacy examination conducted under the auspices of SEBI and the National Institute of Securities Markets (NISM).",
        "status": "100% Score",
        "drive_id": "1cOnLxXZZJ1ndNEfkJYN9vMFzWWdZJdxW",
    },
    {
        "title": "Smart India Hackathon 2025: Round 1 Winner & Principal Nomination",
        "issuer": "AICTE / Smart India Hackathon & VESASC",
        "date": "23 Sep 2025",
        "kind": "College Hackathon Recognition",
        "subject": "AI / ML",
        "domain": "Academic & Extension Honors",
        "tags": ["Smart India Hackathon", "DBTDecoders", "Principal Nomination", "NSP AI"],
        "detail": "College Round 1 recognition and official principal nomination (Ref: VC/SFC/2025-26/0604) for the DBTDecoders National Scholarship Portal assistant proposal. The source package does not establish a completed chatbot deployment or national award.",
        "status": "Institutional Recognition",
    },
    {
        "title": "Smart India Hackathon 2026: Team EchoLogic Selected Architecture (PS SIH26090)",
        "issuer": "AICTE / Smart India Hackathon",
        "date": "Academic Year 2026",
        "kind": "Hackathon Team Selection",
        "subject": "AI / ML",
        "domain": "Academic & Extension Honors",
        "tags": ["Smart India Hackathon", "EchoLogic", "KARIGAR-SETU", "Multimodal AI"],
        "detail": "Selected team proposal for Problem Statement SIH26090: KARIGAR-SETU, an AI-powered smart cataloging and market linkage platform for marginalized artisans.",
        "status": "Institutional Recognition",
    },
]


# Original IIRS documents are private. These keys point only to separately
# rendered, identifier-free public participation copies in site assets.
IIRS_PUBLIC_KEYS = [
    "1046", "1048", "1047", "1052", "169", "162", "173", "150", "172", "170",
    "174", "ocean", "168", "171", "175", "159", "1041", "161", "archival", "160", "1053",
]
_iirs_records = [c for c in CREDENTIALS if c["issuer"] == "IIRS / ISRO Outreach"]
assert len(_iirs_records) == len(IIRS_PUBLIC_KEYS) == 21
for _record, _key in zip(_iirs_records, IIRS_PUBLIC_KEYS):
    _record["public_pdf"] = f"assets/documents/iirs-outreach/iirs-{_key}-participation.pdf"
    _record["tags"] = [_record["subject"], _record["kind"], "IIRS Outreach"]

# Certificate tags describe the printed credential, not an inferred syllabus or
# an independently implemented project.
for _record in CREDENTIALS:
    if _record["title"] == "Machine Learning and Image Processing":
        _record["tags"] = ["Machine Learning", "Image Processing", "thingQbator"]
    elif _record["title"] == "Data Science Career Track Masterclass":
        _record["tags"] = ["Data Science", "Masterclass", "Participation"]
    elif _record["title"] == "Artificial Intelligence Beginner Skill Certification":
        _record["tags"] = ["Artificial Intelligence", "Beginner Skill Test"]
    elif _record["title"] == "Excel Skill Certification":
        _record["tags"] = ["Excel", "Skill Test"]
    elif _record["title"] == "Master Social Media Ads webinar":
        _record["tags"] = ["Social Media Ads", "Webinar", "Participation"]
    elif _record["title"] == "World Sparrow Day 2025 Online Quiz":
        _record["tags"] = ["World Sparrow Day", "Quiz", "Participation"]
    elif _record["title"] == "Environment Management System Audit (EMSA)":
        _record["tags"] = ["EMSA", "Environmental Audit", "Two-Credit Course"]


def project_card(item):
    repo_btn = link(item["repo"], "GitHub Repository ↗", "button button-small button-quiet", external=True) if item.get("repo") else ""
    live_btn = link(item["live"], "Live Deployment ↗", "button button-small button-quiet", external=True) if item.get("live") else ""
    evidence_btn = link(item["evidence"], "Workflow Canvas →", "button button-small button-quiet") if item.get("evidence") else ""
    detail_btn = link(item["route"], "Read Case Study →", "button button-small card-main-link")

    tags_html = "".join(f'<span class="tag">{escape(t)}</span>' for t in item.get("tags", []))
    highlight = f'<p class="card-highlight">{escape(item["highlight"])}</p>' if item.get("highlight") else ""

    return (
        f'<article class="card project-card clickable-card" data-filter-card data-pillar="{escape(item["pillar"], quote=True)}" data-category="{escape(item["category"], quote=True)}">'
        f'<div class="card-top">{eyebrow(item["pillar"])}{badge(item["status"])}</div>'
        f'<h3><a class="card-main-link" href="{escape(item["route"], quote=True)}">{escape(item["name"])}</a></h3>'
        f'<p class="card-category-sub">{escape(item["category"])}</p>'
        f'<p>{escape(item["summary"])}</p>'
        f'{highlight}'
        f'<div class="tags-row">{tags_html}</div>'
        f'<div class="card-actions">{detail_btn}{live_btn}{repo_btn}{evidence_btn}</div>'
        f'</article>'
    )


def experience_card(item):
    badge_html = badge(item.get("badge", "VERIFIED"), "status") if "badge" in item else ""
    status_note = f'<p class="card-category-sub"><em>{escape(item["status_note"])}</em></p>' if "status_note" in item else ""

    doc_links = []
    if item["name"] == "AwareWolf":
        doc_links.append(link("https://drive.google.com/file/d/1pShS64xWmhduHrJyiORbXDGBBXuKAnjc/view", "Appointment Letter ↗", "button button-small button-quiet", external=True))
    elif "Advfiction" in item["name"]:
        doc_links.append(link("https://drive.google.com/file/d/1Q_zS8HQjH03CE4nwsZyvVjkP3t1EI6hn/view", "Web Dev Cert ↗", "button button-small button-quiet", external=True))
        doc_links.append(link("https://drive.google.com/file/d/1T_3ZDXAFRpxJ6-GDZAkyCPVchJdR7815/view", "AI Automation Cert ↗", "button button-small button-quiet", external=True))
        doc_links.append(link("https://drive.google.com/file/d/1r2tEKiVldHHaL94S_brIEPRVAwsiNRxM/view", "Executive LOR ↗", "button button-small button-quiet", external=True))
    elif "AlgoDevOpss" in item["name"]:
        doc_links.append(link("https://drive.google.com/file/d/1yZyBwiDStZatvvD9oj5rlM1WUTBkz9BV/view", "Full-Stack Cert ↗", "button button-small button-quiet", external=True))

    doc_links_html = f'<div class="doc-links" style="margin-top: 0.5rem; display: flex; flex-wrap: wrap; gap: 0.4rem;">{"".join(doc_links)}</div>' if doc_links else ""

    return (
        f'<article class="card experience-card clickable-card">'
        f'<div class="card-top">{eyebrow(item["dates"])}{badge_html}</div>'
        f'<h3><a class="card-main-link" href="{escape(item["route"], quote=True)}">{escape(item["name"])}</a></h3>'
        f'<p class="meta">{escape(item["role"])}</p>'
        f'{status_note}'
        f'<p>{escape(item["summary"])}</p>'
        f'{doc_links_html}'
        f'<div class="card-actions" style="margin-top: var(--space-sm);">{link(item["route"], "Explore Engineering Contribution →", "button button-small")}</div>'
        f'</article>'
    )


def credential_card(item):
    title = item["title"]
    issuer = item["issuer"]
    date = item["date"]
    kind = item["kind"]
    subject = item["subject"]
    domain = item["domain"]
    detail = item["detail"]
    status = item.get("status", "")
    tags = item.get("tags", [])
    drive_id = item.get("drive_id")
    public_pdf = item.get("public_pdf")
    verify_url = item.get("verify_url")

    tags_html = "".join(f'<span class="tag">{escape(t)}</span>' for t in tags)
    search = f"{title} {issuer} {kind} {subject} {domain} {detail} {' '.join(tags)}".lower()

    badge_html = badge(status, "status") if status and status not in ("Verified Credential", "Primary Document Verified") else ""

    actions = []
    if drive_id:
        actions.append(link(f"https://drive.google.com/file/d/{drive_id}/view", "View original certificate ↗", "button button-small", external=True))
    if public_pdf:
        actions.append(link(public_pdf, "View privacy-safe participation copy ↗", "button button-small", external=True))
    if verify_url:
        actions.append(link(verify_url, "Verify with issuer ↗", "button button-small button-quiet", external=True))

    actions_html = f'<div class="card-actions">{ "".join(actions) }</div>' if actions else ""

    return (
        f'<article class="card credential-card" data-filter-card data-issuer="{escape(issuer, quote=True)}" '
        f'data-type="{escape(kind, quote=True)}" data-subject="{escape(subject, quote=True)}" '
        f'data-domain="{escape(domain, quote=True)}" data-search="{escape(search, quote=True)}">'
        f'<div class="card-top">{eyebrow(kind)}{badge_html}</div>'
        f'<h3>{escape(title)}</h3>'
        f'<p class="meta">{escape(issuer)} · {escape(date)}</p>'
        f'<p class="prose-small">{escape(detail)}</p>'
        f'<div class="tags-row">{tags_html}</div>'
        f'{actions_html}'
        f'</article>'
    )


PAGES = {}

# 1. HOMEPAGE: index.html
PAGES["index.html"] = (
    "Home",
    "Rehan Memon | Home",
    "AI engineering and software systems portfolio featuring computer vision, full-stack real-time collaboration, retrieval-augmented generation, and automated workflows.",
    '<section class="hero container">'
    '<div>'
    + eyebrow("AI Engineering · Machine Learning · RAG & LLM Systems · Backend Architecture")
    + '<h1>Rehan Juned Memon<span class="accent">.</span></h1>'
    '<p class="hero-lead">I build <strong>intelligent software systems</strong> across machine learning, computer vision, retrieval-augmented generation (RAG), LLM-powered applications, real-time backend services, and workflow automation.</p>'
    '<p class="hero-sublead" style="color: var(--text-muted); margin-bottom: var(--space-md); font-size: 1.05rem; line-height: 1.5;">My work combines Python, model and data pipelines, LLM integrations, retrieval systems, backend architecture, and full-stack engineering to turn technical ideas into usable software.</p>'
    f'<p class="meta">B.Sc. Artificial Intelligence · <a class="text-link" href="{COLLEGE_URL}" target="_blank" rel="noopener noreferrer">{COLLEGE_NAME_SHORT}</a> (Autonomous), University of Mumbai · 2024–2027 · Semester IV SGPA: <strong>9.27/10</strong> | Cumulative CGPA: <strong>8.14/10</strong> (Semesters I–IV)</p>'
    '<div class="actions">'
    + link("projects.html", "Explore All Work", "button")
    + link(RESUME_URL, "View Resume (Google Doc) ↗", "button button-accent-outline", external=True)
    + link("experience.html", "Experience", "button button-quiet")
    + link("contact.html", "Get in touch →")
    + '</div>'
    '</div>'
    '<aside class="hero-aside" aria-label="Work overview">'
    + eyebrow("Core Competencies")
    + '<h2>Three Engineering Pillars</h2>'
    '<p>Explore implemented projects, collaborative web work and evidence-labelled workflow designs:</p>'
    '<div class="pillar-links">'
    + link("projects.html#pillar-ai", "1. AI & Machine Learning Systems →")
    + link("projects.html#pillar-client", "2. Client & Collaborative Engineering →")
    + link("projects.html#pillar-automation", "3. AI & Workflow Automation →")
    + '</div>'
    '</aside>'
    '</section>'
    + section(
        "Featured AI Engineering Work",
        '<p class="section-lead">Four flagship software systems demonstrating machine learning, retrieval-augmented AI, real-time backend architecture, and multi-source automation pipelines.</p>'
        '<div class="grid two">'
        + project_card(get_project("ConnectHub — Real-Time AI Messaging Engine"))
        + project_card(get_project("AI Research Assistant"))
        + project_card(get_project("Signature Verification AI"))
        + project_card(get_project("Autonomous Job Search Engine"))
        + '</div>'
        '<div class="section-nav-group">'
        + link("projects.html", "View All 14 Projects Across Pillars →", "button")
        + '<div class="sub-nav-links">'
        + link("client-work.html", "Client Deployments →")
        + link("automation.html", "AI & Workflow Automation Systems →")
        + link("credentials.html", "Explore Credentials & Achievements (48) →")
        + '</div>'
        + '</div>',
        "featured-ai-work",
    )
    + section(
        "Selected Client Deployments",
        '<p class="section-lead">Selected client and collaborative systems, with live deployments and prototypes labeled according to their evidence.</p>'
        '<div class="grid two">'
        + project_card(get_project("Advfiction Enterprise Lead LMS"))
        + project_card(get_project("LMS Girls Higher Secondary School"))
        + '</div>'
        '<div class="section-nav-group">'
        + link("client-work.html", "Explore All Client Case Studies →", "button button-small")
        + '</div>',
        "selected-client-work",
    )
    + section(
        "Commercial & Team Experience",
        '<p class="section-lead">Documented engineering contributions across commercial internships and academic web platforms, with direct verification documents accessible immediately.</p>'
        '<div class="grid three">'
        + "".join(experience_card(e) for e in EXPERIENCE)
        + '</div>'
        '<div class="section-nav-group">'
        + link("experience.html", "View Comprehensive Experience →", "button")
        + '<div class="sub-nav-links">'
        + link("awarewolf.html", "AwareWolf Deep Dive →")
        + link("advfiction.html", "Advfiction Deep Dive →")
        + link("algodevopss.html", "AlgoDevOpss Deep Dive →")
        + '</div>'
        + '</div>',
    )
    + section(
        "Academic Distinction & Verified Honors",
        '<div class="grid two">'
        '<article class="card clickable-card">'
        + eyebrow("University of Mumbai")
        + f'<h3><a class="card-main-link" href="{COLLEGE_URL}" target="_blank" rel="noopener noreferrer">{COLLEGE_NAME_FULL}</a></h3>'
        '<p><strong>Semester IV SGPA: 9.27/10</strong> (Grade O Distinction), cumulative CGPA: <strong>8.14/10</strong> across 88 completed credits in B.Sc. Artificial Intelligence. Examination records confirm top scores in AI in IoT (98%) and Generative AI (94%).</p>'
        + '<div class="card-actions">'
        + link("about.html", "Detailed academic background →", "button button-small button-quiet")
        + '</div>'
        + '</article>'
        '<article class="card clickable-card">'
        + eyebrow("National Recognition & Verified Certifications")
        + '<h3><a class="card-main-link" href="credentials.html">Competitive Awards & Credentials</a></h3>'
        '<p>Nominated team member representing VESASC for <strong>Smart India Hackathon 2025</strong> (Team DBTDecoders). The credential library includes IIRS/ISRO outreach records, a <strong>BCG X GenAI simulation</strong>, and <strong>120+ verified field hours</strong> with University of Mumbai DLLE. IIRS document types are being reconciled individually.</p>'
        + '<div class="card-actions">'
        + link("credentials.html", "Explore Credentials & Achievements (48) →", "button button-small")
        + '</div>'
        + '</article>'
        '</div>',
    )
    + explore_more("index.html"),
)
# 2. ABOUT: about.html
PAGES["about.html"] = (
    "About",
    "Rehan Memon | About",
    "Academic background, technical specializations, and engineering principles for Rehan Juned Memon.",
    intro(
        "About Me",
        "Bridging Machine Learning & Usable Systems",
        "I am a B.Sc. Artificial Intelligence undergraduate at Vivekanand Education Society's College of Arts, Science & Commerce, University of Mumbai. I am interested in building practical AI applications and reliable software systems, combining machine learning, backend engineering and full-stack development.",
    )
    + section(
        "Academic Foundation",
        '<div class="prose">'
        f'<p>Currently pursuing a <strong>{DEGREE_NAME}</strong> (2024–2027) at <a class="text-link" href="{COLLEGE_URL}" target="_blank" rel="noopener noreferrer">{COLLEGE_NAME_FULL}</a>, within the <a class="text-link" href="{AI_DEPT_URL}" target="_blank" rel="noopener noreferrer">Department of Artificial Intelligence</a>, affiliated with the University of Mumbai.</p>'
        '<p>Academic standing: <strong>9.27/10 SGPA</strong> (Semester IV) with an <strong>8.14/10 cumulative CGPA</strong> across completed coursework.</p>'
        + '<p>' + link("activities.html#academic-distinctions", "View detailed coursework scores and semester marks →") + '</p>'
        '</div>',
    )
    + section(
        "Technical Focus & Skills Matrix",
        '<p class="section-lead">Selected technical skills mapped to relevant projects, case studies and credentials.</p>'
        '<div class="skills-matrix">'
        '<div class="skill-card">'
        + eyebrow("Core Discipline 1")
        + '<h3>AI & Machine Learning Systems</h3>'
        '<p>Classical machine learning, computer vision feature engineering, and retrieval-augmented generation.</p>'
        '<div class="skill-chips">\n'
        + '\n'.join([
            link("signature-verification.html", "OpenCV Image Pipelines", "skill-chip"),
            link("signature-verification.html", "Scikit-Learn / SVM", "skill-chip"),
            link("ai-research-assistant.html", "ChromaDB Vector Store", "skill-chip"),
            link("ai-research-assistant.html", "RAG & Embeddings", "skill-chip"),
            link("signature-verification.html", "FastAPI Inference", "skill-chip"),
            link("connecthub.html", "Gemini AI Summarization", "skill-chip"),
            link("connecthub.html", "JSONB Vector Similarity", "skill-chip"),
            link("credentials.html", "ISRO Geospatial AI", "skill-chip"),
        ])
        + '\n</div>'
        '</div>'
        '<div class="skill-card">'
        + eyebrow("Core Discipline 2")
        + '<h3>Full-Stack Software Engineering</h3>'
        '<p>Robust frontend architectures, typed REST API services, and relational persistence.</p>'
        '<div class="skill-chips">\n'
        + '\n'.join([
            link("awarewolf.html", "React 19 & TypeScript", "skill-chip"),
            link("algodevopss.html", "Next.js 16 Portal", "skill-chip"),
            link("connecthub.html", "FastAPI & WebSockets", "skill-chip"),
            link("connecthub.html", "Async SQLAlchemy 2.1", "skill-chip"),
            link("client-work.html#advfiction-lms", "Node.js & Express APIs", "skill-chip"),
            link("client-work.html#advfiction-lms", "Supabase / PostgreSQL", "skill-chip"),
            link("client-work.html#girls-hss", "Responsive Web Architecture", "skill-chip"),
            link("client-work.html", "Production Deployments", "skill-chip"),
        ])
        + '\n</div>'
        '</div>'
        '<div class="skill-card">'
        + eyebrow("Core Discipline 3")
        + '<h3>AI & Workflow Automation</h3>'
        '<p>Multi-stage autonomous pipelines, API integrations, and event-driven document generation.</p>'
        '<div class="skill-chips">\n'
        + '\n'.join([
            link("job-search-automation.html", "Autonomous Job Search Engine", "skill-chip"),
            link("job-search-automation.html", "Keyless ATS Ingestion", "skill-chip"),
            link("job-search-automation.html", "Streamlit Analytics UI", "skill-chip"),
            link("automation.html#wf-maps-scraper", "n8n Orchestration", "skill-chip"),
            link("automation.html#wf-maps-scraper", "Apify Actor Scrapers", "skill-chip"),
            link("automation.html#wf-postgres-research", "PostgreSQL Batch ETL", "skill-chip"),
            link("automation.html#wf-lead-dossier", "PDF Document Compilation", "skill-chip"),
            link("automation.html#wf-subworkflow-router", "Webhook Handlers", "skill-chip"),
            link("automation.html", "10 n8n Canvas Architectures", "skill-chip"),
        ])
        + '\n</div>'
        '</div>'
        '<div class="skill-card">'
        + eyebrow("Core Discipline 4")
        + '<h3>Data Science & Geospatial Analysis</h3>'
        '<p>Remote-sensing satellite data processing, digital elevation modeling, and spectral indices.</p>'
        '<div class="skill-chips">\n'
        + '\n'.join([
            link("credentials.html", "Satellite Image Analysis", "skill-chip"),
            link("credentials.html", "ISRO / IIRS Programs", "skill-chip"),
            link("credentials.html", "Spectral Classification", "skill-chip"),
            link("credentials.html", "Pandas & NumPy EDA", "skill-chip"),
            link("credentials.html", "GIS Topology & GNSS", "skill-chip"),
        ])
        + '\n</div>'
        '</div>'
        '</div>',
    )
    + section(
        "Engineering Principles",
        '<div class="prose">'
        '<p>I prioritize software clarity, deterministic reproducibility, and evidence-grounded engineering over hype:</p>'
        '<ul class="prose-list">'
        '<li><strong>Deterministic Retrieval:</strong> When building RAG pipelines, I enforce explicit source citation mapping, cosine similarity thresholds, and chunk-level metadata tracking.</li>'
        '<li><strong>Defensive Persistence:</strong> Concurrency issues and race conditions must be resolved through content-addressed storage (SHA-256), atomic write protocols, and revision tokens.</li>'
        '<li><strong>Empirical Validation:</strong> I verify system capabilities through automated test suites (pytest, vitest) and objective benchmarks rather than anecdotal impressions.</li>'
        '</ul>'
        '</div>',
    )
    + explore_more("about.html"),
)

# 3. EXPERIENCE: experience.html
PAGES["experience.html"] = (
    "Experience",
    "Rehan Memon | Experience",
    "Documented engineering internships across software development, AI automation, and web platforms.",
    intro(
        "Experience",
        "Commercial & Team Engineering",
        "Three documented internship engagements demonstrating full-stack engineering, API architecture, media validation pipelines, and enterprise workflow orchestration. Primary verification credentials and appointment documents are linked directly on each card.",
    )
    + section(
        "Commercial & Team Engagements",
        '<div class="grid three">'
        + "".join(experience_card(e) for e in EXPERIENCE)
        + '</div>',
    )
    + section(
        "Completed Enterprise Simulations & Micro-Internships",
        '<div class="grid two">'
        '<article class="card">'
        '<div class="card-top">'
        + eyebrow("BCG X via Forage · Sep 2025")
        + badge("Completed Simulation", "status")
        + '</div>'
        '<h3>GenAI Enterprise Simulation</h3>'
        '<p class="prose">Completed practical corporate simulation covering automated financial data extraction, Python data modeling, and conversational assistant prototyping with LLMs.</p>'
        '<p class="meta">Forage job simulation certificate; this does not represent direct employment with BCG X.</p>'
        '<div class="card-actions">'
        + link("https://drive.google.com/file/d/1VZPcWKt4f5I_vRD8REPQYADvNDZ_WsIL/view", "View Forage Certificate ↗", "button button-small", external=True)
        + '</div>'
        '</article>'
        '<article class="card">'
        '<div class="card-top">'
        + eyebrow("Talerang & Cloudwrk · 2025")
        + badge("Completed Program", "status")
        + '</div>'
        '<h3>Coding-Track Micro-Internship</h3>'
        '<p class="prose">Completed the Talerang coding-track career-readiness micro-internship in association with Cloudwrk. The certificate records a PASS grade and does not establish direct Cloudwrk employment or a delivered client software project.</p>'
        '<p class="meta">Verified by Talerang Certificate of Completion (Grade: PASS).</p>'
        '<div class="card-actions">'
        + link("https://drive.google.com/file/d/1SDGQMPSTE_5jUZa7LCSEt7mX60VeqxhH/view", "View Completion Certificate ↗", "button button-small", external=True)
        + '</div>'
        + '</article>'
        + '</div>',
    )
    + section(
        "Additional Appointment-Only Virtual Offers",
        '<p class="section-lead">These records document appointment offers for exploratory or virtual learning programs. They are not represented as completed commercial internships, and no completion certificate is claimed.</p>'
        '<div class="grid three appointment-offers-grid">'
        '<article class="card offer-card">'
        + eyebrow("Zaalima Development · Jun 2025")
        + badge("Appointment Offer Only", "status")
        + '<h3>Data Science &amp; Machine Learning</h3>'
        '<p class="meta">Offer Date: 24 Jun 2025 · Term: 25 Jun–25 Sep 2025</p>'
        '<p class="prose-small">Virtual program appointment offer for data science and machine learning tasks. Preserved as an appointment record; commercial completion certificate not claimed.</p>'
        '<div class="card-actions">'
        + link("assets/documents/appointment-only-offers/zaalima-development-offer.pdf", "View Appointment Offer ↗", "button button-small button-quiet", external=True)
        + '</div>'
        + '</article>'
        '<article class="card offer-card">'
        + eyebrow("CodSoft · Nov 2024")
        + badge("Appointment Offer Only", "status")
        + '<h3>Artificial Intelligence Virtual Intern</h3>'
        '<p class="meta">Offer Date: 18 Nov 2024</p>'
        '<p class="prose-small">Virtual educational internship offer letter covering foundational AI tasks (4 weeks, Nov–Dec 2024). Preserved as an exploratory appointment record.</p>'
        '<div class="card-actions">'
        + link("assets/documents/appointment-only-offers/codsoft-ai-internship-offer.pdf", "View Appointment Offer ↗", "button button-small button-quiet", external=True)
        + '</div>'
        + '</article>'
        '<article class="card offer-card">'
        + eyebrow("CodeAlpha · Nov 2024")
        + badge("Appointment Offer Only", "status")
        + '<h3>Artificial Intelligence Internship</h3>'
        '<p class="meta">Offer Date: 15 Nov 2024</p>'
        '<p class="prose-small">Selection and offer confirmation for a 1-month virtual AI learning track (Dec 2024). Maintained as an exploratory learning appointment record.</p>'
        '<div class="card-actions">'
        + link("assets/documents/appointment-only-offers/codealpha-ai-internship-offer.pdf", "View Appointment Offer ↗", "button button-small button-quiet", external=True)
        + '</div>'
        + '</article>'
        '<article class="card offer-card">'
        + eyebrow("TechnoHacks Solutions · Aug 2025")
        + badge("Appointment Offer Only", "status")
        + '<h3>Machine Learning Intern</h3>'
        '<p class="meta">Offer Date: 07 Aug 2025</p>'
        '<p class="prose-small">Offer letter for a 1-month remote Machine Learning virtual program. Documented as an appointment offer only; completion certificate not claimed.</p>'
        '<div class="card-actions">'
        + link("assets/documents/appointment-only-offers/technohacks-ml-internship-offer.pdf", "View Appointment Offer ↗", "button button-small button-quiet", external=True)
        + '</div>'
        + '</article>'
        '<article class="card offer-card">'
        + eyebrow("Prodigy InfoTech · Aug 2026")
        + badge("Appointment Offer Only", "status")
        + '<h3>Generative AI Intern</h3>'
        '<p class="meta">Offer Date: 14 Aug 2026</p>'
        '<p class="prose-small">Educational virtual internship appointment offer (1-month term: Aug–Sep 2026). Documented strictly as an appointment offer only.</p>'
        '<div class="card-actions">'
        + link("assets/documents/appointment-only-offers/prodigy-infotech-generative-ai-offer.pdf", "View Appointment Offer ↗", "button button-small button-quiet", external=True)
        + '</div>'
        + '</article>'
        '</div>',
    )
    + explore_more("experience.html"),
)

# 4. ADVICTION: advfiction.html
PAGES["advfiction.html"] = (
    "Advfiction",
    "Rehan Memon | Advfiction Experience",
    "Two concurrent engineering tracks at Advfiction: Full-Stack Web Development and AI Workflow Automation.",
    intro(
        "Experience / Advfiction Private Limited",
        "Two Concurrent Engineering Workstreams",
        "Apr–Sep 2026 · Two concurrent engineering workstreams across Web Development and AI Automation. Fully verified by primary documents: original offer letters (28 & 29 Apr 2026), official 2-month extension letters (27 Jul 2026 extending appointment through 30 Sep 2026), 22-week completion certificates (issued 1 Oct 2026), and a joint Letter of Recommendation (issued 6 Oct 2026 by MD Rojer R V).",
        "experience.html",
        "Commercial Experience",
    )
    + section(
        "Concurrent Engineering Tracks",
        '<div class="grid two track-comparison">'
        '<article class="card track-card" id="web-track">'
        + eyebrow("Track 1 · Web Development")
        + '<h3>Interface & API Engineering</h3>'
        '<p>Collaborated with the web engineering team on core platforms:</p>'
        '<ul class="prose-list">'
        '<li><strong>Advfiction Enterprise Lead LMS (<a class="text-link" href="client-work.html#advfiction-lms">Case Study</a>):</strong> Contributed a Node/Express public lead endpoint with required-field and email-format checks and Supabase PostgreSQL insertion.</li>'
        '<li><strong>Cross-origin access:</strong> Configured an allowed-origin CORS list for the Vercel-hosted frontends and Render backend. CORS controls browser access; it does not authenticate visitors.</li>'
        '<li><strong>Corporate Website Revamp (<a class="text-link" href="client-work.html#advfiction-website">Live Deployment</a>):</strong> Built responsive UI components and hooked contact forms directly into the backend lead pipeline. Live at <a class="text-link" href="https://advfiction.vercel.app/" target="_blank" rel="noopener noreferrer">advfiction.vercel.app ↗</a>.</li>'
        '</ul>'
        '<div class="card-actions">'
        + link("https://drive.google.com/file/d/1Q_zS8HQjH03CE4nwsZyvVjkP3t1EI6hn/view", "View Web Dev Certificate (PDF) ↗", "button button-small", external=True)
        + link("client-work.html#advfiction-lms", "Inspect LMS Client Deployment →", "button button-small button-quiet")
        + link("https://advfiction.vercel.app/", "Corporate Site ↗", "button button-small button-quiet", external=True)
        + '</div>'
        '</article>'
        '<article class="card track-card" id="automation-track">'
        + eyebrow("Track 2 · AI & Automation")
        + '<h3>n8n Workflow Orchestration</h3>'
        '<p>Worked with n8n canvases and API integrations during the automation track. The linked examples separate visible editor tests from designs:</p>'
        '<ul class="prose-list">'
        '<li><strong>Map-Based Scraping:</strong> An Apify-to-Sheets canvas shows a completed editor run for five items.</li>'
        '<li><strong>Company Research:</strong> A PostgreSQL/search canvas shows partial execution; downstream AI and save steps are not shown completing.</li>'
        '<li><strong>Lead Brief Design:</strong> Sheet-to-Google-Docs/PDF canvases show a configured route, without proof of document delivery.</li>'
        '<li><strong>Other Designs:</strong> Published editor captures show scheduled publishing, Telegram review and AI-assisted content stages; live use is unverified.</li>'
        '</ul>'
        '<div class="card-actions">'
        + link("https://drive.google.com/file/d/1T_3ZDXAFRpxJ6-GDZAkyCPVchJdR7815/view", "View AI Automation Certificate (PDF) ↗", "button button-small", external=True)
        + link("automation.html", "Explore All 10 Workflow Architectures →", "button button-small button-quiet")
        + link("automation.html#wf-maps-scraper", "View Editor Execution Evidence →", "button button-small button-quiet")
        + '</div>'
        '</article>'
        '</div>',
    )
    + section(
        "Executive Recommendation & Formal Extensions",
        '<div class="grid two track-comparison">'
        '<article class="card track-card" id="adv-lor">'
        + eyebrow("Executive Recommendation")
        + '<h3>Joint Letter of Recommendation</h3>'
        '<p>Official executive recommendation issued on 6 October 2026 by Managing Director Rojer R V, commending performance, technical adaptability, and collaborative contributions across both AI Automation and Web Development.</p>'
        '<div class="card-actions">'
        + link("https://drive.google.com/file/d/1r2tEKiVldHHaL94S_brIEPRVAwsiNRxM/view", "Inspect Joint Executive LOR ↗", "button button-small", external=True)
        + '</div>'
        '</article>'
        '<article class="card track-card" id="adv-extensions">'
        + eyebrow("Appointment & Extension Records")
        + '<h3>Documented Contract Extensions</h3>'
        '<p>Both original appointments were formally extended by 2 additional months via official extension letters dated 27 July 2026:</p>'
        '<div class="card-actions">'
        + link("https://drive.google.com/file/d/1MYa4I3-lCY0-il1lshM9f4XZnYcYDNHZ/view", "Web Dev Extension Letter ↗", "button button-small button-quiet", external=True)
        + link("https://drive.google.com/file/d/1U4sEjk5fpLDao0W--VYgmBtSW0bC__VT/view", "AI Extension Letter ↗", "button button-small button-quiet", external=True)
        + '</div>'
        '<p class="meta" style="margin-top: 0.75rem;">Original AI Automation offer letter (<code>19y3Fa9zD8zqbLnZPS86rt8R5bQopky8A</code>) is safely withheld from public links under formal confidentiality obligations.</p>'
        '</article>'
        '</div>',
    )
    + section(
        "Client Boundary & Workstream Integrity",
        '<div class="prose">'
        '<p><strong>Important Clarification on Project Attribution:</strong></p>'
        '<ul class="prose-list">'
        '<li><strong>Advfiction Engagements:</strong> Advfiction work was strictly divided into the internal Enterprise Lead LMS and the Advfiction Corporate Website Revamp, alongside internal n8n automation pipelines.</li>'
        '<li><strong>Independent Client Work:</strong> External projects such as the <em>LMS Girls Higher Secondary School Portal</em> and <em>Marthandam Star Honey Platform</em> were delivered as separate independent client deployments and are not corporate properties of Advfiction.</li>'
        '<li><strong>Personal Portfolio:</strong> This personal engineering portfolio is an independent open-source publication and is not classified as commercial client work.</li>'
        '</ul>'
        '</div>',
    )
    + section(
        "Technologies Across Both Workstreams",
        '<div class="tags-row">'
        + "".join(f'<span class="tag">{escape(t)}</span>' for t in ["Node.js", "Express", "Supabase", "PostgreSQL", "n8n", "Apify Actors", "REST API", "Vercel", "Render", "Google Sheets API"])
        + '</div>',
    )
    + explore_more("advfiction.html"),
)

# 5. ALGODEVPOSS: algodevopss.html
PAGES["algodevopss.html"] = (
    "AlgoDevOpss",
    "Rehan Memon | AlgoDevOpss Experience",
    "Next.js and TypeScript departmental portal development during the AlgoDevOpss internship.",
    intro(
        "Experience / AlgoDevOpss",
        "Departmental Web Portal Engineering",
        "Full-Stack Development Intern · May–August 2026 (Certified Term). Certified appointment: 01 May 2026 to 31 August 2026; informal extension through December 2026 (in progress as of November 2026; formal extension letter pending). Engineering production routes and data modules for the KJSIEIT EXTC academic platform.",
        "experience.html",
        "Commercial Experience",
    )
    + section(
        "Verified Primary Credential & Governance",
        '<div class="grid two track-comparison">'
        '<article class="card track-card" id="algo-completion-certs">'
        + eyebrow("Official Completion Certificate")
        + '<h3>Full-Stack Development Certification</h3>'
        '<p>Certified completion record issued on 31 August 2026 by Founder Yash Balotiya (Udyam: UDYAM-MH-18-0511641) covering Full-Stack Web Development (MERN / Next.js / Machine Learning):</p>'
        '<div class="card-actions">'
        + link("https://drive.google.com/file/d/1yZyBwiDStZatvvD9oj5rlM1WUTBkz9BV/view", "View Full-Stack Certificate (PDF) ↗", "button button-small", external=True)
        + '</div>'
        '<p class="meta" style="margin-top: 0.75rem;">Documented term: 01 May 2026 – 31 August 2026. Continuation communicated through December 2026 (in progress as of November 2026; formal extension letter pending from employer).</p>'
        '</article>'
        '<article class="card track-card" id="algo-privacy-governance">'
        + eyebrow("Document Privacy Governance")
        + '<h3>Sensitive Data Protection Notice</h3>'
        '<p>The original appointment letter (dated 26 April 2026) is withheld from public web links to protect sensitive personal Government identification (Aadhaar number). Certified completion credentials and documented project modules are provided as public proof.</p>'
        '</article>'
        '</div>',
    )
    + section(
        "KJSIEIT EXTC Platform Engineering",
        '<div class="prose">'
        '<p>Contributed as part of a collaborative engineering team to the departmental web portal for the Electronics & Telecommunication Engineering (EXTC) department at K. J. Somaiya Institute of Engineering & Information Technology (KJSIEIT).</p>'
        '<p><strong>Key Technical Contributions:</strong></p>'
        '<ul class="prose-list">'
        '<li><strong>Pedagogy Route:</strong> Developed the dedicated departmental pedagogy showcase route in Next.js and TypeScript, presenting instructional frameworks and lab coursework.</li>'
        '<li><strong>Result Analysis System:</strong> Engineered the typed <code>results-data.ts</code> data transformation module and interactive examination performance dashboard.</li>'
        '<li><strong>Modular Components:</strong> Integrated reusable institutional navigation headers, typed data cards, and responsive tables.</li>'
        '</ul>'
        '</div>',
    )
    + section(
        "CMS & Administration Prototyping",
        '<div class="prose">'
        '<p>Researched and prototyped modular administrative panels for dynamic department updates, exploring database-backed content management workflows and role-based access schemas.</p>'
        '</div>',
    )
    + section(
        "Technical Stack Deployed",
        '<div class="tags-row">'
        + "".join(f'<span class="tag">{escape(t)}</span>' for t in ["Next.js", "React", "TypeScript", "Tailwind CSS", "Data Structures", "Component Design"])
        + '</div>',
    )
    + explore_more("algodevopss.html"),
)

# 6. AWAREWOLF: awarewolf.html
PAGES["awarewolf.html"] = (
    "AwareWolf",
    "Rehan Memon | AwareWolf Experience",
    "Software engineering and generative AI evaluation for media workflows at AwareWolf: React/FastAPI storyboards, image ingestion, FFmpeg diagnostics, and video model evaluation.",
    intro(
        "Experience / AwareWolf",
        "Media Workflows, Persistence & AI Evaluation",
        "Content Operating System Intern · Sep 2026–Present (Engineering Pause Reported Nov 2026) · Offer Term: 17 Sep 2026–16 Mar 2027 · Remote · Paid Internship. Software development for media workflow prototyping and generative-video evaluation, spanning interactive React/TypeScript storyboards, FastAPI APIs, media validation pipelines, FFmpeg stream diagnostics, and video model benchmarking.",
        "experience.html",
        "Commercial Experience",
    )
    + section(
        "Appointment Verification & Status",
        '<div class="grid two track-comparison">'
        '<article class="card track-card" id="awarewolf-offer">'
        + eyebrow("Official Appointment Document")
        + '<h3>Appointment Offer Letter</h3>'
        '<p>Formal appointment offer letter for the 6-month Content Operating System internship (Term: 17 September 2026 to 16 March 2027):</p>'
        '<div class="card-actions">'
        + link("https://drive.google.com/file/d/1pShS64xWmhduHrJyiORbXDGBBXuKAnjc/view", "View Appointment Offer Letter (PDF) ↗", "button button-small", external=True)
        + '</div>'
        '</article>'
        '<article class="card track-card" id="awarewolf-status">'
        + eyebrow("Engagement Status & Confidentiality")
        + '<h3>Confidentiality & Workstream Status</h3>'
        '<p>Operated under formal Non-Disclosure Agreement (NDA) and Information Security obligations. Active development sprints were paused in November 2026.</p>'
        '</article>'
        '</div>',
    )
    + section(
        "Media Library & Five-Scene Storyboard Pilot",
        '<div class="prose">'
        '<p>Contributed to development and validation of a full-stack media management pilot built with <strong>React, TypeScript, and FastAPI</strong>, designed to help content teams organize approved media and prepare editable storyboards:</p>'
        '<ul class="prose-list">'
        '<li><strong>Deterministic Retrieval & Browsing:</strong> Connected immutable metadata catalogs with deterministic lexical search, category browsing, and explicit asset selection across approved media units.</li>'
        '<li><strong>Authenticated Media Previews:</strong> Engineered browser video and photo preview handlers decoding 7 photo previews and 3 distinct video streams returning HTTP 206 Partial Content byte-range responses for smooth timeline scrubbing.</li>'
        '<li><strong>Five-Scene Storyboard Editor:</strong> Implemented responsive scene organization allowing real-time timeline sequencing, media replacement, and bounded start/end trimming.</li>'
        '<li><strong>Revisioned Atomic Persistence:</strong> Built owner-scoped JSON board persistence with revision tokens and atomic write guarantees, verified through save/refresh/reopen cycles and two-tab HTTP 409 conflict detection protecting unsaved local edits.</li>'
        '<li><strong>Validation Snapshot:</strong> The verified pilot snapshot passed <strong>263 backend tests</strong> and <strong>27 frontend tests</strong>, alongside successful local builds (<code>build:jsonl</code> and <code>build:legacy</code>) and multi-viewport responsive checks (390px to 1512px).</li>'
        '</ul>'
        '</div>',
    )
    + section(
        "Validated Image Ingestion Service",
        '<div class="prose">'
        '<p>Engineered a reusable, resilient image-import service ensuring incoming JPEG and PNG assets comply with strict platform specifications:</p>'
        '<ul class="prose-list">'
        '<li><strong>Pillow Format & Geometry Validation:</strong> Enforced file integrity checks, format verification, and safety limits (10 MiB file cap, 40 million decoded pixels, and 8,192-pixel edge maximum).</li>'
        '<li><strong>Content-Addressed Identity:</strong> Derived unique asset identities from SHA-256 byte hashes, using exclusive file destination creation to prevent filesystem races.</li>'
        '<li><strong>Concurrency & Duplicate Protection:</strong> Implemented database integrity constraints to handle duplicate uploads. Verified through <strong>7 focused integration tests</strong>, including three simultaneous identical uploads resolving cleanly to a single unique database record.</li>'
        '</ul>'
        '</div>',
    )
    + section(
        "FFmpeg Renderer & API Diagnostics",
        '<div class="prose">'
        '<p>Investigated complex stream synchronization, process lifecycle, and API consistency issues within automated rendering pipelines:</p>'
        '<ul class="prose-list">'
        '<li><strong>Audio/Video Stream Synchronization:</strong> Traced a critical rendering defect where an exported MP4 showed a 15-second video stream alongside a 38.5-second audio track. Root-caused the mismatch to incorrect catalog durations and harness trim field discrepancies.</li>'
        '<li><strong>Targeted Remediation:</strong> Authored targeted fixes and validation checks resulting in a corrected 5-scene, 29-second reproduction verified with matching streams and clean decoder exit.</li>'
        '<li><strong>API & Persistence Reconciliation:</strong> Traced UI polling failures, missing route handlers, and stale process port conflicts, verifying stability across a 57-test regression snapshot.</li>'
        '</ul>'
        '</div>',
    )
    + section(
        "Generative-Video Evaluation",
        '<div class="prose">'
        '<p>Conducted a controlled, objective benchmark of six generative-video routes using a unified visual brief to evaluate technical delivery, motion quality, hardware constraints, and production economics:</p>'
        '<ul class="prose-list">'
        '<li><strong>Open-Model Inference on Kaggle:</strong> Executed hands-on inference experiments with open-weights models. Successfully ran the Wan model on Kaggle T4 hardware (5.06-second clip at 480×832 in 55.37 minutes, utilizing 12.73 GB peak GPU memory).</li>'
        '<li><strong>Hardware Limit Documentation:</strong> Documented exact CUDA memory boundaries and BF16 constraints, capturing failure bounds such as Hunyuan requesting a 43.28 GB block against available 14.56 GB T4 VRAM.</li>'
        '<li><strong>Hosted Route Comparisons:</strong> Evaluated outputs across commercial hosted endpoints (Flow, Hailuo, Adobe-hosted Veo, PixVerse, LTX), comparing prompt adherence, camera motion fidelity, and cost per usable shot.</li>'
        '</ul>'
        '</div>',
    )
    + section(
        "Architecture Research & Feasibility",
        '<div class="prose">'
        '<p>Contributed to architectural feasibility studies and proof-of-concept integrations:</p>'
        '<ul class="prose-list">'
        '<li><strong>Architecture Decision Report:</strong> Contributed research across a 25-page report analyzing publishing APIs, Google Photos Picker acquisition, stable asset identity, and portable storage options.</li>'
        '<li><strong>Buffer Publishing Experiment:</strong> Built connection testing and adapter modules to validate remote draft generation, observing a text-only X draft in Buffer\'s remote interface.</li>'
        '</ul>'
        '</div>',
    )
    + section(
        "Technical Stack Deployed",
        '<div class="tags-row">'
        + "".join(f'<span class="tag">{escape(t)}</span>' for t in [
            "Python", "FastAPI", "TypeScript", "React", "Vite", "SQLite", "JSONL",
            "FFmpeg", "FFprobe", "Pillow", "pytest", "REST APIs", "HTTP 206 Byte Ranges",
            "Kaggle", "Hugging Face", "Generative AI Evaluation"
        ])
        + '</div>',
    )
    + explore_more("awarewolf.html"),
)

# 7. PROJECTS: projects.html
PAGES["projects.html"] = (
    "Projects",
    "Rehan Memon | Projects & Case Studies",
    "A curated portfolio of 14 projects spanning AI engineering, client systems, and workflow automation.",
    intro(
        "Selected Work",
        "Projects & Case Studies",
        "A curated portfolio of 14 projects spanning AI engineering, client systems, and workflow automation.",
        css_class="page-intro-compact",
    )
    + '<section class="section section-directory-tools container">'
    '<div class="filter-pills" role="group" aria-label="Filter projects by engineering pillar">'
    '<button type="button" class="filter-pill" data-filter-pillar-button="AI & Machine Learning Systems" aria-pressed="false" aria-controls="projectResults">1. AI & Machine Learning Systems (5)</button>'
    '<button type="button" class="filter-pill" data-filter-pillar-button="Client & Collaborative Engineering" aria-pressed="false" aria-controls="projectResults">2. Client & Collaborative Engineering (5)</button>'
    '<button type="button" class="filter-pill" data-filter-pillar-button="AI & Workflow Automation" aria-pressed="false" aria-controls="projectResults">3. AI & Workflow Automation (4)</button>'
    '</div>'
    '<div class="filter-bar">'
    '<label for="projectSearch">Search all 14 projects</label>'
    '<input id="projectSearch" type="search" placeholder="Search by name, technique, tool..." data-filter-search>'
    '<label for="projectPillar">Filter by Pillar</label>'
    '<select id="projectPillar" data-filter-pillar>'
    '<option value="">All Pillars (14 Projects)</option>'
    '<option>AI & Machine Learning Systems</option>'
    '<option>Client & Collaborative Engineering</option>'
    '<option>AI & Workflow Automation</option>'
    '</select>'
    '</div>'
    '<p class="filter-count" data-filter-count role="status" aria-live="polite" aria-atomic="true">14 projects shown</p>'
    '</section>'
    '<div id="projectResults" data-filter-list data-noun-singular="project" data-noun-plural="projects">'
    + section(
        "Pillar 1: AI & Machine Learning Systems",
        '<p class="section-lead">Algorithmic baselines evaluated under rigorous evaluation protocols, real-time ASGI distributed architectures, and reproducible benchmarks.</p>'
        '<div class="grid two">'
        + "".join(project_card(p) for p in PROJECTS if p["pillar"] == "AI & Machine Learning Systems")
        + '</div>',
        "pillar-ai",
        'data-pillar-section',
    )
    + section(
        "Pillar 2: Client & Collaborative Engineering",
        '<p class="section-lead">Client platforms, interactive web interfaces, and collaborative API endpoints developed for organizations and educational partners.</p>'
        '<div class="grid two">'
        + "".join(project_card(p) for p in PROJECTS if p["pillar"] == "Client & Collaborative Engineering")
        + '</div>'
        '<p class="section-end">' + link("client-work.html", "Explore In-Depth Client Deployments & Architecture →") + '</p>',
        "pillar-client",
        'data-pillar-section',
    )
    + section(
        "Pillar 3: AI & Workflow Automation Systems",
        '<p class="section-lead">Autonomous local-first Python job discovery alongside 10 selected n8n workflow architectures covering map data capture, research enrichment, and document generation.</p>'
        '<div class="grid two">'
        + "".join(project_card(p) for p in PROJECTS if p["pillar"] == "AI & Workflow Automation")
        + '</div>'
        '<div class="section-nav-group">'
        + link("automation.html", "Explore All 10 Workflow Architectures →", "button")
        + '<div class="sub-nav-links">'
        + link("automation.html#wf-maps-scraper", "View Editor Execution Evidence →")
        + '</div>'
        + '</div>',
        "pillar-automation",
        'data-pillar-section',
    )
    + '<section class="container"><p class="no-results" data-no-results hidden>No projects match your filter criteria.</p></section>'
    '</div>'
    + explore_more("projects.html"),
)

# 8. SIGNATURE VERIFICATION: signature-verification.html
PAGES["signature-verification.html"] = (
    "Signature Verification AI",
    "Rehan Memon | Signature Verification AI",
    "Offline handwritten signature verification with OpenCV preprocessing, 331 handcrafted features, and RBF SVM classification.",
    intro(
        "Pillar 1 · AI & Machine Learning Systems",
        "Signature Verification AI",
        "A classical computer vision pipeline engineered to distinguish authentic signatures from skilled forgeries through geometric, statistical, and contour feature extraction.",
        "projects.html#pillar-ai",
        "Pillar 1: AI & Machine Learning Systems",
    )
    + section(
        "Pipeline Architecture",
        '<p class="prose">The verification pipeline executes a multi-stage image processing sequence engineered to standardize scan variations and isolate ink strokes:</p>'
        '<figure class="diagram">'
        '<img src="diagrams/signature-pipeline.svg" width="1000" height="172" loading="lazy" alt="Preprocessing, 331-dimensional feature extraction, and SVM classification. The API does not return a probability score.">'
        '<figcaption>Inference flow: grayscale conversion, Gaussian denoising, Otsu thresholding, contour cropping, 331 handcrafted features, and RBF SVM classification.</figcaption>'
        '</figure>'
        '<ol class="flow">'
        + case_row("1. OpenCV Preprocessing", "Converts images to grayscale, applies Gaussian blur and Otsu thresholding, then finds contours to crop the signature area.")
        + case_row("2. Geometric Normalization", "Calculates the signature bounding envelope and resizes the binary mask to standardized dimensions while preserving stroke aspect ratios.")
        + case_row("3. Feature Extraction (331-D)", "Combines aspect ratio, normalized bounding-box area and global ink density (3), a 16×16 local density grid (256), horizontal and vertical projections (64), contour count (1), and Hu moments (7).")
        + case_row("4. SVM Classification", "Projects extracted feature vectors into an RBF-kernel Support Vector Machine (SVM) trained under a writer-disjoint split protocol to detect genuine vs forged specimens.")
        + case_row("5. FastAPI & Demo Interface", "Exposes inference through FastAPI and a React interface for image upload, preview, and preprocessing visualization. The API returns a class label without a calibrated confidence probability.")
        + '</ol>',
    )
    + section(
        "Evaluation & Empirical Results",
        '<div class="prose">'
        '<p>To prevent data leakage, the feature extraction and classification pipeline was evaluated under a strict <strong>writer-disjoint validation protocol</strong> on the benchmark CEDAR signature dataset, ensuring the test split contains signatures from authors never seen during model training.</p>'
        '<div class="table-container" style="overflow-x: auto; margin: var(--space-md) 0;">'
        '<table class="data-table" style="width: 100%; border-collapse: collapse; text-align: left; font-size: var(--text-sm);">'
        '<thead>'
        '<tr style="border-bottom: 2px solid var(--border); color: var(--text-muted);">'
        '<th style="padding: 0.6rem 0.8rem;">Evaluation Metric</th>'
        '<th style="padding: 0.6rem 0.8rem;">Verified Baseline</th>'
        '<th style="padding: 0.6rem 0.8rem;">Benchmark & Protocol Details</th>'
        '</tr>'
        '</thead>'
        '<tbody>'
        '<tr style="border-bottom: 1px solid var(--border);">'
        '<td style="padding: 0.6rem 0.8rem; font-weight: 600;">Overall Accuracy</td>'
        '<td style="padding: 0.6rem 0.8rem; color: var(--accent); font-weight: 600;">65.91%</td>'
        '<td style="padding: 0.6rem 0.8rem;">CEDAR dataset writer-disjoint split (RBF-SVM, C=10.0, gamma=scale)</td>'
        '</tr>'
        '<tr style="border-bottom: 1px solid var(--border);">'
        '<td style="padding: 0.6rem 0.8rem; font-weight: 600;">Precision (Genuine)</td>'
        '<td style="padding: 0.6rem 0.8rem; color: var(--accent); font-weight: 600;">72.11%</td>'
        '<td style="padding: 0.6rem 0.8rem;">Low false-acceptance rate for authentic business signatures</td>'
        '</tr>'
        '<tr style="border-bottom: 1px solid var(--border);">'
        '<td style="padding: 0.6rem 0.8rem; font-weight: 600;">Recall (Sensitivity)</td>'
        '<td style="padding: 0.6rem 0.8rem; color: var(--accent); font-weight: 600;">51.89%</td>'
        '<td style="padding: 0.6rem 0.8rem;">Conservative rejection threshold against skilled forgeries</td>'
        '</tr>'
        '<tr>'
        '<td style="padding: 0.6rem 0.8rem; font-weight: 600;">F1-Score (Harmonic Mean)</td>'
        '<td style="padding: 0.6rem 0.8rem; color: var(--accent); font-weight: 600;">60.35%</td>'
        '<td style="padding: 0.6rem 0.8rem;">Balanced harmonic mean across 331 handcrafted geometric & texture features</td>'
        '</tr>'
        '</tbody>'
        '</table>'
        '</div>'
        '<p class="meta">Baseline evaluated with StandardScaler normalization and RBF-kernel SVM on CEDAR benchmark pairs.</p>'
        '</div>'
        '<div class="actions">'
        + link(SIGNATURE, "View GitHub Repository ↗", "button", external=True)
        + link("projects.html#pillar-ai", "Explore other AI projects →", "button button-quiet")
        + '</div>',
    )
    + explore_more("signature-verification.html"),
)

# 9. AI RESEARCH ASSISTANT: ai-research-assistant.html
PAGES["ai-research-assistant.html"] = (
    "AI Research Assistant",
    "Rehan Memon | AI Research Assistant",
    "Document question-answering prototype featuring token-aware chunking, Chroma dense indexing, retrieval, and source citation mapping.",
    intro(
        "Pillar 1 · AI & Machine Learning Systems",
        "AI Research Assistant",
        "An in-development retrieval-augmented generation (RAG) prototype that indexes documents in Chroma and maps answer citations to retrieved source metadata. Answer faithfulness has not been independently evaluated.",
        "projects.html#pillar-ai",
        "Pillar 1: AI & Machine Learning Systems",
    )
    + section(
        "RAG Ingestion & Retrieval Pipeline",
        '<p class="prose">The system operates as an end-to-end Python microservice orchestrating document parsing, token-aware chunking, vector embedding, and similarity search:</p>'
        '<figure class="diagram">'
        '<img src="diagrams/research-pipeline.svg" width="1000" height="172" loading="lazy" alt="Document ingestion, token-aware chunking, Chroma vector embedding, similarity search, prompt synthesis with source citations.">'
        '<figcaption>RAG processing sequence: document ingestion, token-aware chunking, dense vector indexing in Chroma, retrieval, and answer generation with source citation mapping.</figcaption>'
        '</figure>'
        '<ol class="flow">'
        + case_row("1. Document Ingestion", "Parses PDF, DOCX, and TXT documents and records source location metadata for retrieval.")
        + case_row("2. Token-Aware Chunking", "Uses token-aware chunks with a configured default of 700 tokens and 15% overlap; boundaries and metadata are preserved where available.")
        + case_row("3. Chroma Dense Indexing", "Generates dense mathematical embeddings for each chunk and indexes them into a persistent Chroma vector database collection.")
        + case_row("4. Similarity Retrieval", "Executes cosine distance search against indexed embeddings to retrieve the top-k most relevant text chunks for a given query.")
        + case_row("5. Answer and Citation Mapping", "Passes retrieved context to the answer generator and maps citation markers back to source metadata. Citation presence alone does not verify factual faithfulness.")
        + '</ol>',
    )
    + section(
        "Harness & Engineering Implementation",
        '<div class="prose">'
        '<p>Engineered with a clean Python service architecture: modular ingestion workers, decoupled vector storage abstractions, and a FastAPI harness exposing query and document upload endpoints.</p>'
        '</div>'
        '<div class="actions">'
        + link(RESEARCH, "View GitHub Repository ↗", "button", external=True)
        + link("projects.html#pillar-ai", "Explore other AI projects →", "button button-quiet")
        + '</div>',
    )
    + explore_more("ai-research-assistant.html"),
)

# 10. CONNECTHUB: connecthub.html
PAGES["connecthub.html"] = (
    "ConnectHub Messaging Engine",
    "Rehan Memon | ConnectHub Real-Time AI Messaging Engine",
    "Messaging prototype using FastAPI, async SQLAlchemy, Psycopg, PostgreSQL, WebSockets, Gemini room summaries, and room-scoped Python cosine search over JSONB embeddings.",
    intro(
        "Pillar 1 · AI & Machine Learning Systems",
        "ConnectHub — Real-Time AI Messaging Engine",
        "An in-development multi-room messaging application with FastAPI, PostgreSQL, WebSockets, Gemini-assisted summaries, and room-scoped semantic search.",
        "projects.html#pillar-ai",
        "Pillar 1: AI & Machine Learning Systems",
    )
    + section(
        "ASGI & Real-Time Pipeline",
        '<p class="prose">ConnectHub combines WebSocket connections, asynchronous relational persistence, AI summaries, and room-scoped semantic search in a modular application:</p>'
        '<figure class="diagram">'
        '<img src="diagrams/connecthub-pipeline.svg" width="1000" height="172" loading="lazy" alt="FastAPI handles room WebSockets and in-memory presence; async SQLAlchemy persists messages to PostgreSQL; Gemini supplies summaries; Python compares JSONB-stored embeddings within a room.">'
        '<figcaption>Current architecture: FastAPI, in-memory presence, PostgreSQL persistence, Gemini summaries, and room-scoped Python cosine search.</figcaption>'
        '</figure>'
        '<ol class="flow">'
        + case_row("1. FastAPI ASGI & PostgreSQL", "Uses FastAPI, Uvicorn, async SQLAlchemy sessions, Psycopg, and Alembic migrations. PostgreSQL stores the authoritative room and message records.")
        + case_row("2. WebSockets & Ephemeral In-Memory Presence", "Features a dedicated <code>/ws/{room_id}</code> connection manager maintaining active client socket sets per chat room. Dispatches real-time broadcast events, ephemeral typing indicators, read receipts, and member join/leave notifications with low-latency local socket dispatch.")
        + case_row("3. Relational Schema & Cascade Integrity", "Normalized relational schema modeling Users, Rooms, Memberships, Messages, and AI Summaries. Enforces foreign-key cascade deletes, compound uniqueness constraints, and B-tree compound indexing on <code>(room_id, created_at)</code> for optimized paginated history traversal.")
        + case_row("4. Gemini Room Summaries", "A request route gathers room history and calls Gemini to generate a catch-up summary. Embedding generation uses a background task; summary generation is not a separate durable worker.")
        + case_row("5. Room-Scoped Cosine Search", "Stores embedding arrays in PostgreSQL JSONB and compares them in Python within a room. No pgvector index or measured search latency is claimed.")
        + '</ol>',
    )
    + section(
        "Architectural Trade-offs & Deep Engineering Decisions",
        '<div class="prose">'
        '<div class="grid two">'
        '<div class="card">'
        '<h3>Single-Process In-Memory Presence</h3>'
        '<p><strong>Current design:</strong> Active sockets and presence are tracked in process memory. This supports the current single-process prototype.</p>'
        '<p><strong>Limit:</strong> A multi-worker deployment would require shared coordination and a separate design and test pass. No Redis adapter is implemented.</p>'
        '</div>'
        '<div class="card">'
        '<h3>JSONB Storage and Python Cosine Search</h3>'
        '<p><strong>Current design:</strong> Embedding arrays are stored in PostgreSQL JSONB and compared in Python for room-scoped search.</p>'
        '<p><strong>Limit:</strong> Search scale and latency have not been independently benchmarked. The implementation does not use pgvector or HNSW.</p>'
        '</div>'
        '</div>'
        '<div class="card" style="margin-top: 1.5rem;">'
        '<h3>Async Database Sessions</h3>'
        '<p>Uses SQLAlchemy <code>AsyncSession</code> for database operations. The project still requires load and failure testing before any concurrency or throughput claim.</p>'
        '</div>'
        '</div>',
    )
    + section(
        "Verification, Test Harness & Code Quality",
        '<div class="prose">'
        '<p>The system is verified by a multi-tiered automated test suite: <strong>97 backend unit and integration tests</strong> (FastAPI / pytest), <strong>21 frontend component tests</strong> (React / Vitest), and <strong>3 Playwright end-to-end integration scenarios</strong> covering real-time messaging, WebSocket room lifecycles, and database persistence. Test areas include:</p>'
        '<ul class="prose-list">'
        '<li><strong>Authentication &amp; Permissions:</strong> JWT creation, password hashing with bcrypt, token revocation, and role-based room access enforcement (Owner vs Member).</li>'
        '<li><strong>Message Dispatch &amp; Pagination:</strong> Validated message sequencing, database persistence, cursor-based pagination, and foreign-key integrity.</li>'
        '<li><strong>WebSocket Lifecycle:</strong> Connection handshake, room authorization, broadcast delivery, and clean disconnect state cleanup.</li>'
        '<li><strong>AI Error Handling:</strong> Mocked summary-service failures, token quota exhaustion, and room-scoped semantic search.</li>'
        '</ul>'
        '</div>'
        '<div class="actions">'
        + link("https://connecthub-web-w89e.onrender.com", "Live Application Demo ↗", "button", external=True)
        + link(CONNECT_HUB, "GitHub Repository ↗", "button button-quiet", external=True)
        + link("projects.html#pillar-ai", "Explore other AI projects →", "button button-quiet")
        + '</div>',
    )
    + explore_more("connecthub.html"),
)

# 11. AUTONOMOUS JOB SEARCH ENGINE: job-search-automation.html
PAGES["job-search-automation.html"] = (
    "Job Search Automation",
    "Rehan Memon | Autonomous Job Search Engine",
    "Local-first job discovery prototype with public-source adapters, a Schema.org parser, deterministic matching, Streamlit review, and a preparation-only safety boundary.",
    intro(
        "Pillar 3 · Workflow Automation",
        "Autonomous Job Search Engine",
        "A local-first job discovery prototype built with Python source adapters, deterministic matching, a Streamlit review interface, and preparation-only safety controls. Final applications remain manual.",
        "projects.html#pillar-automation",
        "Pillar 3: AI & Workflow Automation",
    )
    + section(
        "Autonomous Discovery & Ingestion Pipeline",
        '<p class="prose">The local pipeline can retrieve supported public listings, normalize and deduplicate them, score matches, and present opportunities for manual review. Scheduled unattended operation is not independently verified:</p>'
        '<figure class="diagram">'
        '<img src="diagrams/job-search-pipeline.svg" width="1000" height="172" loading="lazy" alt="Keyless public ATS collectors ingest job postings, deduplicate and normalize schemas, execute deterministic multi-criteria scoring, present ranked feeds in Streamlit, with strict preparation-only safety guardrails.">'
        '<figcaption>End-to-end automation sequence: keyless ATS ingestion, schema normalization, deterministic multi-factor scoring, Streamlit dashboard review, and preparation safety locks.</figcaption>'
        '</figure>'
        '<ol class="flow">'
        + case_row("1. Public-Source Ingestion", "Registered adapters cover Greenhouse, Lever, Ashby, Himalayas, Remotive, and Arbeitnow; a separate parser reads Schema.org structured data. Adzuna is a stub, not an operational connector. Live reliability varies by source and has not been established here.")
        + case_row("2. Schema Normalization & Deduplication", "Ingestion pipelines normalize disparate JSON response payloads into strongly-typed Python dataclasses. Generates deterministic SHA-256 fingerprint hashes across company, title, and location attributes to prevent duplicate records across recurring runs.")
        + case_row("3. Deterministic Multi-Factor Scoring", "Evaluates candidate resumes against normalized job requirements using rule-based algorithmic scoring: job title similarity, technical skill taxonomy extraction, minimum years of experience checks, and negative keyword filtering (security clearance, visa sponsorship exclusions).")
        + case_row("4. Streamlit Interactive Analytics Dashboard", "Rich, locally-hosted web interface providing real-time feed exploration, score threshold filters, keyword search, match score distribution histograms, and direct application preparation toolkits.")
        + case_row("5. Safety Guardrails & Preparation Hard-Lock", "Architecturally enforces a strict <code>PREPARATION_ONLY</code> boundary. Generates tailored cover letter drafts, interview talking points, and direct portal links, but explicitly forbids autonomous submission or bot-driven form filling, keeping human judgment in control.")
        + '</ol>',
    )
    + section(
        "Engineering Philosophy & Architectural Trade-offs",
        '<div class="prose">'
        '<div class="grid two">'
        '<div class="card">'
        '<h3>Source Adapters and Structured Data</h3>'
        '<p><strong>Current design:</strong> Source-specific adapters parse supported public feeds, while a separate Schema.org parser reads structured job data. Adzuna is present as a stub.</p>'
        '<p><strong>Limit:</strong> Connector registration and mocked tests do not establish live reliability, throughput, or support for every employer board.</p>'
        '</div>'
        '<div class="card">'
        '<h3>Deterministic Matching</h3>'
        '<p><strong>Decision:</strong> Built a multi-criteria deterministic scoring matrix in pure Python rather than passing every job description to an external commercial LLM.</p>'
        '<p><strong>Rationale:</strong> Rule-based scores can be inspected and tested without an external model call. Processing speed and live-source coverage require separate measurement.</p>'
        '</div>'
        '</div>'
        '<div class="card" style="margin-top: 1.5rem;" id="verification">'
        '<h3>Test Evidence and Operational Status</h3>'
        '<p>A current offline suite run collected 452 tests: <strong>450 passed, 1 failed, 1 skipped</strong>. The failure is an end-to-end deterministic-score threshold assertion (31.2 versus expected 50.0), which needs correction in that project before claiming a clean suite. The skipped test requires Windows symlink privilege. Mocked connector checks do not verify live scheduled ingestion.</p>'
        '</div>'
        '</div>'
        '<div class="actions">'
        + link("projects.html#pillar-automation", "View Project Overview →", "button")
        + link("projects.html#pillar-automation", "Explore Workflow Automation →", "button button-quiet")
        + '</div>',
    )
    + explore_more("job-search-automation.html"),
)

# 10. CLIENT WORK: client-work.html
PAGES["client-work.html"] = (
    "Client work",
    "Rehan Memon | Client Work",
    "Client and collaborative websites, administrative portals, API services, and labeled prototypes.",
    intro(
        "Pillar 2 · Client & Collaborative Engineering",
        "Client & Collaborative Engineering",
        "Selected websites, educational portals, API services, and prototypes. Each entry distinguishes a working public deployment from local source evidence and identifies the supported personal contribution.",
        "projects.html#pillar-client",
        "Pillar 2: Client & Collaborative Engineering",
    )
    + section(
        "Advfiction LMS (Lead Management System)",
        '<article class="card client-card" id="advfiction-lms">'
        '<div class="card-top">'
        + eyebrow("Advfiction Private Limited")
        + badge("Live Production Deployment")
        + '</div>'
        '<h3>Enterprise Lead Management System</h3>'
        '<p class="card-category-sub">Frontend Dashboard & Production REST API Service</p>'
        '<p>A complete full-stack lead management platform serving sales operations. Designed to intake, validate, and route candidate leads from public marketing channels into secure operational dashboards.</p>'
        '<div class="client-details">'
        '<h4>Technical Architecture & Personal Contribution:</h4>'
        '<ul class="prose-list">'
        '<li><strong>Production REST API:</strong> Collaborated on the Express/Node.js backend API hosted on Render, developing route input validation schemas and Supabase insertion routines for public lead capture.</li>'
        '<li><strong>CORS & Security Policies:</strong> Implemented multi-origin CORS configurations ensuring seamless communication between the Vercel-hosted frontend and Render backend services.</li>'
        '<li><strong>Supabase Integration:</strong> Structured database tables, foreign-key relationships, and service-role API queries.</li>'
        '<li><strong>Frontend Client:</strong> Built authenticated dashboard views with clean error handling and session validation.</li>'
        '</ul>'
        '</div>'
        '<div class="card-actions">'
        + link("https://advfiction-lms.vercel.app/pages/login.html", "Launch LMS Frontend ↗", "button button-small", external=True)
        + link("https://advfiction-lms-backend.onrender.com/api/health", "Live API Health Check ↗", "button button-small button-quiet", external=True)
        + link("advfiction.html", "View Internship Deep Dive →", "button button-small button-quiet")
        + '</div>'
        '</article>',
    )
    + section(
        "Advfiction Company Website",
        '<article class="card client-card" id="advfiction-website">'
        '<div class="card-top">'
        + eyebrow("Corporate Web Presence")
        + badge("Live Production Deployment")
        + '</div>'
        '<h3>Advfiction Corporate Website Revamp</h3>'
        '<p class="card-category-sub">Collaborative Corporate Web Platform · Vercel Deployment</p>'
        '<p>The primary digital front for Advfiction Private Limited, highlighting corporate consulting, engineering solutions, and client engagement tracks.</p>'
        '<div class="client-details">'
        '<h4>Technical Architecture & Personal Contribution:</h4>'
        '<ul class="prose-list">'
        '<li><strong>Responsive Design:</strong> Built cross-device responsive page layouts ensuring seamless presentation across desktop and mobile.</li>'
        '<li><strong>Contact Integration:</strong> Integrated frontend contact submission mechanisms with the central lead-intake infrastructure.</li>'
        '</ul>'
        '</div>'
        '<div class="card-actions">'
        + link("https://advfiction.vercel.app/", "Visit Live Website ↗", "button button-small", external=True)
        + link("advfiction.html", "View Internship Deep Dive →", "button button-small button-quiet")
        + '</div>'
        '</article>',
    )
    + section(
        "LMS Girls Higher Secondary School",
        '<article class="card client-card" id="girls-hss">'
        '<div class="card-top">'
        + eyebrow("Educational Web Platform · Independent Client")
        + badge("Live Platform Deployment")
        + '</div>'
        '<h3>Girls Higher Secondary School Institutional Portal & Admin Suite</h3>'
        '<p class="card-category-sub">Next.js 16 App Router · React 19 · TypeScript · Tailwind CSS · Supabase SSR</p>'
        '<p>A modern educational institution portal and administrative suite delivering server-rendered public pages and authenticated management workflows.</p>'
        '<div class="client-details">'
        '<h4>Technical Architecture & Engineering Deliverables:</h4>'
        '<ul class="prose-list">'
        '<li><strong>Administrative Management Suite:</strong> Engineered dedicated administrative modules for institutional news, event scheduling, faculty directories, photo galleries, and student achievement showcases using Next.js 16 App Router and React 19.</li>'
        '<li><strong>Supabase Data Layer:</strong> Integrated Supabase PostgreSQL tables and server-side queries (SSR) for robust data retrieval and secure content updates.</li>'
        '<li><strong>Responsive Design System:</strong> Architected responsive layouts styled with Tailwind CSS, ensuring clean viewing across mobile, tablet, and desktop viewports.</li>'
        '<li><strong>Inquiry Pipeline:</strong> Implemented public admission and general inquiry handling with direct database ingestion.</li>'
        '</ul>'
        '</div>'
        '<div class="card-actions">'
        + link("https://girlshss.netlify.app/", "Explore Live Platform ↗", "button button-small", external=True)
        + '</div>'
        '</article>',
    )
    + section(
        "Marthandam Star Honey",
        '<article class="card client-card" id="msh-honey">'
        '<div class="card-top">'
        + eyebrow("Commercial E-Commerce Platform · Independent Client")
        + badge("Live Client Deployment")
        + '</div>'
        '<h3>Marthandam Star Honey Commercial Showcase</h3>'
        '<p class="card-category-sub">React 19 · Vite · Tailwind CSS · Express Backend · Google Sheets API</p>'
        '<p>A specialized commercial e-commerce showcase and wholesale enquiry portal designed for honey product distribution.</p>'
        '<div class="client-details">'
        '<h4>Technical Architecture & Personal Contribution:</h4>'
        '<ul class="prose-list">'
        '<li><strong>Interactive Product Catalog:</strong> Built animated product showcase components with Framer Motion and Tailwind CSS, presenting product variants and nutritional profiles.</li>'
        '<li><strong>Enquiry Routing Service:</strong> The local source contains Express routes and a Google Sheets API controller for customer inquiries. The frontend source targets a localhost API; delivery from the public site has not been verified.</li>'
        '<li><strong>Validation & Feedback:</strong> Client-side phone/email checks are implemented; a successful live submission is not established.</li>'
        '</ul>'
        '</div>'
        '<div class="card-actions">'
        + link("https://msh-website.netlify.app/", "Explore Live Website ↗", "button button-small", external=True)
        + '</div>'
        '</article>',
    )
    + section(
        "SAHASH NGO Conversational Assistant",
        '<article class="card client-card" id="sahash-chatbot">'
        '<div class="card-top">'
        + eyebrow("NGO Assistant Prototype · ConnectFor / SAHASH India")
        + badge("Deployment Unverified")
        + '</div>'
        '<h3>SAHASH NGO Voice & Conversational Assistant</h3>'
        '<p class="card-category-sub">Node.js · Express · Google Gemini API · Keyword Retrieval · Web Speech API</p>'
        '<p>A conversational assistant prototype developed in the SAHASH India / ConnectFor context. Its local source contains FAQ and organization-data lookup, but production content and deployment have not been verified.</p>'
        '<div class="client-details">'
        '<h4>Technical Architecture & Personal Contribution:</h4>'
        '<ul class="prose-list">'
        '<li><strong>FAQ and Document Lookup:</strong> An in-memory cache scores organization documents by tokens and intents, then passes selected context to Gemini. The prompt includes cautious fallback instructions; factual faithfulness has not been evaluated.</li>'
        '<li><strong>Multimodal Voice & Text UI:</strong> Implemented a floating launcher with bidirectional speech synthesis and voice recognition via the browser Web Speech API.</li>'
        '<li><strong>Express Backend & Session Memory:</strong> Built modular API controllers with conversational context buffers and express rate-limiting middleware for abuse prevention.</li>'
        '</ul>'
        '</div>'
        '<div class="card-actions">'
        + link("projects.html#pillar-client", "View in Projects Catalog →", "button button-small button-quiet")
        + link("about.html", "Technical Skills Matrix →", "button button-small button-quiet")
        + '</div>'
        '</article>',
    )
    + explore_more("client-work.html"),
)

def workflow_image(filename, width, height, alt, caption):
    """Show an original editor capture with a caption and the shared lightbox."""
    return (
        '<figure class="evidence-figure workflow-capture">'
        f'<button type="button" class="image-zoom-trigger" aria-haspopup="dialog" aria-label="Enlarge image: {escape(alt)}">'
        f'<img src="assets/workflows/{escape(filename)}" width="{width}" height="{height}" loading="lazy" decoding="async" alt="{escape(alt)}">'
        '</button>'
        f'<figcaption class="evidence-caption">{escape(caption)}</figcaption>'
        '</figure>'
    )


# 11. AUTOMATION: automation.html (Unified Canonical n8n Architecture Page)

def workflow_index():
    return (
        '<section class="section section-directory-tools container" style="margin-bottom: var(--space-md);">'
        '<div class="workflow-index-box">'
        '<div class="workflow-index-header">'
        '<h2 class="workflow-index-heading">Workflow Architecture Index</h2>'
        '<p class="workflow-index-sub">Jump directly to any workflow architecture below:</p>'
        '</div>'
        '<div class="workflow-index-grid" role="navigation" aria-label="Workflow quick navigation">'
        '<div class="workflow-index-col">'
        '<a href="#wf-instagram-api" class="workflow-index-link"><span class="wf-num">01</span> Instagram Scheduled Publishing <span class="wf-status">Design</span></a>'
        '<a href="#wf-news-prompt" class="workflow-index-link"><span class="wf-num">02</span> News Sources to AI Summary <span class="wf-status">Design</span></a>'
        '<a href="#wf-social-publisher" class="workflow-index-link"><span class="wf-num">03</span> PostgreSQL to AI Social Publisher <span class="wf-status">Design</span></a>'
        '<a href="#wf-subworkflow-router" class="workflow-index-link"><span class="wf-num">04</span> AI Outreach &amp; Team Notification <span class="wf-status">Skeleton</span></a>'
        '<a href="#wf-social-orchestrator" class="workflow-index-link"><span class="wf-num">05</span> Caption to Image Asset <span class="wf-status">Design</span></a>'
        '</div>'
        '<div class="workflow-index-col">'
        '<a href="#wf-itinerary-proposal" class="workflow-index-link"><span class="wf-num">06</span> AI Itinerary &amp; PDF Proposal <span class="wf-status">Design</span></a>'
        '<a href="#wf-maps-scraper" class="workflow-index-link"><span class="wf-num">07</span> Apify Maps to Google Sheets <span class="wf-status">Editor run</span></a>'
        '<a href="#wf-lead-dossier" class="workflow-index-link"><span class="wf-num">08</span> Lead Row to PDF Brief <span class="wf-status">Design</span></a>'
        '<a href="#wf-postgres-research" class="workflow-index-link"><span class="wf-num">09</span> PostgreSQL Search &amp; AI Enrichment <span class="wf-status">Partial run</span></a>'
        '<a href="#wf-telegram-bot" class="workflow-index-link"><span class="wf-num">10</span> Telegram Review &amp; Approval <span class="wf-status">Design</span></a>'
        '</div>'
        '</div>'
        '</div>'
        '</section>'
    )


def evidence_status_legend():
    return (
        '<section class="section container" style="margin-bottom: var(--space-md);">'
        '<div class="workflow-index-box" style="padding: 1.25rem 1.5rem;">'
        '<h3 style="font-size: 1.05rem; margin: 0 0 0.5rem 0; color: var(--ink);">Evidence &amp; Verification Status Legend</h3>'
        '<p class="prose" style="font-size: 0.88rem; margin: 0 0 0.85rem 0; color: var(--muted);">'
        'Each architecture below reflects authentic internship engineering work and is classified by its verified evidence maturity:'
        '</p>'
        '<div class="workflow-index-grid" style="grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 0.75rem;">'
        '<div class="workflow-index-col" style="padding: 0.75rem;">'
        '<div style="margin-bottom: 0.35rem;">' + badge("Editor execution shown") + '</div>'
        '<p style="font-size: 0.82rem; margin: 0; color: var(--muted);">Live canvas runtime data flow with completed node execution indicators.</p>'
        '</div>'
        '<div class="workflow-index-col" style="padding: 0.75rem;">'
        '<div style="margin-bottom: 0.35rem;">' + badge("Partial execution shown") + '</div>'
        '<p style="font-size: 0.82rem; margin: 0; color: var(--muted);">Verified initial pipeline stages; downstream enrichment/persistence unrun.</p>'
        '</div>'
        '<div class="workflow-index-col" style="padding: 0.75rem;">'
        '<div style="margin-bottom: 0.35rem;">' + badge("Design/configuration only") + '</div>'
        '<p style="font-size: 0.82rem; margin: 0; color: var(--muted);">Complete node logic and schema configuration awaiting credentials/deployment.</p>'
        '</div>'
        '<div class="workflow-index-col" style="padding: 0.75rem;">'
        '<div style="margin-bottom: 0.35rem;">' + badge("Test harness or skeleton") + '</div>'
        '<p style="font-size: 0.82rem; margin: 0; color: var(--muted);">Validation harness engineered with mock lead payloads and routing templates.</p>'
        '</div>'
        '</div>'
        '</div>'
        '</section>'
    )


def workflow_example(number, anchor, category, status, title, purpose, business_value, engineering, tech_tags, evidence, images):
    tags_html = "".join(f'<span class="tag">{escape(t)}</span>' for t in tech_tags)
    body = (
        f'<article class="card evidence-card" id="{anchor}">'
        f'<div class="card-top">{eyebrow(f"Portfolio Order {number:02d} · {category}")}{badge(status)}</div>'
        f'<h3>{escape(title)}</h3>'
        f'<div class="workflow-story">'
        f'<p><strong>Operational Purpose:</strong> {escape(purpose)}</p>'
        f'<p><strong>Intended Business Value:</strong> {escape(business_value)}</p>'
        f'<p><strong>Engineering Contribution:</strong> {escape(engineering)}</p>'
        f'</div>'
        f'<div class="tags-row" style="margin: var(--space-xs) 0 var(--space-sm);">{tags_html}</div>'
        '<div class="workflow-captures">'
        + "".join(workflow_image(*image) for image in images)
        + '</div>'
        f'<p class="card-highlight"><strong>Evidence Verification Status:</strong> {escape(evidence)}</p>'
        '</article>'
    )
    return section(f"{number:02d}. {title}", body)


PAGES["automation.html"] = (
    "Automation",
    "Rehan Memon | AI & Workflow Automation",
    "Selected n8n workflow architectures developed during my Advfiction internship, with original editor captures, technical contributions and clearly stated execution evidence.",
    intro(
        "Pillar 3 · Workflow Automation",
        "AI & Workflow Automation",
        "Selected n8n workflow architectures developed during my Advfiction internship, with original editor captures, technical contributions and clearly stated execution evidence.",
        "projects.html#pillar-automation",
        "Pillar 3: AI & Workflow Automation",
        "page-intro-compact",
    )
    + workflow_index()
    + evidence_status_legend()
    + workflow_example(
        1, "wf-instagram-api", "Scheduled Publishing", "Design/configuration only",
        "Instagram Scheduled Publishing",
        "Automate scheduled social marketing publication by querying approved content assets from a spreadsheet, verifying publication time windows, and uploading media via the Instagram Graph API.",
        "Configured to support scheduled social publishing without manual posting during scheduled time slots.",
        "Implemented cron schedule triggering, status filtering for approved posts, Meta Graph API media container creation, publication polling, and post-publish Telegram alerts.",
        ["n8n", "Instagram Graph API", "Cron Scheduler", "Meta API", "Social Media Automation"],
        "The editor view shows the design and a warning on a notification node. A successful post or connected client account is not established.",
        [("instagram-scheduling.jpeg", 1600, 639, "n8n daily publishing design with approved-post lookup, timing checks, Instagram container and publish nodes, sheet update and Telegram notice.", "Original editor capture · scheduling design, with a warning on the notification path.")],
    )
    + workflow_example(
        2, "wf-news-prompt", "News Processing", "Design/configuration only",
        "News Sources to AI Summary",
        "Fetch articles from multiple news feeds, deduplicate headlines, request an LLM summary, and append curated briefs into spreadsheets.",
        "Designed to assist research teams by aggregating public news sources into structured summaries.",
        "Configured concurrent HTTP Request nodes, JavaScript array aggregation routines, JSON prompt formatting, and spreadsheet append nodes.",
        ["n8n", "HTTP Request Nodes", "JavaScript Transform", "LLM Summarization", "Competitive Intelligence"],
        "A design view shows the node sequence; there are no visible execution indicators or verified generated outputs.",
        [("news-ai-summary.jpeg", 1577, 503, "n8n news processing design merging two HTTP sources, JavaScript transformations, an AI request and a sheet append.", "News summary canvas · design shown, execution unverified."),
         ("news-image-composite.jpeg", 1600, 438, "Composite n8n content design connecting news, AI text, image generation, Drive and Telegram stages.", "Related composite canvas · stages are connected; output is unverified.")],
    )
    + workflow_example(
        3, "wf-social-publisher", "Social Publishing Prototype", "Design/configuration only",
        "PostgreSQL to AI Social Publisher",
        "Select records from PostgreSQL, prompt an LLM for social copy, trigger an image generation API, submit the draft to Telegram for review, and route approved posts to Facebook.",
        "Prototyped to coordinate multi-channel publishing from internal database records to social channels through a single canvas.",
        "Configured relational database queries, multi-modal generative prompts, supervisory Telegram notifications, and Facebook Graph API endpoints into a unified sequence.",
        ["n8n", "PostgreSQL", "Facebook Graph API", "Telegram Bot API", "Multi-modal AI", "Content Pipeline"],
        "The editor view shows connected nodes, not a successful approval, generated asset, published post or completed status update.",
        [("social-publisher-prototype.jpeg", 1600, 681, "n8n social publisher design with PostgreSQL, AI caption, image generation, Telegram review and Facebook request stages.", "Additional original canvas · publication and approvals unverified.")],
    )
    + workflow_example(
        4, "wf-subworkflow-router", "Outreach Prototype", "Test harness or skeleton",
        "AI Outreach and Team Notification Skeleton",
        "Provide a testing harness to evaluate lead qualification rules against simulated webhook payloads and route alerts to communication channels.",
        "Serves as a prototype skeleton to test lead routing logic before connecting live CRM accounts.",
        "Constructed mock lead test harnesses, conditional qualification decision trees, AI response synthesis, and multi-channel communication node templates.",
        ["n8n", "Lead Qualification", "Slack API", "Gmail API", "Test Harness", "Webhook Routing"],
        "The canvas labels itself a skeleton; communication nodes show configuration warnings. No live outreach or sent messages are established.",
        [("outreach-test-harness.jpeg", 1600, 728, "n8n AI outreach skeleton with mock lead data, qualification branch, AI request, Gmail and Slack nodes showing configuration warnings.", "Original editor capture · explicit skeleton; no outreach delivery shown.")],
    )
    + workflow_example(
        5, "wf-social-orchestrator", "Generative Media", "Design/configuration only",
        "Caption to Image Asset",
        "Read approved marketing copy from a spreadsheet, call a generative image API, store image assets in Google Drive, and log file URLs.",
        "Prototyped to assist digital marketing campaigns by pairing copy with AI-generated visual drafts.",
        "Built row-by-row iteration loops, dynamic prompt parameter injection, binary payload retrieval from image generation endpoints, Google Drive file upload, and spreadsheet URL updates.",
        ["n8n", "Generative AI Images", "Google Drive API", "Binary Data Handling", "Asset Pipeline"],
        "The design is visible, but successful image generation and asset sharing are not shown. It may be a stage of a larger content workflow.",
        [("caption-to-image-asset.jpeg", 1600, 527, "n8n caption-to-image design looping over sheet rows, calling an image API, uploading to Drive and updating the sheet.", "Original editor capture · image creation and sharing not demonstrated.")],
    )
    + workflow_example(
        6, "wf-itinerary-proposal", "Proposal Prototype", "Design/configuration only",
        "AI Itinerary and PDF Proposal",
        "Process incoming travel specifications, synthesize a multi-day itinerary using an LLM, convert styled HTML into a PDF proposal, and notify sales staff.",
        "Designed to expedite client proposal drafting by producing structured, branded itinerary documents from intake parameters.",
        "Configured prompt construction with client variable injection, JSON/HTML template structuring, PDF.co API conversion nodes, and status write-back to CRM tables.",
        ["n8n", "Groq AI / LLM", "HTML-to-PDF", "PDF.co API", "Spreadsheet ETL", "Sales Automation"],
        "The canvas shows configuration only; no generated itinerary, delivered proposal or completed lead update is established.",
        [("itinerary-pdf-proposal.jpeg", 1593, 472, "n8n itinerary proposal design with sheet filter, Groq AI request, HTML formatting, PDF.co conversion and Gmail route.", "Additional original canvas · proposal delivery unverified.")],
    )
    + workflow_example(
        7, "wf-maps-scraper", "Lead Capture", "Editor execution shown",
        "Apify Maps to Google Sheets",
        "Ingest local business and map listings from Apify scrapers, sanitize and filter dataset records, and append structured leads into Google Sheets for sales outreach.",
        "Designed to accelerate prospect list generation by transforming raw geocoded scraper datasets into spreadsheet-ready prospect tables for outbound sales teams.",
        "Configured webhook-triggered Apify actor execution, dataset pagination retrieval, conditional schema validation filtering, and idempotent Google Sheets append nodes.",
        ["n8n", "Apify Actor API", "Google Sheets API", "Data Filtering", "Lead Generation"],
        "Original editor capture demonstrates green indicators through the append node and five output items. Deployment and repeat runs are not established.",
        [("apify-map-to-sheets.jpeg", 798, 140, "n8n canvas connecting Maps Scraper, Apify actor, dataset retrieval, filter and Google Sheets append; five final items visible.", "Original editor capture · five items at the append node.")],
    )
    + workflow_example(
        8, "wf-lead-dossier", "Document Automation", "Design/configuration only",
        "Lead Row to PDF Brief",
        "Generate customized PDF prospect dossiers and executive briefing documents whenever a qualifying prospect record is logged or updated in a spreadsheet.",
        "Reduces repetitive sales preparation by assembling structured prospect information into printable summary documents.",
        "Built Google Sheets row change detection, template data formatting, programmatic Google Docs creation with text token replacement, Google Drive PDF export, and Gmail notification delivery.",
        ["n8n", "Google Docs API", "Google Drive API", "PDF Generation", "Gmail Automation", "Document Workflows"],
        "Two canvas views show initial and filtered pipeline configurations; document creation and email delivery are not shown completed.",
        [("lead-brief-initial.jpeg", 1600, 516, "Initial n8n lead brief design from spreadsheet row through Google Docs, Drive PDF export and Gmail notification.", "Initial canvas design · no delivered document shown."),
         ("lead-brief-filtered.jpeg", 1600, 752, "Later n8n lead brief design adding a filter before Google Docs creation and PDF export.", "Later canvas design · filter added; delivery remains unverified.")],
    )
    + workflow_example(
        9, "wf-postgres-research", "Company Research", "Partial execution shown",
        "PostgreSQL Search and AI Enrichment",
        "Query un-enriched company records from PostgreSQL, batch process candidate rows, and execute fallback search queries to discover missing firmographic context prior to LLM synthesis.",
        "Streamlines corporate intelligence gathering by automatically discovering company domains and firmographic data directly within relational records.",
        "Configured batched database cursor reads, duplicate detection logic, SerpApi/Google Search fallback nodes, and prompt formatting for AI summarization.",
        ["n8n", "PostgreSQL", "Batch Processing", "SerpApi", "LLM Prompting", "Data Enrichment"],
        "Early nodes and search branch show completed execution indicators; the downstream AI request has a warning indicator and final persistence is not shown completed.",
        [("postgres-search-ai-enrichment.jpeg", 1600, 590, "n8n PostgreSQL research canvas: fetched rows, batch, deduplication, search, warning on AI request and unrun save node.", "Original editor capture · partial run; AI enrichment and persistence unverified.")],
    )
    + workflow_example(
        10, "wf-telegram-bot", "Human Approval", "Design/configuration only",
        "Telegram Review and Approval",
        "Implement an asynchronous governance gate where pending marketing drafts or automated actions pause until a human supervisor clicks Approve or Reject via an interactive Telegram message.",
        "Helps prevent automated content delivery errors by introducing human verification before external publication.",
        "Configured n8n Wait-for-Webhook patterns, interactive inline Telegram bot callback query buttons, and conditional state branching to update master spreadsheets.",
        ["n8n", "Telegram Bot API", "Human-in-the-Loop", "Webhook Wait Node", "Approval Workflows"],
        "Original canvas displays wait node and conditional approval branches; reviewer responses and downstream triggers are not shown completed.",
        [("telegram-review-approval.jpeg", 1600, 677, "n8n Telegram approval design with sheet rows, reviewer message, wait node and approve or reject branches.", "Original editor capture · one unique image; second source file was identical.")],
    )
    + section(
        "Explore More Engineering Work",
        '<p class="prose">Explore other systems, client deliverables, and verified credentials across my engineering portfolio.</p>'
        '<div class="section-nav-group">'
        + link("projects.html", "Projects & Case Studies →", "button")
        + '<div class="sub-nav-links">'
        + link("experience.html", "Internship Experience →")
        + link("client-work.html", "Client Work & Deployments →")
        + link("credentials.html", "Credentials & Certifications →")
        + link("contact.html", "Get in Touch →")
        + '</div>'
        + '</div>',
    )
    + explore_more("automation.html"),
)


# 12. AUTOMATION EVIDENCE COMPATIBILITY REDIRECT: automation-evidence.html
PAGES["automation-evidence.html"] = (
    "Automation Evidence Gallery",
    "Rehan Memon | Automation Workflow Gallery",
    "The n8n workflow gallery has been consolidated into the unified AI & Workflow Automation systems page.",
    '<section class="container" style="padding: 4rem 1rem; text-align: center;">'
    '<div class="card" style="max-width: 680px; margin: 2rem auto; padding: 2.5rem 2rem;">'
    '<div class="card-top" style="justify-content: center; margin-bottom: 1rem;">'
    + badge("Consolidated Architecture")
    + '</div>'
    '<h1>AI &amp; Workflow Automation</h1>'
    '<p class="prose" style="margin: 1.5rem 0;">The complete 10-workflow gallery has been consolidated directly into our primary <strong>AI &amp; Workflow Automation</strong> systems page.</p>'
    '<script>window.location.replace("automation.html"+window.location.hash);</script>'
    '<div class="card-actions" style="justify-content: center;">'
    + link("automation.html", "Explore All 10 Workflow Architectures →", "button")
    + '</div>'
    '</div>'
    '</section>'
)

# 13. CREDENTIALS: credentials.html
PAGES["credentials.html"] = (
    "Credentials",
    "Rehan Memon | Credentials",
    "Verified workshop certifications, industry job simulations, and academic leadership records.",
    intro(
        "Credentials",
        "Curated Credential & Learning Library",
        f"A curated archive of {len(CREDENTIALS)} credentials and learning records spanning government remote sensing programs (ISRO/IIRS), computer science coursework, industry job simulations, and university extension honors.",
    )
    + '<section class="section container">'
    '<div class="status-banner">'
    '<p class="eyebrow">Evidence Traceability & Verification</p>'
    '<h2>Credential Evidence and Document Status</h2>'
    '<p class="status-desc">This registry contains 48 credential and recognition records. The 21 IIRS/ISRO outreach entries distinguish six workshop participations from fifteen online-course participations and link to separate privacy-safe copies. Other linked certificates require individual source and sharing review. Institutional nominations are documented privately.</p>'
    '</div>'
    '<div class="featured-credentials" style="margin-bottom: var(--space-xl);">'
    '<h2>Curated Featured Credentials</h2>'
    '<p class="section-lead">Selected institutional, government and commercial learning records across software engineering, AI systems, remote sensing, and university activities; document and classification evidence varies by entry.</p>'
    '<div class="grid three">'
    '<article class="card">'
    + eyebrow("AlgoDevOpss · Aug 2026") + badge("Commercial Internship", "status")
    + '<h3>Full-Stack Development Certification</h3>'
    '<p class="prose">Commercial internship completion certificate for departmental Next.js/TypeScript portal engineering, signed by Founder Yash Balotiya (Udyam: UDYAM-MH-18-0511641).</p>'
    '<div class="card-actions">'
    + link("https://drive.google.com/file/d/1yZyBwiDStZatvvD9oj5rlM1WUTBkz9BV/view", "View Certificate ↗", "button button-small", external=True)
    + '</div>'
    '</article>'
    '<article class="card">'
    + eyebrow("Advfiction · Oct 2026") + badge("Dual-Track Verified", "status")
    + '<h3>AI Automation Developer Certificate</h3>'
    '<p class="prose">Verified 22-week commercial internship completion certificate across AI workflow engineering and multi-stage n8n integrations, signed by MD Rojer R V.</p>'
    '<div class="card-actions">'
    + link("https://drive.google.com/file/d/1T_3ZDXAFRpxJ6-GDZAkyCPVchJdR7815/view", "View Certificate ↗", "button button-small", external=True)
    + '</div>'
    '</article>'
    '<article class="card">'
    + eyebrow("BCG X via Forage · Sep 2025") + badge("Enterprise Simulation", "status")
    + '<h3>GenAI Job Simulation Certificate</h3>'
    '<p class="prose">BCG X GenAI job simulation completed through Forage. This is a training simulation rather than employment with BCG X.</p>'
    '<div class="card-actions">'
    + link("https://drive.google.com/file/d/1VZPcWKt4f5I_vRD8REPQYADvNDZ_WsIL/view", "View Certificate ↗", "button button-small", external=True)
    + '</div>'
    '</article>'
    '<article class="card">'
    + eyebrow("IIRS / ISRO Outreach · 2025") + badge("Workshop Participation", "status")
    + '<h3>AI/ML Model for Specific Crop Acreage Mapping</h3>'
    '<p class="prose">Workshop conducted: 2 April 2025 · Certificate issued: 29 May 2025. The linked public copy removes enrollment and verification identifiers for candidate privacy.</p>'
    '<div class="card-actions">'
    + link("assets/documents/iirs-outreach/iirs-1046-participation.pdf", "View privacy-safe participation copy ↗", "button button-small", external=True)
    + '</div>'
    '</article>'
    '<article class="card">'
    + eyebrow("University of Mumbai DLLE · Apr 2026") + badge("University Award", "status")
    + '<h3>Certificate of Extension Work (120+ Hours)</h3>'
    '<p class="prose">Official University of Mumbai institutional award for completing over 120 verified field hours in Information Technology & community orientation.</p>'
    '<div class="card-actions">'
    + link("https://drive.google.com/file/d/1TiYoTYAcfwcNY4Q1iIRXUk5O0zbKXJGx/view", "View Certificate ↗", "button button-small", external=True)
    + '</div>'
    '</article>'
    '<article class="card">'
    + eyebrow("NISM / SEBI · Oct 2024") + badge("100% Score", "status")
    + '<h3>National Financial Literacy Examination</h3>'
    '<p class="prose">Perfect 100% score certification in the national World Investor Week examination administered by NISM and SEBI at VESASC.</p>'
    '<div class="card-actions">'
    + link("https://drive.google.com/file/d/1cOnLxXZZJ1ndNEfkJYN9vMFzWWdZJdxW/view", "View Certificate ↗", "button button-small", external=True)
    + '</div>'
    '</article>'
    '</div>'
    '</div>'
    '<h2>Browse All 48 Credential Records</h2>'
    '<div class="filter-pills" role="group" aria-label="Credential Domain Filter">'
    '<button type="button" class="filter-pill active" data-filter-domain="all" aria-pressed="true">All Records</button>'
    '<button type="button" class="filter-pill" data-filter-domain="geospatial & remote sensing" aria-pressed="false">Geospatial & Remote Sensing</button>'
    '<button type="button" class="filter-pill" data-filter-domain="ai, ml & data science" aria-pressed="false">AI, ML & Data Science</button>'
    '<button type="button" class="filter-pill" data-filter-domain="generative ai & automation" aria-pressed="false">Generative AI & Automation</button>'
    '<button type="button" class="filter-pill" data-filter-domain="software engineering" aria-pressed="false">Software Engineering</button>'
    '<button type="button" class="filter-pill" data-filter-domain="professional development" aria-pressed="false">Professional Development</button>'
    '<button type="button" class="filter-pill" data-filter-domain="academic & extension honors" aria-pressed="false">Academic Honors & DLLE</button>'
    '</div>'
    '<div class="filter-bar">'
    '<label for="credentialSearch">Search credentials</label>'
    '<input id="credentialSearch" type="search" placeholder="Search by title, issuer, keyword..." data-filter-search>'
    '<label for="credentialType">Type</label>'
    '<select id="credentialType" data-filter-type>'
    '<option value="">All Types</option>'
    + "".join(f'<option>{escape(kind)}</option>' for kind in sorted({c["kind"] for c in CREDENTIALS}))
    + '</select>'
    '<label for="credentialSubject">Subject</label>'
    '<select id="credentialSubject" data-filter-subject>'
    '<option value="">All Subjects</option>'
    '<option>AI / ML</option>'
    '<option>Generative AI</option>'
    '<option>Data Science</option>'
    '<option>Web Development</option>'
    '<option>Frontend Engineering</option>'
    '<option>Programming</option>'
    '<option>Systems Engineering</option>'
    '<option>Image Analysis</option>'
    '<option>Remote Sensing</option>'
    '<option>GIS & Satellite Systems</option>'
    '<option>Community Leadership</option>'
    '<option>Financial Literacy</option>'
    '</select>'
    '</div>'
    '<p class="filter-count" data-filter-count aria-live="polite"></p>'
    '<div class="grid two" data-filter-list data-noun-singular="credential" data-noun-plural="credentials">'
    + "".join(credential_card(c) for c in CREDENTIALS)
    + '</div>'
    '<p class="no-results" data-no-results hidden>No credentials match these filter criteria.</p>'
    '</section>'
    + section(
        "Verification & Institutional Integrity",
        '<div class="prose">'
        '<p>This library combines original documents, institutional records, and entries still under source review. A document link appears only where its current public destination is retained; its presence does not imply that every title, classification, privacy detail, or sharing permission has been independently verified. Sources represented include:</p>'
        '<ul class="prose-list">'
        '<li><strong>ISRO / IIRS Outreach:</strong> Indian Institute of Remote Sensing (Dehradun), Department of Space, Government of India.</li>'
        '<li><strong>BCG X via Forage:</strong> Boston Consulting Group enterprise simulation verification.</li>'
        '<li><strong>University of Mumbai DLLE:</strong> Department of Lifelong Learning and Extension formal certification.</li>'
        '<li><strong>thingQbator / Nasscom Foundation:</strong> Machine Learning and Image Processing certificate with Zikshaa listed as training partner.</li>'
        '<li><strong>NISM / SEBI:</strong> National Institute of Securities Markets financial literacy assessment.</li>'
        f'<li><strong>Academic Institution:</strong> <a class="text-link" href="{COLLEGE_URL}" target="_blank" rel="noopener noreferrer">{COLLEGE_NAME_FULL}</a>.</li>'
        '</ul>'
        '</div>',
    )
    + explore_more("credentials.html"),
)

# 14. ACTIVITIES: activities.html
PAGES["activities.html"] = (
    "Activities",
    "Rehan Memon | Activities & Recognition",
    "Smart India Hackathon nomination, university extension leadership, and institutional governance.",
    intro(
        "Activities",
        "Recognition & Leadership",
        "Verified participation in competitive national hackathons, university extension initiatives, and institutional student leadership.",
    )
    + section(
        "Smart India Hackathons (National Pipeline)",
        '<div class="grid two">'
        '<article class="card" id="sih-dbtdecoders">'
        '<div class="card-top">'
        + eyebrow("SIH 2025 · Team DBTDecoders")
        + badge("Round 1 Winner & Nominee")
        + '</div>'
        '<h3>SIH 2025: Round 1 College Winner & Principal Nomination</h3>'
        f'<p class="prose">Selected as the internal college round winner and officially nominated by the Principal of <a class="text-link" href="{COLLEGE_URL}" target="_blank" rel="noopener noreferrer">{COLLEGE_NAME_SHORT}</a> on 23 September 2025 (Ref: <code>VC/SFC/2025-26/0604</code>) as a core member of Team DBTDecoders representing the institution at <strong>Smart India Hackathon 2025</strong>.</p>'
        '<p class="prose">The team submission proposed conversational eligibility guidance for the National Scholarship Portal. The available deck and report describe a planned architecture; chatbot source and runtime behaviour were not established in this review.</p>'
        '<p class="meta">College recognition and nomination are documented separately from implementation and national-level results.</p>'
        '<div class="card-actions">'
        + link("https://drive.google.com/file/d/1q4Q5FpiPAZm-irxqMFRu3pySTRTiIZjr/view", "View Submission Deck ↗", "button button-small", external=True)
        + link("https://drive.google.com/file/d/1jsAe9UTxFwLhNVxKxh53FTQ4VVbICB4A/view", "View Project Report ↗", "button button-small button-quiet", external=True)
        + link("https://drive.google.com/file/d/1zqPoTyExGU_E8ShO77lAc91TT8BJ5Bg-/view", "View Demonstration Video ↗", "button button-small button-quiet", external=True)
        + link("projects.html#pillar-ai", "Explore Related AI Architecture →", "button button-small button-quiet")
        + '</div>'
        '</article>'
        '<article class="card" id="karigar-setu">'
        '<div class="card-top">'
        + eyebrow("SIH 2026 · Team Echo Logic")
        + badge("Selected Architecture")
        + '</div>'
        '<h3>SIH 2026: KARIGAR-SETU Artisan Platform (PS SIH26090)</h3>'
        '<p class="prose">Selected team architecture for Problem Statement SIH26090 (Heritage & Culture theme). Designed an AI-powered smart cataloging and direct marketplace mobile application for marginalized artisans.</p>'
        '<p class="prose">Engineered the technical blueprint incorporating on-device MobileNet/TensorFlow.js computer vision for product image enhancement, Google Gemini Flash API for catalog generation, and Web Speech API multilingual voice assistance.</p>'
        '<p class="meta">Verified by official SIH idea submission presentation and architecture blueprint.</p>'
        '<div class="card-actions">'
        + link("projects.html#pillar-ai", "Explore Related AI Architecture →", "button button-small button-quiet")
        + '</div>'
        '</article>'
        '</div>',
    )
    + section(
        "Public Speaking & Event Hosting",
        '<div class="grid two">'
        '<article class="card">'
        '<div class="card-top">'
        + eyebrow("Public Speaking · 2025")
        + '</div>'
        '<h3>NCC Day — Event Host, Anchor & Public Speaker</h3>'
        '<p class="meta">NCC Day Programme · Guru Nanak Khalsa College, Matunga, Mumbai</p>'
        '<p class="prose">Served as the host and anchor for the full NCC Day programme at Guru Nanak Khalsa College, Matunga, and delivered a speech before a large gathering that included senior NCC officers and distinguished guests.</p>'
        '</article>'
        '<article class="card">'
        '<div class="card-top">'
        + eyebrow("Inter-Collegiate Tech Festival · 2025")
        + '</div>'
        '<h3>Talentia — Event Anchor & Master of Ceremonies</h3>'
        '<p class="prose">Demonstrated stage presence, crowd management, and public speaking as anchor and master of ceremonies for the college annual festival.</p>'
        '<p class="meta">Co-curricular anchoring role at VESASC.</p>'
        '</article>'
        '</div>',
        sid="public-speaking",
    )
    + section(
        "Academic Examination Distinctions (VESASC Autonomous)",
        '<article class="card">'
        '<div class="card-top">'
        + eyebrow("B.Sc. Artificial Intelligence · University of Mumbai")
        + badge("Academic Results")
        + '</div>'
        '<h3>Academic Examination Standing (Semesters I–IV)</h3>'
        '<div class="grid two" style="margin-top: 1rem;">'
        '<div class="evidence-node-col">'
        '<h4>Aggregated Degree Performance</h4>'
        '<ul>'
        '<li><strong>Semester IV SGPA:</strong> 9.27 / 10.0 (Grade O Distinction)</li>'
        '<li><strong>Cumulative CGPA:</strong> 8.14 / 10.0 (Across Semesters I–IV)</li>'
        '<li><strong>Semester III SGPA:</strong> 8.18 / 10.0 (Grade A+ Standing)</li>'
        '<li><strong>Total Earned Credits:</strong> 88.00 / 88.00 Completed</li>'
        '</ul>'
        '</div>'
        '<div class="evidence-node-col">'
        '<h4>Institutional Information</h4>'
        '<ul>'
        f'<li><strong>Institution:</strong> <a class="text-link" href="{COLLEGE_URL}" target="_blank" rel="noopener noreferrer">{COLLEGE_NAME_SHORT}</a></li>'
        '<li><strong>Affiliation:</strong> University of Mumbai</li>'
        '<li><strong>Degree Program:</strong> B.Sc. Artificial Intelligence (2024–2027)</li>'
        '<li><strong>Examination Verification:</strong> Authenticated by official college examination marksheets.</li>'
        '</ul>'
        '</div>'
        '</div>'
        '</article>',
        sid="academic-distinctions",
    )
    + section(
        "University Extension Work",
        '<article class="card clickable-card">'
        '<div class="card-top">'
        + eyebrow("Department of Lifelong Learning & Extension (DLLE)")
        + badge("University Award")
        + '</div>'
        '<h3><a class="card-main-link" href="credentials.html">University of Mumbai Extension Leadership (120+ Hours)</a></h3>'
        '<p class="prose">Awarded the official Certificate of Extension Work for completing over <strong>120 verified annual field hours</strong> of social development and institutional community initiatives during academic year 2025–26 under the University of Mumbai DLLE program.</p>'
        '<p class="meta">Verified by University of Mumbai institutional certificate.</p>'
        '<div class="card-actions">'
        + link("https://drive.google.com/file/d/1TiYoTYAcfwcNY4Q1iIRXUk5O0zbKXJGx/view", "View DLLE Certificate (120+ Hours) ↗", "button button-small", external=True)
        + '</div>'
        '</article>',
    )
    + section(
        "Financial Literacy & Market Governance",
        '<article class="card">'
        '<div class="card-top">'
        + eyebrow("SEBI & NISM · October 2024")
        + badge("100% Score")
        + '</div>'
        '<h3>National Financial Literacy Examination</h3>'
        '<p class="prose">Achieved a <strong>perfect 100% score</strong> in the national World Investor Week examination administered under the joint auspices of the Securities and Exchange Board of India (SEBI) and National Institute of Securities Markets (NISM) at VESASC.</p>'
        '<p class="meta">Authenticated by official SEBI/NISM certification score.</p>'
        '<div class="card-actions">'
        + link("https://drive.google.com/file/d/1cOnLxXZZJ1ndNEfkJYN9vMFzWWdZJdxW/view", "View SEBI Financial Literacy Certificate (100% Score) ↗", "button button-small", external=True)
        + '</div>'
        '</article>',
    )
    + explore_more("activities.html"),
)

# 15. CONTACT: contact.html
PAGES["contact.html"] = (
    "Contact",
    "Rehan Memon | Contact",
    "Get in touch for AI engineering, backend systems, and workflow automation opportunities.",
    intro(
        "Contact",
        "Let's Build Together",
        "I am actively exploring opportunities in AI Engineering, Machine Learning, Backend Systems Architecture, and Workflow Automation. Reach out through any of the direct channels below.",
    )
    + section(
        "Curriculum Vitae",
        '<article class="card resume-hero-card">'
        '<div class="card-top">'
        + eyebrow("Verified Candidate Credentials")
        + badge("Available Online & PDF")
        + '</div>'
        '<h3>Professional Resume</h3>'
        f'<p class="prose">The linked Google Docs resume remains a candidate version until Rehan confirms it is the latest approved public document. The portfolio case studies contain the current project detail; academic records include a 9.27 Semester IV SGPA at <a class="text-link" href="{COLLEGE_URL}" target="_blank" rel="noopener noreferrer">{COLLEGE_NAME_SHORT}</a>.</p>'
        '<div class="card-actions">'
        + link(RESUME_URL, "View Live Resume (Google Doc) ↗", "button", external=True)
        + link(RESUME_PDF_URL, "Download PDF Export ↗", "button button-accent-outline", external=True)
        + '</div>'
        '</article>',
    )
    + section(
        "Direct Contact Channels",
        '<div class="grid three">'
        '<article class="card">'
        + eyebrow("Direct Inquiries")
        + '<h3>Email</h3>'
        + f'<div class="copy-email-box"><a class="text-link" href="mailto:{EMAIL}">{EMAIL}</a><button type="button" class="button button-small copy-email-btn" data-copy="{EMAIL}" aria-label="Copy email address to clipboard">Copy 📋</button></div>'
        + '<p class="note">Preferred channel for professional inquiries, engineering roles, and technical collaborations.</p>'
        + '</article>'
        '<article class="card">'
        + eyebrow("Professional Network")
        + '<h3>LinkedIn</h3>'
        + f'<p>{link(LINKEDIN, "linkedin.com/in/rehan-memon-b1803b334 ↗", external=True)}</p>'
        + '<p class="note">Connect for industry updates, professional discussions, and networking.</p>'
        + '</article>'
        '<article class="card">'
        + eyebrow("Open Source & Code")
        + '<h3>GitHub</h3>'
        + f'<p>{link(GITHUB, "github.com/rehanmemon-ai ↗", external=True)}</p>'
        + '<p class="note">Source code for public projects, machine learning baselines, and web repositories.</p>'
        + '</article>'
        '</div>',
    )
    + section(
        "Academic & Professional Profiles",
        '<div class="grid three">'
        '<article class="card">'
        + eyebrow("Competitive Programming")
        + '<h3>LeetCode</h3>'
        + f'<p>{link(LEETCODE, "leetcode.com/u/rehanmemon-ai ↗", external=True)}</p>'
        + '<p class="note">Algorithms, data structures, and problem-solving practice.</p>'
        + '</article>'
        '<article class="card">'
        + eyebrow("Machine Learning")
        + '<h3>Kaggle</h3>'
        + f'<p>{link(KAGGLE, "kaggle.com/rehanjunedmemon ↗", external=True)}</p>'
        + '<p class="note">Data science notebooks, generative-video model benchmarks, and datasets.</p>'
        + '</article>'
        '<article class="card">'
        + eyebrow("Institutional Affiliation")
        + f'<h3>{COLLEGE_NAME_SHORT}</h3>'
        + f'<p>{link(COLLEGE_URL, "ves.ac.in/vesasc ↗", external=True)}</p>'
        + '<p class="note">Department of Artificial Intelligence, University of Mumbai.</p>'
        + '</article>'
        '</div>',
    )
    + explore_more("contact.html"),
)

NAV = [
    ("index.html", "Home"),
    ("about.html", "About"),
    ("experience.html", "Experience"),
    ("projects.html", "Projects"),
    ("client-work.html", "Client Work"),
    ("automation.html", "Automation"),
    ("credentials.html", "Credentials"),
    ("activities.html", "Activities"),
    ("contact.html", "Contact"),
]

SCHEMA_JSON_LD = f"""  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Person",
    "name": "Rehan Juned Memon",
    "url": "{SITE_URL}/",
    "jobTitle": "AI Engineer & Software Systems Developer",
    "alumniOf": {{
      "@type": "EducationalOrganization",
      "name": "{COLLEGE_NAME_FULL}",
      "url": "{COLLEGE_URL}"
    }},
    "knowsAbout": [
      "Machine Learning",
      "Computer Vision",
      "Retrieval-Augmented Generation",
      "Full-Stack Web Development",
      "Workflow Automation",
      "FastAPI",
      "Next.js",
      "Python",
      "TypeScript",
      "n8n"
    ],
    "sameAs": [
      "{GITHUB}",
      "{LINKEDIN}",
      "{LEETCODE}",
      "{KAGGLE}"
    ]
  }}
  </script>"""


def generate_sitemap():
    urls = []
    for filename in PAGES:
        if filename == "automation-evidence.html":
            continue  # Compatibility redirect; the consolidated page is canonical.
        urls.append(f"  <url>\n    <loc>{SITE_URL}/{filename}</loc>\n    <changefreq>weekly</changefreq>\n  </url>")
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(urls) + "\n</urlset>\n"
    (ROOT / "sitemap.xml").write_text(xml, encoding="utf-8", newline="\n")


def generate_robots():
    txt = f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}/sitemap.xml\n"
    (ROOT / "robots.txt").write_text(txt, encoding="utf-8", newline="\n")


def render(filename, item):
    label, title, description, body = item
    nav_desktop = "".join(
        f'<a href="{href}"' + (' aria-current="page"' if filename == href else "") + f'>{name}</a>'
        for href, name in NAV
    )
    nav_mobile = "".join(
        f'<a href="{href}"' + (' aria-current="page"' if filename == href else "") + f'>{name}</a>'
        for href, name in NAV
    )
    resume_btn = f'<a class="button button-small resume-nav-btn" href="{RESUME_URL}" target="_blank" rel="noopener noreferrer">Resume ↗</a>'
    schema_script = f"\n{SCHEMA_JSON_LD}" if filename == "index.html" else ""
    redirect_meta = ""
    canonical_path = "automation.html" if filename == "automation-evidence.html" else ("" if filename == "index.html" else filename)

    brand_mark = (
        '<a class="brand" href="index.html" aria-label="Rehan Memon, home">'
        '<svg class="brand-monogram" viewBox="0 0 64 64" width="28" height="28" aria-hidden="true" focusable="false">'
        '<rect width="64" height="64" rx="14" fill="#0b1317"/>'
        '<rect x="1.5" y="1.5" width="61" height="61" rx="12.5" fill="none" stroke="#22d3ee" stroke-width="2.5" stroke-opacity="0.85"/>'
        '<path d="M14 47V17H25C29.5 17 32 19.5 32 24.5C32 29.5 29.5 32 25 32H14" fill="none" stroke="#22d3ee" stroke-width="6.5" stroke-linecap="round" stroke-linejoin="round"/>'
        '<path d="M22 32L32 47" fill="none" stroke="#22d3ee" stroke-width="6.5" stroke-linecap="round" stroke-linejoin="round"/>'
        '<path d="M37 47V17L44.5 31L52 17V47" fill="none" stroke="#ffffff" stroke-width="6.5" stroke-linecap="round" stroke-linejoin="round"/>'
        '</svg>'
        '<span class="brand-text">REHAN MEMON</span>'
        '</a>'
    )

    return f'''<!doctype html>
<html lang="en" class="dark">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">{redirect_meta}
  <meta name="description" content="{escape(description, quote=True)}">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{escape(title, quote=True)}">
  <meta property="og:description" content="{escape(description, quote=True)}">
  <meta property="og:url" content="{SITE_URL}/{canonical_path}">
  <meta property="og:image" content="{SITE_URL}/assets/social-card.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <link rel="canonical" href="{SITE_URL}/{canonical_path}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{escape(title, quote=True)}">
  <meta name="twitter:description" content="{escape(description, quote=True)}">
  <meta name="twitter:image" content="{SITE_URL}/assets/social-card.png">
  <meta name="theme-color" content="#0d171c">
  <title>{escape(title)}</title>
  <link rel="icon" type="image/svg+xml" href="favicon.svg">
  <link rel="icon" href="favicon.ico" sizes="any">
  <link rel="apple-touch-icon" href="apple-touch-icon.png">
  <script>
    (function(){{
      try {{
        var t = localStorage.getItem('theme');
        if (t === 'light') {{
          document.documentElement.classList.remove('dark');
          document.documentElement.classList.add('light');
          var m = document.querySelector('meta[name="theme-color"]');
          if (m) m.setAttribute('content', '#f7f7f2');
        }}
      }} catch(e) {{}}
    }})();
  </script>
  <link rel="stylesheet" href="site.css">{schema_script}
  <script src="site.js" defer></script>
</head>
<body>
  <a class="skip-link" href="#main">Skip to content</a>
  <header class="site-header">
    <div class="container header-inner">
      {brand_mark}
      <nav class="desktop-nav" aria-label="Primary">{nav_desktop}</nav>
      <div class="header-actions">
        {resume_btn}
        <button id="themeToggle" class="icon-button" type="button" aria-label="Switch to light theme"><span id="themeIcon" aria-hidden="true">Light</span></button>
        <button id="mobileMenuBtn" class="icon-button menu-button" type="button" aria-controls="mobileMenu" aria-expanded="false" aria-label="Open menu">Menu</button>
      </div>
    </div>
    <nav id="mobileMenu" class="mobile-nav" aria-label="Mobile primary" hidden>
      {nav_mobile}
      <div class="mobile-menu-cta">
        <a class="button" href="{RESUME_URL}" target="_blank" rel="noopener noreferrer">View Resume (Google Doc) ↗</a>
      </div>
    </nav>
  </header>
  <main id="main">{body}</main>
  <footer class="site-footer">
    <div class="container footer-inner">
      <p>Rehan Juned Memon · AI Engineering &amp; Software Systems</p>
      <div class="footer-links">
        {link('projects.html', 'Projects')}
        {link('experience.html', 'Experience')}
        {link('automation.html', 'Workflow Automation')}
        {link('credentials.html', 'Credentials')}
        {link(RESUME_URL, 'Resume ↗', external=True)}
        {link(f'mailto:{EMAIL}', 'Email')}
      </div>
    </div>
  </footer>
</body>
</html>
'''


def main():
    for filename, item in PAGES.items():
        (ROOT / filename).write_text(render(filename, item), encoding="utf-8", newline="\n")
    generate_sitemap()
    generate_robots()
    print(f"Rendered {len(PAGES)} static pages with three-pillar architecture, sitemap.xml, and robots.txt")


if __name__ == "__main__":
    main()
