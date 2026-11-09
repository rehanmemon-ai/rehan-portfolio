"""Render the static portfolio pages from reviewed, evidence-backed content. Dependency-free."""

from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent
GITHUB = "https://github.com/rehanmemon-ai"
SIGNATURE = f"{GITHUB}/signature-verification"
RESEARCH = f"{GITHUB}/Assistant_Bot-Research"
EMAIL = "memon18rehan@gmail.com"
LINKEDIN = "https://www.linkedin.com/in/rehan-memon-b1803b334"
LEETCODE = "https://leetcode.com/u/rehanmemon-ai/"
KAGGLE = "https://www.kaggle.com/rehanjunedmemon"
RESUME_DOC_ID = "1aXDe4hqYjGSrUSUdmjhXPUbHVSO_6Em_5VP4u_72Kfg"
RESUME_URL = f"https://docs.google.com/document/d/{RESUME_DOC_ID}/edit"
RESUME_PDF_URL = f"https://docs.google.com/document/d/{RESUME_DOC_ID}/export?format=pdf"
DRIVE_CREDENTIALS_URL = "https://drive.google.com/drive/folders/11IE6MjLIiwc70rHwgrvSJOeOFZvSw6AM?usp=drive_link"
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
        ("automation-evidence.html", "Automation Workflow Gallery →", "Selected n8n canvas examples"),
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
    # PILLAR 1: Applied AI & Machine Learning Systems
    {
        "name": "Signature Verification AI",
        "pillar": "Applied AI & Machine Learning",
        "category": "Computer Vision · Machine Learning",
        "status": "Research Baseline · Verified Implementation",
        "summary": "Offline handwritten signature verification pipeline engineered with OpenCV morphological preprocessing, extraction of 331 geometric/contour features, and an RBF Support Vector Machine evaluated under a writer-disjoint split protocol.",
        "route": "signature-verification.html",
        "repo": SIGNATURE,
        "live": "",
        "highlight": "Extracts 331 handcrafted features (Hu moments, projection profiles, ink density) with FastAPI and React demo interface.",
        "tags": ["Python", "OpenCV", "Scikit-Learn", "SVM", "FastAPI", "React"],
    },
    {
        "name": "AI Research Assistant",
        "pillar": "Applied AI & Machine Learning",
        "category": "Generative AI · Retrieval-Augmented Generation",
        "status": "In Progress / Currently Developing",
        "summary": "Document question-answering prototype featuring token-aware text chunking, dense Chroma vector database indexing, workspace-scoped similarity retrieval, transparent source citation mapping, and a local FastAPI service harness.",
        "route": "ai-research-assistant.html",
        "repo": RESEARCH,
        "live": "",
        "highlight": "Modular Python ingestion prototype with Chroma dense vector embeddings and citation-grounded retrieval.",
        "tags": ["Python", "ChromaDB", "Vector Search", "FastAPI", "RAG", "Embeddings"],
    },
    {
        "name": "KARIGAR-SETU — Artisan Smart Cataloging",
        "pillar": "Applied AI & Machine Learning",
        "category": "Multimodal AI · On-Device Vision",
        "status": "Selected Architecture · SIH 2026",
        "summary": "AI-powered mobile cataloging and direct market linkage platform designed for marginalized artisans (Problem Statement SIH26090). Combines on-device MobileNet/TensorFlow.js computer vision for product enhancement, Google Gemini Flash API for automated catalog descriptions, and Web Speech API for multilingual voice interaction.",
        "route": "activities.html#karigar-setu",
        "repo": "",
        "live": "",
        "highlight": "On-device TensorFlow.js visual preprocessing and multilingual voice interaction tailored for low-digital-literacy artisans.",
        "tags": ["React 19", "TensorFlow.js", "MobileNet", "Google Gemini API", "Web Speech API", "Vite"],
    },
    {
        "name": "National Scholarship Portal AI Assistant",
        "pillar": "Applied AI & Machine Learning",
        "category": "Conversational Agent · Knowledge Base RAG",
        "status": "College Round 1 Winner · SIH 2025",
        "summary": "Interactive conversational assistant built for the National Scholarship Portal (NSP / DBT scheme). Selected as Round 1 College Winner and formally nominated by Principal (Ref: VC/SFC/2025-26/0604) for national participation. Features guided eligibility query routing and verified knowledge base matching.",
        "route": "activities.html#sih-dbtdecoders",
        "repo": "",
        "live": "",
        "highlight": "College 1st Round Winner and Principal-nominated hackathon prototype with recorded demonstration.",
        "tags": ["Conversational AI", "Node.js", "Knowledge Base", "SIH 2025", "NSP DBT"],
    },

    # PILLAR 2: Selected Client Deployments
    {
        "name": "SAHASH NGO Voice & Conversational Assistant",
        "pillar": "Selected Client Deployments",
        "category": "Conversational AI · NGO Community Support",
        "status": "Completed Deployment Prototype",
        "summary": "Full-stack conversational assistant engineered for SAHASH India via ConnectFor to assist community members, volunteers, and donors. Built with Node.js, Express, Google Gemini Flash API, an in-memory vector store for verified organizational FAQs, session memory, rate limiting, and a multilingual Web Speech API voice interface.",
        "route": "client-work.html#sahash-chatbot",
        "repo": "",
        "live": "",
        "highlight": "Voice-enabled conversational agent with semantic retrieval grounded strictly in verified NGO organization data to prevent hallucinations.",
        "tags": ["Node.js", "Express", "Google Gemini API", "Vector Store", "Web Speech API", "Voice UI"],
    },
    {
        "name": "Advfiction Enterprise Lead LMS",
        "pillar": "Selected Client Deployments",
        "category": "Full-Stack Web & API Engineering",
        "status": "Live Client Deployment",
        "summary": "Full-stack lead management system serving marketing operations. Engineered production REST API endpoints, CORS security configurations, input sanitization schemas, and Supabase PostgreSQL persistence connected to a responsive authenticated interface.",
        "route": "client-work.html#advfiction-lms",
        "repo": "",
        "live": "https://advfiction-lms.vercel.app/pages/login.html",
        "highlight": "Active production service with live backend health monitoring on Render and client frontend on Vercel.",
        "tags": ["Node.js", "Express", "Supabase", "PostgreSQL", "REST API", "Vercel"],
    },
    {
        "name": "LMS Girls Higher Secondary School",
        "pillar": "Selected Client Deployments",
        "category": "Full-Stack Portal · Next.js & Supabase",
        "status": "Live Platform Deployment",
        "summary": "Comprehensive educational web platform built with Next.js 16, React 19, TypeScript, and Supabase. Implemented administrative modules for dynamic event scheduling, student enquiry capture, and automated countdown logic.",
        "route": "client-work.html#girls-hss",
        "repo": "",
        "live": "https://girlshss.netlify.app/",
        "highlight": "Dynamic administrative dashboard and serverless API routes for school event and enquiry workflows.",
        "tags": ["Next.js 16", "React 19", "TypeScript", "Tailwind CSS", "Supabase"],
    },
    {
        "name": "Marthandam Star Honey Platform",
        "pillar": "Selected Client Deployments",
        "category": "E-Commerce Showcase & API Integration",
        "status": "Live Client Deployment",
        "summary": "Commercial product showcase and inquiry platform engineered with React 19, Vite, Tailwind CSS, and Framer Motion. Built wholesale product catalog modules and an Express backend routing customer inquiries directly into Google Sheets via API.",
        "route": "client-work.html#msh-honey",
        "repo": "",
        "live": "https://msh-website.netlify.app/",
        "highlight": "Interactive product showcase with validated inquiry routing directly into cloud spreadsheets.",
        "tags": ["React 19", "Vite", "Tailwind CSS", "Express", "Google Sheets API"],
    },
    {
        "name": "Advfiction Corporate Website Revamp",
        "pillar": "Selected Client Deployments",
        "category": "Collaborative Web Engineering",
        "status": "Live Production Deployment",
        "summary": "Revamp of the primary corporate web presence for Advfiction Private Limited. Implemented responsive interface layouts, interactive service presentations, and contact form integrations routing inquiries directly to the company's backend lead pipeline.",
        "route": "client-work.html#advfiction-website",
        "repo": "",
        "live": "https://advfiction.vercel.app/",
        "highlight": "Live company website featuring mobile-responsive UI and connected contact intake.",
        "tags": ["JavaScript", "HTML5/CSS3", "API Integration", "Vercel"],
    },

    # PILLAR 3: AI & Workflow Automation Systems
    {
        "name": "Apify-to-Sheets Lead Pipeline",
        "pillar": "AI & Workflow Automation",
        "category": "Map Data Ingestion",
        "status": "Editor Run Shown",
        "summary": "An n8n canvas connects an Apify map scraper to dataset retrieval, a filter, and Google Sheets row insertion. A private editor capture shows five items at the final append node.",
        "route": "automation.html#map-lead-capture",
        "repo": "",
        "live": "",
        "evidence": "automation-evidence.html#wf-maps-scraper",
        "highlight": "One small editor run is visible; ongoing deployment and larger-scale output are not established.",
        "tags": ["n8n", "Apify Actors", "Google Sheets API", "Data Filtering", "ETL"],
    },
    {
        "name": "Company Research & AI Enrichment Canvas",
        "pillar": "AI & Workflow Automation",
        "category": "Database Research Canvas",
        "status": "Partial Editor Run",
        "summary": "A PostgreSQL research canvas fetches rows, batches them, checks prior processing and routes search results toward an AI request and database save step.",
        "route": "automation.html#company-research",
        "repo": "",
        "live": "",
        "evidence": "automation-evidence.html#wf-postgres-research",
        "highlight": "Early nodes completed in the editor; the AI request shows a warning and the save step is not shown completing.",
        "tags": ["n8n", "PostgreSQL", "AI Prompts", "SerpApi", "Batch Processing"],
    },
    {
        "name": "Lead Brief & PDF Workflow Design",
        "pillar": "AI & Workflow Automation",
        "category": "Document Automation Design",
        "status": "Design-Stage Pipeline",
        "summary": "Two n8n canvas views show a sheet-triggered lead brief: format fields, create a Google Doc, export a PDF and route a Gmail notification. A later view adds a filter.",
        "route": "automation.html#lead-report",
        "repo": "",
        "live": "",
        "evidence": "automation-evidence.html#wf-lead-dossier",
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
        "dates": "Sep 2026–Present · Offer: Sep 2026–Mar 2027",
        "status_note": "Workstream paused since November 2026",
        "summary": "Engineered media workflow prototyping in React/TypeScript and FastAPI: built five-scene JSONL storyboards (263 backend / 27 frontend tests passing in verified local snapshot), engineered Pillow/SHA-256 image ingestion (7 integration tests), investigated legacy FFmpeg stream drift, and benchmarked generative-video models on Kaggle.",
        "route": "awarewolf.html",
    },
    {
        "name": "Advfiction Private Limited",
        "role": "Web Development Intern · AI Automation Developer Intern",
        "badge": "DUAL TRACK",
        "dates": "Apr–Sep 2026 · Concurrent Tracks",
        "status_note": "Initial 3-month term: 30 Apr–30 Jul 2026; Extended through 30 Sep 2026",
        "summary": "Operated across two concurrent engineering workstreams: built full-stack lead intake APIs (Node/Express, Supabase) and responsive interfaces on the web team, while architecting multi-stage n8n workflows for automated lead capture, PostgreSQL research, and document generation.",
        "route": "advfiction.html",
    },
    {
        "name": "AlgoDevOpss",
        "role": "Full-Stack Development Intern",
        "badge": "VERIFIED TERM",
        "dates": "May–Dec 2026 · Extended Appointment",
        "status_note": "Appointment letter: May–Oct 2026; Completion certificate: May–Aug 2026; Extension communicated through Dec 2026 (updated extension offer letter pending)",
        "summary": "Collaborated on departmental web modules for the KJSIEIT EXTC website in Next.js and TypeScript, engineering the dedicated Pedagogy showcase route and the typed results-data.ts performance module, alongside database-backed CMS prototyping.",
        "route": "algodevopss.html",
    },
]

# Full Curated Credential Records across 6 Domains
CREDENTIALS = [
    # Domain 1: Generative AI & Automation
    {
        "title": "GenAI Job Simulation",
        "issuer": "BCG X via Forage",
        "date": "15 Sep 2025",
        "kind": "Enterprise Simulation",
        "subject": "Generative AI",
        "domain": "Generative AI & Automation",
        "tags": ["Generative AI", "Python", "LLMs", "RAG", "Data Extraction"],
        "detail": "Enterprise simulation involving automated unstructured data extraction, financial performance modeling in Python, and engineering a conversational AI assistant prototype.",
        "status": "Verified Credential",
    },

    # Domain 2: AI, Machine Learning & Data Science
    {
        "title": "Application of AI/ML Model for Specific Crop Acreage Mapping (Course 1046)",
        "issuer": "IIRS / ISRO Outreach",
        "date": "29 May 2025",
        "kind": "Government Training",
        "subject": "AI / ML",
        "domain": "AI, ML & Data Science",
        "tags": ["AI/ML", "Satellite Data", "Spectral Classification", "Remote Sensing"],
        "detail": "Government certification on applying supervised machine learning algorithms and spectral index models to multi-spectral satellite datasets for agricultural acreage estimation.",
        "status": "Government Certified",
    },
    {
        "title": "Machine Learning and Image Processing",
        "issuer": "Zikshaa · Nasscom Foundation Partner",
        "date": "Academic Year 2024–2025",
        "kind": "Industry Program",
        "subject": "AI / ML",
        "domain": "AI, ML & Data Science",
        "tags": ["Machine Learning", "Image Processing", "OpenCV", "Scikit-Learn"],
        "detail": "Comprehensive training in classical machine learning algorithms, image filtering, spatial transformations, feature extraction, and predictive classification models.",
        "status": "Verified Credential",
    },
    {
        "title": "Data Science Career Track Masterclass",
        "issuer": "PW Skills (PhysicsWallah)",
        "date": "Academic Year 2024–2025",
        "kind": "Technical Masterclass",
        "subject": "Data Science",
        "domain": "AI, ML & Data Science",
        "tags": ["Data Science", "Python", "Pandas", "EDA", "Statistical Modeling"],
        "detail": "Intensive coursework on end-to-end data science workflows: exploratory data analysis, feature engineering, statistical hypotheses testing, and model evaluation protocols.",
        "status": "Verified Credential",
    },
    {
        "title": "Artificial Intelligence Beginner Skill Certification",
        "issuer": "Guru Skill Assessment",
        "date": "Academic Year 2025",
        "kind": "Skill Assessment",
        "subject": "AI / ML",
        "domain": "AI, ML & Data Science",
        "tags": ["AI Fundamentals", "Knowledge Representation", "Search Algorithms"],
        "detail": "Certified proficiency in fundamental AI principles, state-space representations, heuristic search methods, and core machine learning paradigms.",
        "status": "Verified Credential",
    },
    {
        "title": "Machine Learning For Health-Care",
        "issuer": "Cursa Educational Platform",
        "date": "Academic Year 2024–2025",
        "kind": "Course Certification",
        "subject": "AI / ML",
        "domain": "AI, ML & Data Science",
        "tags": ["Machine Learning", "Healthcare Analytics", "Predictive Modeling"],
        "detail": "Training in applying supervised classification and regression models to clinical tabular datasets, biomedical metrics, and risk stratification workflows.",
        "status": "Verified Credential",
    },
    {
        "title": "Fundamentals of Artificial Intelligence",
        "issuer": "Cursa Educational Platform",
        "date": "Academic Year 2024–2025",
        "kind": "Course Certification",
        "subject": "AI / ML",
        "domain": "AI, ML & Data Science",
        "tags": ["AI Concepts", "Neural Networks", "NLP Basics", "Computer Vision"],
        "detail": "Foundational study of artificial intelligence architectures, heuristic problem-solving, perceptrons, and neural network fundamentals.",
        "status": "Verified Credential",
    },
    {
        "title": "5-Day AI & Computer Vision Bootcamp: Face Tracking with Cursor.AI",
        "issuer": "Let's Upgrade / Tech Partner",
        "date": "Academic Year 2024–2025",
        "kind": "Hands-on Bootcamp",
        "subject": "AI / ML",
        "domain": "AI, ML & Data Science",
        "tags": ["Computer Vision", "Face Tracking", "Cursor.AI", "JavaScript"],
        "detail": "Applied workshop building browser-based facial landmark tracking and interaction models integrated with modern AI-assisted engineering environments.",
        "status": "Verified Credential",
    },
    {
        "title": "Artificial Intelligence & Deep Learning Workshop",
        "issuer": "FirstBit Solutions",
        "date": "19 Jul 2025",
        "kind": "Technical Workshop",
        "subject": "AI / ML",
        "domain": "AI, ML & Data Science",
        "tags": ["Deep Learning", "Neural Networks", "AI Workshop", "FirstBit Solutions"],
        "detail": "Hands-on technical workshop on deep neural network architectures, backpropagation algorithms, activation functions, and foundational computer vision concepts.",
        "status": "Verified Credential",
    },

    # Domain 3: Software Engineering & Programming
    {
        "title": "Full-Stack Web Development Internship Certification",
        "issuer": "AlgoDevOpss",
        "date": "31 Aug 2026",
        "kind": "Internship Credential",
        "subject": "Web Development",
        "domain": "Software Engineering",
        "tags": ["Next.js", "TypeScript", "React", "Full-Stack Web", "API Design"],
        "detail": "Formal internship completion award for engineering departmental Next.js web applications, TypeScript data architectures, and dynamic UI modules for academic portals.",
        "status": "Primary Document Verified",
    },
    {
        "title": "Building E-Commerce Applications with React",
        "issuer": "PW Skills (PhysicsWallah)",
        "date": "Academic Year 2024–2025",
        "kind": "Technical Masterclass",
        "subject": "Frontend Engineering",
        "domain": "Software Engineering",
        "tags": ["React", "JavaScript", "State Management", "Component Architecture"],
        "detail": "Hands-on engineering masterclass focused on developing modular React single-page applications, cart state management, and responsive component libraries.",
        "status": "Verified Credential",
    },
    {
        "title": "Data Structures & Algorithms with C++",
        "issuer": "Let's Upgrade / Tech Partner",
        "date": "10 Jul 2025",
        "kind": "Technical Bootcamp",
        "subject": "Programming",
        "domain": "Software Engineering",
        "tags": ["C++", "DSA", "Algorithms", "Time Complexity", "Memory Management"],
        "detail": "Bootcamp covering fundamental algorithms: binary search trees, graph traversals, dynamic programming paradigms, and time/space complexity optimization.",
        "status": "Verified Credential",
    },
    {
        "title": "Python 3: From Basics to Advanced Engineering",
        "issuer": "Cursa Educational Platform",
        "date": "Academic Year 2024–2025",
        "kind": "Course Certification",
        "subject": "Programming",
        "domain": "Software Engineering",
        "tags": ["Python 3", "OOP", "Decorators", "File I/O", "Data Structures"],
        "detail": "Comprehensive certification in modern Python syntax, object-oriented design, functional programming patterns, exception handling, and standard library modules.",
        "status": "Verified Credential",
    },
    {
        "title": "Operating Systems & System Programming",
        "issuer": "Cursa Educational Platform",
        "date": "Academic Year 2024–2025",
        "kind": "Course Certification",
        "subject": "Systems Engineering",
        "domain": "Software Engineering",
        "tags": ["Operating Systems", "Process Management", "Concurrency", "Memory Paging"],
        "detail": "Study of system architectures: kernel process scheduling, virtual memory management, thread synchronization primitives, and POSIX system call interfaces.",
        "status": "Verified Credential",
    },
    {
        "title": "Advanced Spreadsheet Engineering & Data Analysis",
        "issuer": "One Roadmap Skill Certification",
        "date": "Academic Year 2024–2025",
        "kind": "Skill Assessment",
        "subject": "Data Tools",
        "domain": "Software Engineering",
        "tags": ["Excel", "Data Modeling", "Lookup Formulas", "Pivot Tables"],
        "detail": "Certified proficiency in complex analytical functions, dynamic matrix lookups, data aggregation pipelines, and financial modeling worksheets.",
        "status": "Verified Credential",
    },
    {
        "title": "Cloud Computing Fundamentals & Architecture",
        "issuer": "Cursa Educational Platform",
        "date": "11 Feb 2026",
        "kind": "Course Certification",
        "subject": "Systems Engineering",
        "domain": "Software Engineering",
        "tags": ["Cloud Computing", "Virtualization", "IaaS/PaaS", "Infrastructure"],
        "detail": "Certification covering cloud deployment models, virtualization hypervisors, serverless architectures, and distributed storage infrastructure.",
        "status": "Verified Credential",
    },
    {
        "title": "Web Development Foundations: HTML, CSS & JavaScript",
        "issuer": "Cursa Educational Platform",
        "date": "11 Feb 2026",
        "kind": "Course Certification",
        "subject": "Web Development",
        "domain": "Software Engineering",
        "tags": ["HTML5", "CSS3", "JavaScript", "DOM Manipulation", "Responsive Design"],
        "detail": "Core engineering coursework covering semantic HTML5 structures, CSS Flexbox/Grid responsive layouts, and ES6+ DOM manipulation pipelines.",
        "status": "Verified Credential",
    },

    # Domain 4: Geospatial Analysis & Remote Sensing (ISRO / IIRS)
    {
        "title": "Advanced Image Analysis for Geospatial Professionals (Course 1048)",
        "issuer": "IIRS / ISRO Outreach",
        "date": "12 Nov 2025",
        "kind": "Government Training",
        "subject": "Image Analysis",
        "domain": "Geospatial & Remote Sensing",
        "tags": ["Image Analysis", "Digital Elevation Models", "Geospatial", "ISRO"],
        "detail": "Advanced remote-sensing course covering multi-band optical imagery preprocessing, orthorectification, feature segmentation, and radiometric correction.",
        "status": "Government Certified",
    },
    {
        "title": "Advances in Thermal Infrared Remote Sensing for Ecological Studies (Course 1047)",
        "issuer": "IIRS / ISRO Outreach",
        "date": "3 Nov 2025",
        "kind": "Government Training",
        "subject": "Remote Sensing",
        "domain": "Geospatial & Remote Sensing",
        "tags": ["Thermal Infrared", "Ecological Modeling", "Surface Temperature", "ISRO"],
        "detail": "Specialized government training on land surface temperature retrieval algorithms, emissivity estimation, and thermal infrared applications in ecology.",
        "status": "Government Certified",
    },
    {
        "title": "Aerosols Measurement, Retrieval and Environmental Impacts (Course 1052)",
        "issuer": "IIRS / ISRO Outreach",
        "date": "12 Jan 2026",
        "kind": "Government Training",
        "subject": "Remote Sensing",
        "domain": "Geospatial & Remote Sensing",
        "tags": ["Aerosol Optical Depth", "Atmospheric Remote Sensing", "MODIS", "ISRO"],
        "detail": "Government workshop on satellite atmospheric retrieval algorithms, optical depth calculation, radiative forcing models, and particulate monitoring.",
        "status": "Government Certified",
    },
    {
        "title": "Basics of Remote Sensing, GIS and Global Navigation Satellite Systems (Course 169)",
        "issuer": "IIRS / ISRO Outreach",
        "date": "7 Feb 2026",
        "kind": "Government Training",
        "subject": "GIS & Satellite Systems",
        "domain": "Geospatial & Remote Sensing",
        "tags": ["Remote Sensing", "GIS", "GNSS", "Coordinate Systems", "ISRO"],
        "detail": "Comprehensive foundation program in electromagnetic radiation theory, spatial map projections, vector/raster GIS topology, and multi-constellation satellite positioning.",
        "status": "Government Certified",
    },
    {
        "title": "Geospatial Technology for Modelling of Urban Environments (Course 162)",
        "issuer": "IIRS / ISRO Outreach",
        "date": "28 Jun 2025",
        "kind": "Government Training",
        "subject": "Urban GIS",
        "domain": "Geospatial & Remote Sensing",
        "tags": ["Urban Modeling", "3D GIS", "Land Cover Change", "Spatial Planning", "ISRO"],
        "detail": "Technical training on urban canopy modeling, impervious surface extraction, spatial sprawl metrics, and high-resolution satellite cartography.",
        "status": "Government Certified",
    },
    {
        "title": "Overview of Geocomputation and Geo-Web Services (Course 173)",
        "issuer": "IIRS / ISRO Outreach",
        "date": "12 Jan 2026",
        "kind": "Government Training",
        "subject": "Spatial Web Services",
        "domain": "Geospatial & Remote Sensing",
        "tags": ["Geocomputation", "OGC Web Services", "WMS/WFS", "Spatial Databases", "ISRO"],
        "detail": "Engineering course on OGC geospatial web protocols (WMS, WFS, WCS), cloud spatial architectures, spatial querying, and web mapping interfaces.",
        "status": "Government Certified",
    },
    {
        "title": "Overview of Geographical Information Systems (Course 172)",
        "issuer": "IIRS / ISRO Outreach",
        "date": "17 Nov 2025",
        "kind": "Government Training",
        "subject": "GIS Topology",
        "domain": "Geospatial & Remote Sensing",
        "tags": ["GIS", "Spatial Analysis", "Overlay Operations", "Database Design", "ISRO"],
        "detail": "Training in spatial data structures, topological overlay analysis, proximity buffers, and relational geodatabase schema design.",
        "status": "Government Certified",
    },
    {
        "title": "Overview of Geographical Information Systems (Course 150)",
        "issuer": "IIRS / ISRO Outreach",
        "date": "22 Nov 2024",
        "kind": "Government Training",
        "subject": "GIS Foundations",
        "domain": "Geospatial & Remote Sensing",
        "tags": ["GIS", "Spatial Projections", "Cartography", "ISRO"],
        "detail": "Introductory government training in vector cartographic structures, coordinate reference frames, and thematic map production.",
        "status": "Government Certified",
    },
    {
        "title": "Overview of Global Navigation Satellite Systems (Course 170)",
        "issuer": "IIRS / ISRO Outreach",
        "date": "3 Nov 2025",
        "kind": "Government Training",
        "subject": "GNSS Navigation",
        "domain": "Geospatial & Remote Sensing",
        "tags": ["GNSS", "NavIC", "GPS", "Differential Positioning", "ISRO"],
        "detail": "Study of satellite constellation signals, pseudorange multilateration, ionospheric error mitigation, and NavIC/GPS dual-frequency positioning architectures.",
        "status": "Government Certified",
    },
    {
        "title": "RS & GIS Applications in Natural Resource Management (Course 174)",
        "issuer": "IIRS / ISRO Outreach",
        "date": "12 Jan 2026",
        "kind": "Government Training",
        "subject": "Resource Management",
        "domain": "Geospatial & Remote Sensing",
        "tags": ["Natural Resources", "Watershed Delineation", "Forestry", "ISRO"],
        "detail": "Applied curriculum on hydrological watershed modeling, forest cover change detection, soil erosion vulnerability mapping, and multi-criteria evaluation.",
        "status": "Government Certified",
    },
    {
        "title": "Remote Sensing and Numerical Ocean Modelling for Oceanic Processes",
        "issuer": "IIRS / ISRO Outreach",
        "date": "3 Nov 2025",
        "kind": "Government Training",
        "subject": "Ocean Remote Sensing",
        "domain": "Geospatial & Remote Sensing",
        "tags": ["Oceanography", "Altimetry", "Sea Surface Temperature", "Hydrodynamics", "ISRO"],
        "detail": "Training on satellite ocean altimetry, chlorophyll-a concentration retrieval, sea surface temperature dynamics, and coastal hydrodynamic simulation.",
        "status": "Government Certified",
    },
    {
        "title": "Remote Sensing Data Analytics for Crop Production Forecasting (Course 168)",
        "issuer": "IIRS / ISRO Outreach",
        "date": "17 Jul 2025",
        "kind": "Government Training",
        "subject": "Agricultural Analytics",
        "domain": "Geospatial & Remote Sensing",
        "tags": ["Crop Forecasting", "NDVI Time Series", "Yield Modeling", "ISRO"],
        "detail": "Instruction on vegetation indices (NDVI, EVI) time-series analysis, phenological stage tracking, and statistical crop yield prediction equations.",
        "status": "Government Certified",
    },
    {
        "title": "Remote Sensing Observations for Earth and Planetary Geological Studies (Course 171)",
        "issuer": "IIRS / ISRO Outreach",
        "date": "3 Nov 2025",
        "kind": "Government Training",
        "subject": "Planetary Geology",
        "domain": "Geospatial & Remote Sensing",
        "tags": ["Planetary Geology", "Hyperspectral", "Mineral Mapping", "ISRO"],
        "detail": "Advanced module on hyperspectral mineral absorption feature analysis, planetary surface crater morphology, and structural geological mapping.",
        "status": "Government Certified",
    },
    {
        "title": "Research and Career Opportunities for Space Science & Technology in India (Course 175)",
        "issuer": "IIRS / ISRO Outreach",
        "date": "12 Jan 2026",
        "kind": "Government Seminar",
        "subject": "Space Science",
        "domain": "Geospatial & Remote Sensing",
        "tags": ["Space Tech", "Mission Payloads", "Satellite Systems", "ISRO"],
        "detail": "Overview of Indian space program architectures, payload sensor engineering, deep space ground tracking networks, and scientific data archives.",
        "status": "Government Certified",
    },
    {
        "title": "Space Exploration Technology: An Overview (Course 159)",
        "issuer": "IIRS / ISRO Outreach",
        "date": "1 Jun 2025",
        "kind": "Government Training",
        "subject": "Space Technology",
        "domain": "Geospatial & Remote Sensing",
        "tags": ["Launch Vehicles", "Orbital Mechanics", "Spacecraft Subsystems", "ISRO"],
        "detail": "Technical training on launch vehicle telemetry, orbital insertion trajectories, spacecraft power subsystems, and deep-space communication protocols.",
        "status": "Government Certified",
    },
    {
        "title": "Space Inputs for Village-Level Crop Assessment (Course 1041)",
        "issuer": "IIRS / ISRO Outreach",
        "date": "26 Mar 2025",
        "kind": "Government Training",
        "subject": "Agricultural Remote Sensing",
        "domain": "Geospatial & Remote Sensing",
        "tags": ["Cadastral Mapping", "High-Resolution Imagery", "Agritech", "ISRO"],
        "detail": "Methodology for integrating cadastral parcel boundaries with very-high-resolution multispectral imagery for micro-level agricultural assessment.",
        "status": "Government Certified",
    },
    {
        "title": "Recent Trends in Ecological Modelling & Simulation (Course 161)",
        "issuer": "IIRS / ISRO Outreach",
        "date": "28 Jun 2025",
        "kind": "Government Training",
        "subject": "Ecological GIS",
        "domain": "Geospatial & Remote Sensing",
        "tags": ["Ecological Simulation", "Habitat Suitability", "Biodiversity GIS", "ISRO"],
        "detail": "Coursework in species distribution modeling, MaxEnt algorithms, landscape fragmentation indices, and conservation geospatial analytics.",
        "status": "Government Certified",
    },
    {
        "title": "Archival and Access of Space Science Data",
        "issuer": "IIRS / ISRO Outreach",
        "date": "17 Jul 2025",
        "kind": "Government Training",
        "subject": "Space Data Science",
        "domain": "Geospatial & Remote Sensing",
        "tags": ["ISDA Portal", "Data Archival", "PDS4 Standard", "Metadata", "ISRO"],
        "detail": "Study of planetary and astronomical data archiving standards, PDS4 data models, open-access science repositories, and API query pipelines.",
        "status": "Government Certified",
    },
    {
        "title": "The Method of Space Science Research (Course 160)",
        "issuer": "IIRS / ISRO Outreach",
        "date": "28 Jun 2025",
        "kind": "Government Training",
        "subject": "Research Methodology",
        "domain": "Geospatial & Remote Sensing",
        "tags": ["Research Methodology", "Scientific Computing", "Data Calibration", "ISRO"],
        "detail": "Methodological training on formulating space science research problems, instrumental calibration pipelines, hypothesis testing, and observational telemetry analysis.",
        "status": "Government Certified",
    },
    {
        "title": "Origin of the Universe and Solar System Exploration (Course 1053)",
        "issuer": "IIRS / ISRO Outreach",
        "date": "21 Jan 2026",
        "kind": "Government Training",
        "subject": "Astrophysics",
        "domain": "Geospatial & Remote Sensing",
        "tags": ["Astrophysics", "Solar Physics", "Planetary Science", "ISRO"],
        "detail": "Scientific course on cosmological expansion models, solar wind magnetosphere interactions, planetary accretion dynamics, and lunar/Martian mission data.",
        "status": "Government Certified",
    },

    # Domain 5: Professional Development & Job Simulations
    {
        "title": "Coding-Track Micro-Internship Program",
        "issuer": "Talerang · Cloudwrk Partner",
        "date": "Academic Year 2025",
        "kind": "Micro-Internship",
        "subject": "Industry Readiness",
        "domain": "Professional Development",
        "tags": ["Software Engineering", "Workplace Readiness", "Code Quality", "Collaboration"],
        "detail": "Rigorous software engineering readiness and corporate problem-solving program evaluated with a top-bracket PASS distinction across code hygiene, design, and execution standards.",
        "status": "Verified Credential",
    },
    {
        "title": "Master Social Media Advertising & Campaign Optimization",
        "issuer": "Digital Marketing Academy",
        "date": "Academic Year 2024–2025",
        "kind": "Professional Course",
        "subject": "Marketing Tech",
        "domain": "Professional Development",
        "tags": ["Digital Campaigns", "Analytics", "Audience Segmentation", "Optimization"],
        "detail": "Certification covering digital ad architectures, audience targeting parameters, campaign performance analytics, and conversion funnel optimization.",
        "status": "Verified Credential",
    },

    # Domain 6: Academic & Community Honors
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
    },
    {
        "title": "EMSA Technical & Media Committee Recognition",
        "issuer": "VESASC (Autonomous) EMSA",
        "date": "Academic Year 2024–2025",
        "kind": "Institutional Leadership",
        "subject": "Campus Leadership",
        "domain": "Academic & Extension Honors",
        "tags": ["VESASC", "EMSA", "Leadership", "Technical Operations"],
        "detail": "Recognition for serving on the Electronics & Media Student Association (EMSA) executive committee at VESASC Autonomous, organizing technical symposiums and academic seminars.",
        "status": "Institutional Recognition",
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
        "status": "Verified Credential",
    },
    {
        "title": "Smart India Hackathon 2025: Round 1 Winner & Principal Nomination",
        "issuer": "AICTE / Smart India Hackathon & VESASC",
        "date": "23 Sep 2025",
        "kind": "National Examination",
        "subject": "AI / ML",
        "domain": "Academic & Extension Honors",
        "tags": ["Smart India Hackathon", "DBTDecoders", "Principal Nomination", "NSP AI"],
        "detail": "Round 1 College Winner and official Principal nomination (Ref: VC/SFC/2025-26/0604) to represent VESASC at SIH 2025 for engineering the National Scholarship Portal conversational assistant.",
        "status": "Institutional Recognition",
    },
    {
        "title": "Smart India Hackathon 2026: Team EchoLogic Selected Architecture (PS SIH26090)",
        "issuer": "AICTE / Smart India Hackathon",
        "date": "Academic Year 2026",
        "kind": "National Examination",
        "subject": "AI / ML",
        "domain": "Academic & Extension Honors",
        "tags": ["Smart India Hackathon", "EchoLogic", "KARIGAR-SETU", "Multimodal AI"],
        "detail": "Selected team proposal for Problem Statement SIH26090: KARIGAR-SETU, an AI-powered smart cataloging and market linkage platform for marginalized artisans.",
        "status": "Institutional Recognition",
    },
]


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
    return (
        f'<article class="card experience-card clickable-card">'
        f'<div class="card-top">{eyebrow(item["dates"])}{badge_html}</div>'
        f'<h3><a class="card-main-link" href="{escape(item["route"], quote=True)}">{escape(item["name"])}</a></h3>'
        f'<p class="meta">{escape(item["role"])}</p>'
        f'{status_note}'
        f'<p>{escape(item["summary"])}</p>'
        f'<div class="card-actions">{link(item["route"], "Explore Engineering Contribution →", "button button-small")}</div>'
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
    status = item.get("status", "Verified Credential")
    tags = item.get("tags", [])

    tags_html = "".join(f'<span class="tag">{escape(t)}</span>' for t in tags)
    search = f"{title} {issuer} {kind} {subject} {domain} {detail} {' '.join(tags)}".lower()

    return (
        f'<article class="card credential-card clickable-card" data-filter-card data-issuer="{escape(issuer, quote=True)}" '
        f'data-type="{escape(kind, quote=True)}" data-subject="{escape(subject, quote=True)}" '
        f'data-domain="{escape(domain, quote=True)}" data-search="{escape(search, quote=True)}">'
        f'<div class="card-top">{eyebrow(kind)}{badge(status, "status")}</div>'
        f'<h3>{escape(title)}</h3>'
        f'<p class="meta">{escape(issuer)} · {escape(date)}</p>'
        f'<p class="prose-small">{escape(detail)}</p>'
        f'<div class="tags-row">{tags_html}</div>'
        f'</article>'
    )


PAGES = {}

# 1. HOMEPAGE: index.html
PAGES["index.html"] = (
    "Home",
    "Rehan Memon | Home",
    "Applied AI Engineer & Software Developer building production web platforms, vector retrieval systems (RAG), computer vision pipelines, and scalable workflow automations.",
    '<section class="hero container">'
    '<div>'
    + eyebrow("Applied AI · Full-Stack Systems · Workflow Automation")
    + '<h1>Rehan Juned Memon<span class="accent">.</span></h1>'
    '<p class="hero-lead">I engineer <strong>practical machine learning systems</strong>, <strong>vector retrieval architectures (RAG)</strong>, full-stack web platforms, and <strong>autonomous multi-stage workflows</strong>.</p>'
    f'<p class="meta">B.Sc. Artificial Intelligence · <a class="text-link" href="{COLLEGE_URL}" target="_blank" rel="noopener noreferrer">{COLLEGE_NAME_SHORT}</a>, University of Mumbai · 2024–2027 · Semester IV SGPA: <strong>9.27/10</strong> · CGPA: <strong>8.14/10</strong></p>'
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
    '<p>Practical systems designed for reliability, scalability, and measurable business utility:</p>'
    '<div class="pillar-links">'
    + link("projects.html#pillar-ai", "1. Applied AI & Machine Learning →")
    + link("projects.html#pillar-client", "2. Selected Client Deployments →")
    + link("projects.html#pillar-automation", "3. AI & Workflow Automation →")
    + '</div>'
    '</aside>'
    '</section>'
    + section(
        "Selected Engineering Work",
        '<p class="section-lead">Curated highlights representing production web engineering, vector search, computer vision, and autonomous data pipelines.</p>'
        '<div class="grid two">'
        + project_card(get_project("Signature Verification AI"))
        + project_card(get_project("AI Research Assistant"))
        + project_card(get_project("Advfiction Enterprise Lead LMS"))
        + project_card(get_project("Apify-to-Sheets Lead Pipeline"))
        + '</div>'
        '<p class="section-end">'
        + link("projects.html", "View All Projects Across All Pillars →")
        + ' · '
        + link("client-work.html", "Client Deployments →")
        + ' · '
        + link("automation.html", "Workflow Automation →")
        + ' · '
        + link("automation-evidence.html", "Automation Evidence Gallery →")
        + '</p>',
        "selected-work",
    )
    + section(
        "Commercial & Team Experience",
        '<p class="section-lead">Documented engineering contributions across high-velocity startups and academic web platforms.</p>'
        '<div class="grid three">'
        + "".join(experience_card(e) for e in EXPERIENCE)
        + '</div>'
        '<p class="section-end">'
        + link("experience.html", "View Comprehensive Experience →")
        + ' · '
        + link("awarewolf.html", "AwareWolf Deep Dive →")
        + ' · '
        + link("advfiction.html", "Advfiction Deep Dive →")
        + ' · '
        + link("algodevopss.html", "AlgoDevOpss Deep Dive →")
        + '</p>',
    )
    + section(
        "Academic Distinction & Verified Honors",
        '<div class="grid two">'
        '<article class="card clickable-card">'
        + eyebrow("VESASC (Autonomous) · University of Mumbai")
        + f'<h3><a class="card-main-link" href="{COLLEGE_URL}" target="_blank" rel="noopener noreferrer">{COLLEGE_NAME_FULL}</a></h3>'
        '<p>Consistent top-percentile academic performance in <strong>B.Sc. Artificial Intelligence</strong>. <strong>Semester IV SGPA: 9.27/10</strong>, cumulative CGPA: <strong>8.14/10</strong>. Standout coursework: <strong>98% (49/50, Grade O) in AI in IoT</strong> and <strong>94% (47/50, Grade O) in Generative AI & Prompt Engineering</strong>.</p>'
        + '<div class="card-actions">'
        + link("about.html", "Detailed academic background →", "button button-small button-quiet")
        + '</div>'
        + '</article>'
        '<article class="card clickable-card">'
        + eyebrow("National Recognition & Verified Certifications")
        + '<h3><a class="card-main-link" href="credentials.html">Competitive Awards & Credentials</a></h3>'
        '<p>Nominated team member representing VESASC for <strong>Smart India Hackathon 2025</strong> (Team DBTDecoders). Completed <strong>21 ISRO/IIRS geospatial AI</strong> courses, <strong>BCG X GenAI simulation</strong>, and <strong>120+ verified field hours</strong> with University of Mumbai DLLE.</p>'
        + '<div class="card-actions">'
        + link("credentials.html", "Inspect verified credential archive →", "button button-small button-quiet")
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
        f"I am an Artificial Intelligence undergraduate at {COLLEGE_NAME_SHORT}, University of Mumbai, focused on transforming ML models into reliable, production-grade software.",
    )
    + section(
        "Academic Foundation",
        '<div class="prose">'
        f'<p>Currently pursuing a <strong>{DEGREE_NAME}</strong> (2024–2027) at <a class="text-link" href="{COLLEGE_URL}" target="_blank" rel="noopener noreferrer">{COLLEGE_NAME_FULL}</a>, within the <a class="text-link" href="{AI_DEPT_URL}" target="_blank" rel="noopener noreferrer">Department of Artificial Intelligence</a>, affiliated with the University of Mumbai.</p>'
        '<p>My March 2026 Semester IV results demonstrate consistent mastery across core disciplines: <strong>9.27/10 SGPA</strong> with an <strong>8.14/10 cumulative CGPA</strong>. Standout subject scores include <strong>98% (49/50, Grade O) in AI in IoT</strong>, <strong>94% (47/50, Grade O) in Generative AI & Prompt Engineering</strong>, <strong>94% (47/50, Grade O) in Data Analytics using Python</strong>, and <strong>92% (46/50, Grade O) in AI in Drone Technology</strong>.</p>'
        '</div>',
    )
    + section(
        "Technical Focus & Skills Matrix",
        '<p class="section-lead">Core engineering proficiencies mapped directly to verified project implementations and institutional certifications:</p>'
        '<div class="skills-matrix">'
        '<div class="skill-card">'
        + eyebrow("Core Discipline 1")
        + '<h3>Applied AI & Machine Learning</h3>'
        '<p>Classical machine learning, computer vision feature engineering, and retrieval-augmented generation.</p>'
        '<div class="skill-chips">'
        + link("signature-verification.html", "OpenCV", "skill-chip")
        + link("signature-verification.html", "Scikit-Learn / SVM", "skill-chip")
        + link("ai-research-assistant.html", "ChromaDB", "skill-chip")
        + link("ai-research-assistant.html", "RAG & Embeddings", "skill-chip")
        + link("signature-verification.html", "FastAPI Inference", "skill-chip")
        + link("credentials.html", "ISRO Geospatial AI", "skill-chip")
        + '</div>'
        '</div>'
        '<div class="skill-card">'
        + eyebrow("Core Discipline 2")
        + '<h3>Full-Stack Software Engineering</h3>'
        '<p>Robust frontend architectures, typed REST API services, and relational persistence.</p>'
        '<div class="skill-chips">'
        + link("awarewolf.html", "React 19 & TypeScript", "skill-chip")
        + link("algodevopss.html", "Next.js 16", "skill-chip")
        + link("client-work.html#advfiction-lms", "Node.js & Express", "skill-chip")
        + link("client-work.html#advfiction-lms", "Supabase / PostgreSQL", "skill-chip")
        + link("awarewolf.html", "Pillow Validation", "skill-chip")
        + link("client-work.html", "Vercel / Render", "skill-chip")
        + '</div>'
        '</div>'
        '<div class="skill-card">'
        + eyebrow("Core Discipline 3")
        + '<h3>AI & Workflow Automation</h3>'
        '<p>Multi-stage autonomous pipelines, API integrations, and event-driven document generation.</p>'
        '<div class="skill-chips">'
        + link("automation.html#map-lead-capture", "n8n Orchestration", "skill-chip")
        + link("automation.html#map-lead-capture", "Apify Actors", "skill-chip")
        + link("automation.html#company-research", "PostgreSQL Batch ETL", "skill-chip")
        + link("automation.html#lead-report", "PDF Compilation", "skill-chip")
        + link("automation-evidence.html", "Webhook Handlers", "skill-chip")
        + link("automation-evidence.html", "n8n Canvas Examples", "skill-chip")
        + '</div>'
        '</div>'
        '<div class="skill-card">'
        + eyebrow("Core Discipline 4")
        + '<h3>Data Science & Geospatial Analysis</h3>'
        '<p>Remote-sensing satellite data processing, digital elevation modeling, and spectral indices.</p>'
        '<div class="skill-chips">'
        + link("credentials.html", "Satellite Image Analysis", "skill-chip")
        + link("credentials.html", "ISRO / IIRS Programs", "skill-chip")
        + link("credentials.html", "Spectral Classification", "skill-chip")
        + link("credentials.html", "Pandas / NumPy", "skill-chip")
        + link("credentials.html", "GIS Topology", "skill-chip")
        + '</div>'
        '</div>'
        '</div>',
    )
    + section(
        "Engineering Principles",
        '<div class="prose">'
        '<p>I prioritize software clarity, deterministic reproducibility, and evidence-grounded engineering over hype:</p>'
        '<ul class="prose-list">'
        '<li><strong>Deterministic Retrieval:</strong> When building RAG pipelines, I enforce explicit source citation mapping, cosine similarity thresholds, and lexical fallback checks.</li>'
        '<li><strong>Defensive Persistence:</strong> Concurrency issues and race conditions must be resolved through content-addressed storage (SHA-256), atomic write protocols, and revision tokens.</li>'
        '<li><strong>Empirical Validation:</strong> I verify system capabilities through automated test suites (pytest, jest) and objective benchmarks rather than anecdotal impressions.</li>'
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
        "Three documented internship engagements demonstrating full-stack engineering, API architecture, and enterprise workflow orchestration.",
    )
    + section(
        "Internship Timeline",
        '<div class="grid three">'
        + "".join(experience_card(e) for e in EXPERIENCE)
        + '</div>',
    )
    + section(
        "Engineering Scope & Highlights",
        '<div class="grid three">'
        '<article class="card clickable-card">'
        + eyebrow("AwareWolf · Sep 2026–Present (Paused)")
        + badge("PAID INTERNSHIP", "status")
        + '<h3><a class="card-main-link" href="awarewolf.html">Media Systems Prototyping</a></h3>'
        '<p>Engineered full-stack five-scene JSONL storyboards (263 backend / 27 frontend tests passing in local verification snapshot), Pillow/SHA-256 ingestion, FFmpeg sync fixes, and generative-video benchmarks on Kaggle.</p>'
        + link("awarewolf.html", "View AwareWolf deep dive →", "button button-small button-quiet")
        + '</article>'
        '<article class="card clickable-card">'
        + eyebrow("Advfiction Private Limited · Apr–Sep 2026")
        + badge("DUAL TRACK", "status")
        + '<h3><a class="card-main-link" href="advfiction.html">Dual-Track Web & AI Automation</a></h3>'
        '<p>Simultaneously supported client-facing web development (LMS backend APIs, responsive layouts) and internal AI automation initiatives (n8n lead scrapers, company research pipelines).</p>'
        + link("advfiction.html", "View Advfiction deep dive →", "button button-small button-quiet")
        + '</article>'
        '<article class="card clickable-card">'
        + eyebrow("AlgoDevOpss · May–Dec 2026")
        + badge("EXTENDED APPOINTMENT", "status")
        + '<h3><a class="card-main-link" href="algodevopss.html">Academic Web Portal</a></h3>'
        '<p>Appointment letter: May–October 2026. Completion certificate: May–August 2026. Extension communicated through December 2026; updated extension offer letter pending. Developed production TypeScript routes and data modules for the KJSIEIT EXTC website.</p>'
        + link("algodevopss.html", "View AlgoDevOpss deep dive →", "button button-small button-quiet")
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
        "Apr–Sep 2026 · Web Development Intern & AI Automation Developer Intern · Initial 3-month term (30 Apr–30 Jul 2026) extended for two additional months through 30 Sep 2026. Bridging frontend/backend web infrastructure with multi-node workflow orchestration.",
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
        '<li><strong>Advfiction Enterprise Lead LMS (<a class="text-link" href="client-work.html#advfiction-lms">Case Study</a>):</strong> Collaborated on Node/Express REST API endpoints handling public lead ingestion, input validation schemas, and Supabase PostgreSQL insertion.</li>'
        '<li><strong>CORS & Security Policies:</strong> Configured multi-origin CORS enabling secure communication between Vercel-hosted frontends and Render backend services.</li>'
        '<li><strong>Corporate Website Revamp (<a class="text-link" href="client-work.html#advfiction-website">Live Deployment</a>):</strong> Built responsive UI components and hooked contact forms directly into the backend lead pipeline. Live at <a class="text-link" href="https://advfiction.vercel.app/" target="_blank" rel="noopener noreferrer">advfiction.vercel.app ↗</a>.</li>'
        '</ul>'
        '<div class="card-actions">'
        + link("client-work.html#advfiction-lms", "Inspect LMS Client Deployment →", "button button-small")
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
        '<li><strong>Other Designs:</strong> Private canvas views show scheduled publishing, Telegram review and AI-assisted content stages; live use is unverified.</li>'
        '</ul>'
        '<div class="card-actions">'
        + link("automation.html", "Featured Automation Workflows →", "button button-small")
        + link("automation-evidence.html", "View Workflow Gallery →", "button button-small button-accent-outline")
        + '</div>'
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
        "Technical Stack Deployed",
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
        "Full-Stack Development Intern · May–December 2026. Appointment letter: May–October 2026. Completion certificate: May–August 2026. Extension communicated through December 2026; updated extension offer letter pending. Developing production routes for the KJSIEIT EXTC academic platform.",
        "experience.html",
        "Commercial Experience",
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
    "Software engineering and applied AI evaluation for media workflows at AwareWolf: React/FastAPI storyboards, image ingestion, FFmpeg diagnostics, and video model evaluation.",
    intro(
        "Experience / AwareWolf",
        "Media Workflows, Persistence & AI Evaluation",
        "Content Operating System Intern · Sep 2026–Present (Engineering Pause Reported Nov 2026) · Offer: 17 Sep 2026–16 Mar 2027 · Remote · Paid Internship. Software development for media workflow prototyping and applied AI evaluation, spanning interactive React/TypeScript storyboards, FastAPI APIs, media validation pipelines, FFmpeg stream diagnostics, and generative-video benchmarking.",
        "experience.html",
        "Commercial Experience",
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
        "Applied Generative-Video Evaluation",
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
    "Rehan Memon | Projects",
    "Comprehensive technical catalog across Applied AI & ML, Selected Client Deployments, and AI Workflow Automation.",
    intro(
        "Projects",
        "Selected Projects",
        "Explore 12 projects across applied AI, client deployments and workflow automation.",
        css_class="page-intro-compact",
    )
    + '<section class="section section-directory-tools container">'
    '<div class="filter-pills" role="group" aria-label="Filter projects by engineering pillar">'
    '<button type="button" class="filter-pill" data-filter-pillar-button="Applied AI & Machine Learning" aria-pressed="false" aria-controls="projectResults">1. Applied AI & Machine Learning (4)</button>'
    '<button type="button" class="filter-pill" data-filter-pillar-button="Selected Client Deployments" aria-pressed="false" aria-controls="projectResults">2. Selected Client Deployments (5)</button>'
    '<button type="button" class="filter-pill" data-filter-pillar-button="AI & Workflow Automation" aria-pressed="false" aria-controls="projectResults">3. AI & Workflow Automation (3)</button>'
    '</div>'
    '<div class="filter-bar">'
    '<label for="projectSearch">Search all 12 projects</label>'
    '<input id="projectSearch" type="search" placeholder="Search by name, technique, tool..." data-filter-search>'
    '<label for="projectPillar">Filter by Pillar</label>'
    '<select id="projectPillar" data-filter-pillar>'
    '<option value="">All Pillars (12 Projects)</option>'
    '<option>Applied AI & Machine Learning</option>'
    '<option>Selected Client Deployments</option>'
    '<option>AI & Workflow Automation</option>'
    '</select>'
    '</div>'
    '<p class="filter-count" data-filter-count role="status" aria-live="polite" aria-atomic="true">12 projects shown</p>'
    '</section>'
    '<div id="projectResults" data-filter-list data-noun-singular="project" data-noun-plural="projects">'
    + section(
        "Pillar 1: Applied AI & Machine Learning Systems",
        '<p class="section-lead">Algorithmic baselines evaluated under rigorous evaluation protocols and reproducible benchmarks.</p>'
        '<div class="grid two">'
        + "".join(project_card(p) for p in PROJECTS if p["pillar"] == "Applied AI & Machine Learning")
        + '</div>',
        "pillar-ai",
        'data-pillar-section',
    )
    + section(
        "Pillar 2: Selected Client Deployments",
        '<p class="section-lead">Production web platforms, administrative portals, and authenticated API services serving real operational teams.</p>'
        '<div class="grid two">'
        + "".join(project_card(p) for p in PROJECTS if p["pillar"] == "Selected Client Deployments")
        + '</div>'
        '<p class="section-end">' + link("client-work.html", "Explore In-Depth Client Deployments & Architecture →") + '</p>',
        "pillar-client",
        'data-pillar-section',
    )
    + section(
        "Pillar 3: AI & Workflow Automation Systems",
        '<p class="section-lead">Selected n8n canvases covering map-data capture, company research and document automation. Editor-test and design status are shown on each card.</p>'
        '<div class="grid two">'
        + "".join(project_card(p) for p in PROJECTS if p["pillar"] == "AI & Workflow Automation")
        + '</div>'
        '<p class="section-end">'
        + link("automation.html", "Explore Featured Automation Case Studies →")
        + ' · '
        + link("automation-evidence.html", "View Selected Workflow Examples →")
        + '</p>',
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
    "Offline handwritten signature verification pipeline with morphological preprocessing, 331 contour features, and SVM classification.",
    intro(
        "Pillar 1 · Applied AI & Systems",
        "Signature Verification AI",
        "A classical computer vision pipeline engineered to distinguish authentic signatures from skilled forgeries through geometric, statistical, and contour feature extraction.",
        "projects.html#pillar-ai",
        "Pillar 1: Applied AI & Machine Learning",
    )
    + section(
        "Pipeline Architecture",
        '<p class="prose">The verification pipeline executes a multi-stage image processing sequence engineered to standardize scan variations and isolate ink strokes:</p>'
        '<figure class="diagram">'
        '<img src="diagrams/signature-pipeline.svg" width="1000" height="172" loading="lazy" alt="Preprocessing, 331-dimensional feature extraction, SVM classification, prediction with confidence score.">'
        '<figcaption>End-to-end inference flow: morphological noise reduction, geometric normalization, 331 handcrafted features, and RBF SVM scoring.</figcaption>'
        '</figure>'
        '<ol class="flow">'
        + case_row("1. Morphological Preprocessing", "Converts raw RGB scans to greyscale, applies Otsu dynamic thresholding to binarize ink strokes, and removes high-frequency paper grain noise.")
        + case_row("2. Geometric Normalization", "Calculates the signature bounding envelope and resizes the binary mask to standardized dimensions while preserving stroke aspect ratios.")
        + case_row("3. Feature Extraction (331-D)", "Extracts 331 handcrafted descriptors: 7 invariant Hu moments, horizontal/vertical projection profiles, pixel density grids, and contour curvature vectors.")
        + case_row("4. SVM Classification", "Projects extracted feature vectors into an RBF-kernel Support Vector Machine (SVM) trained under a writer-disjoint split protocol to detect genuine vs forged specimens.")
        + case_row("5. FastAPI & Demo Interface", "Wraps the inference pipeline in a lightweight FastAPI microservice connected to an interactive React signature canvas for real-time verification.")
        + '</ol>',
    )
    + section(
        "Evaluation & Empirical Results",
        '<div class="prose">'
        '<p>To prevent data leakage, the model was strictly evaluated under a <strong>writer-disjoint validation protocol</strong>, ensuring the test split contains signatures from individuals never seen during training.</p>'
        '<p><strong>Observed Performance:</strong> The RBF Support Vector Machine achieved superior discrimination on skilled forgeries compared to linear baselines, demonstrating the discriminative power of combining contour moments with projection density grids.</p>'
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
    "Document question-answering prototype featuring token-aware text chunking, Chroma dense vector indexing, and grounded retrieval.",
    intro(
        "Pillar 1 · Applied AI & Systems",
        "AI Research Assistant",
        "A modular retrieval-augmented generation (RAG) prototype engineered to index large document collections into a dense vector database and generate citation-grounded answers.",
        "projects.html#pillar-ai",
        "Pillar 1: Applied AI & Machine Learning",
    )
    + section(
        "RAG Ingestion & Retrieval Pipeline",
        '<p class="prose">The system operates as an end-to-end Python microservice orchestrating document parsing, token-aware chunking, vector embedding, and similarity search:</p>'
        '<figure class="diagram">'
        '<img src="diagrams/research-pipeline.svg" width="1000" height="172" loading="lazy" alt="Document ingestion, token-aware chunking, Chroma vector embedding, similarity search, prompt synthesis with source citations.">'
        '<figcaption>RAG processing sequence: document ingestion, token-aware chunking, dense vector embedding in Chroma, and citation-grounded synthesis.</figcaption>'
        '</figure>'
        '<ol class="flow">'
        + case_row("1. Document Ingestion", "Parses raw PDF, Markdown, and text files, stripping formatting noise and extracting structured section hierarchies.")
        + case_row("2. Token-Aware Chunking", "Splits long-form documents into semantically coherent chunks (500 tokens with 50-token overlap) to prevent boundary context clipping.")
        + case_row("3. Chroma Dense Indexing", "Generates dense mathematical embeddings for each chunk and indexes them into a persistent Chroma vector database collection.")
        + case_row("4. Similarity Retrieval", "Executes cosine distance search against indexed embeddings to retrieve the top-k most relevant text chunks for a given query.")
        + case_row("5. Grounded Prompt Synthesis", "Structures the retrieved context chunks into an augmented prompt harness, enforcing explicit inline source citations to prevent hallucinations.")
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

# 10. CLIENT WORK: client-work.html
PAGES["client-work.html"] = (
    "Client work",
    "Rehan Memon | Client Work",
    "Production client websites, administrative portals, and backend API services.",
    intro(
        "Pillar 2 · Client Deployments",
        "Selected Client Deployments",
        "A showcase of live, production web applications, educational portals, and backend API services built for real-world client operations.",
        "projects.html#pillar-client",
        "Pillar 2: Selected Client Deployments",
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
        '<h3>Girls Higher Secondary School Institutional Portal</h3>'
        '<p class="card-category-sub">Next.js 16 · React 19 · TypeScript · Supabase</p>'
        '<p>A modern educational institution platform providing academic program directories, event calendars, dynamic notices, and administrative management tools.</p>'
        '<div class="client-details">'
        '<h4>Technical Architecture & Personal Contribution:</h4>'
        '<ul class="prose-list">'
        '<li><strong>Administrative Routes:</strong> Implemented administrative pages under <code>src/app/admin</code> for dynamic management of events, notices, and student enquiries.</li>'
        '<li><strong>Serverless API Endpoints:</strong> Built Next.js Route Handlers (<code>/api/events</code>, <code>/api/enquiries</code>) backed by Supabase client querying.</li>'
        '<li><strong>Interactive UI Components:</strong> Engineered dynamic event countdown timers, responsive faculty directories, and accessible enquiry submission forms.</li>'
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
        '<li><strong>Enquiry Routing Service:</strong> Engineered an Express backend integration (<code>contactRoutes.js</code>, <code>contactController.js</code>) that receives customer inquiries and automatically appends rows into Google Sheets via the Google Sheets API.</li>'
        '<li><strong>Validation & Feedback:</strong> Implemented client-side phone/email input validation with instant visual submission feedback.</li>'
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
        + eyebrow("Non-Profit Deployment · ConnectFor / SAHASH India")
        + badge("Completed Deployment Prototype")
        + '</div>'
        '<h3>SAHASH NGO Voice & Conversational Assistant</h3>'
        '<p class="card-category-sub">Node.js · Express · Google Gemini API · Vector Store · Web Speech API</p>'
        '<p>A specialized conversational AI assistant engineered for SAHASH India via ConnectFor to assist community members, volunteers, and donors with verified organization details, programs, and social impact queries.</p>'
        '<div class="client-details">'
        '<h4>Technical Architecture & Personal Contribution:</h4>'
        '<ul class="prose-list">'
        '<li><strong>Grounded Semantic Matching:</strong> Engineered an in-memory vector store matching user queries against verified organization documents and FAQs, with intentional safe fallback preventing out-of-domain hallucinations.</li>'
        '<li><strong>Multimodal Voice & Text UI:</strong> Implemented a floating launcher with bidirectional speech synthesis and voice recognition via the browser Web Speech API.</li>'
        '<li><strong>Express Backend & Session Memory:</strong> Built modular API controllers with conversational context buffers and express rate-limiting middleware for abuse prevention.</li>'
        '</ul>'
        '</div>'
        '</article>',
    )
    + explore_more("client-work.html"),
)

# 11. AUTOMATION: automation.html
PAGES["automation.html"] = (
    "Automation",
    "Rehan Memon | Automation Systems",
    "Selected n8n workflow examples from lead capture, research, and document automation.",
    intro(
        "Pillar 3 · Workflow Automation",
        "n8n Automation Work",
        "Editor-tested and design-stage n8n examples from my Advfiction internship archive, with execution limits stated for each.",
        "projects.html#pillar-automation",
        "Pillar 3: AI & Workflow Automation",
        "page-intro-compact",
    )
    + section(
        "Map-based lead capture",
        '<article class="card" id="map-lead-capture">'
        '<div class="card-top">'
        + eyebrow("01 / Lead Capture")
        + badge("Editor run shown")
        + '</div>'
        '<h3>Apify Map Scraper to Google Sheets</h3>'
        '<p class="prose">A map-scraping canvas connects an Apify actor to dataset retrieval, a filter and a Google Sheets append step. The private editor capture shows green completion indicators through the final node, with five items displayed as appended.</p>'
        '<figure class="diagram"><img src="diagrams/automation-map-to-sheet.svg" width="1000" height="172" loading="lazy" alt="Illustrative sequence: map scraper, Apify actor, dataset retrieval, filter and Google Sheets append."><figcaption>Public diagram of the visible node sequence. The original canvas capture remains private.</figcaption></figure>'
        '<p class="card-highlight"><strong>Evidence limit:</strong> The screenshot supports an editor run for this small sample. It does not establish an active schedule, production deployment or a larger lead count.</p>'
        '</article>',
    )
    + section(
        "Company research and enrichment",
        '<article class="card" id="company-research">'
        '<div class="card-top">'
        + eyebrow("02 / Research Pipeline")
        + badge("Partial editor run")
        + '</div>'
        '<h3>PostgreSQL Research with Search Fallback</h3>'
        '<p class="prose">The captured canvas fetches company rows from PostgreSQL, splits a batch, checks prior processing and routes a search request toward an AI request and database save step.</p>'
        '<figure class="diagram"><img src="diagrams/automation-research.svg" width="1000" height="172" loading="lazy" alt="Illustrative sequence: PostgreSQL fetch, batching, deduplication, search fallback, AI request and database save."><figcaption>Illustrative path through the visible canvas; downstream completion is unverified.</figcaption></figure>'
        '<p class="card-highlight"><strong>Evidence limit:</strong> The editor shows early nodes and a search branch completing, followed by a warning at the AI request. It does not prove that the batch was enriched or saved.</p>'
        '</article>',
    )
    + section(
        "Lead report generation",
        '<article class="card" id="lead-report">'
        '<div class="card-top">'
        + eyebrow("03 / Document Automation")
        + badge("Design shown")
        + '</div>'
        '<h3>Google Sheets to PDF Lead Brief</h3>'
        '<p class="prose">Two private canvas views show a lead-row trigger, data formatting, Google Docs creation and text insertion, PDF export through Drive, and a Gmail notification. The later view adds a filter before document creation.</p>'
        '<figure class="diagram"><img src="diagrams/automation-report.svg" width="1000" height="172" loading="lazy" alt="Illustrative sequence: spreadsheet row, formatting and filter, document creation, PDF export and email notification."><figcaption>Public abstraction of the captured document workflow.</figcaption></figure>'
        '<p class="card-highlight"><strong>Evidence limit:</strong> The screenshots show design/configuration, not a completed PDF or delivered email.</p>'
        '</article>',
    )
    + section(
        "More workflow examples",
        '<p class="prose">The accompanying gallery documents other visible canvas designs, including scheduled publishing, human approval, news processing, image creation and an outreach test harness. Related views are grouped rather than counted as separate deployments.</p>'
        '<div class="card-actions">'
        + link("automation-evidence.html", "Explore the Workflow Gallery →", "button")
        + '</div>',
    )
    + explore_more("automation.html"),
)


def workflow_example(number, anchor, category, status, title, description, steps, evidence):
    step_html = "".join(
        f'<div class="evidence-node-col"><h4>{escape(label)}</h4><p>{escape(value)}</p></div>'
        for label, value in steps
    )
    body = (
        f'<article class="card evidence-card" id="{anchor}">'
        f'<div class="card-top">{eyebrow(f"Workflow example {number}")}{badge(status)}</div>'
        f'<h3>{escape(title)}</h3>'
        f'<p class="prose">{escape(description)}</p>'
        f'<div class="evidence-node-grid">{step_html}</div>'
        f'<p class="card-highlight"><strong>What the evidence shows:</strong> {escape(evidence)}</p>'
        '</article>'
    )
    return section(f'{number}. {category}', body)


# Eight selected public descriptions. The count refers to cards, not independently
# established production systems. Original n8n captures remain outside the build.
PAGES["automation-evidence.html"] = (
    "Automation Evidence Gallery",
    "Rehan Memon | Automation Workflow Gallery",
    "Selected n8n canvas examples, with editor-test and design status kept distinct.",
    intro(
        "Pillar 3 · Workflow Examples",
        "n8n Workflow Gallery",
        "Selected examples from my Advfiction internship archive. Each card describes visible canvas steps and states the limit of the available evidence; the original screenshots remain private.",
        "automation.html",
        "Workflow Automation Overview",
        "page-intro-compact",
    )
    + workflow_example(
        1, "wf-maps-scraper", "Lead Capture", "Editor run shown",
        "Apify Maps to Google Sheets",
        "A map-scraping flow obtains an Apify dataset, filters items and appends rows to a sheet.",
        [("Start", "Maps Scraper and Apify actor"), ("Transform", "Get dataset items and Filter"), ("Output", "Append row in sheet")],
        "The editor capture shows green indicators through the append node and five output items. Deployment and repeat runs are not established.",
    )
    + workflow_example(
        2, "wf-postgres-research", "Company Research", "Partial editor run",
        "PostgreSQL Search and AI Enrichment",
        "A company-research canvas fetches database rows, batches them, checks for prior processing and sends a search result toward an AI request.",
        [("Start", "Manual trigger and PostgreSQL fetch"), ("Transform", "Batch, deduplication and search fallback"), ("Output", "AI request followed by PostgreSQL save node")],
        "Early nodes and one search branch show completed indicators; the AI request has a warning and downstream save is not shown as completed.",
    )
    + workflow_example(
        3, "wf-lead-dossier", "Document Automation", "Design shown",
        "Lead Row to PDF Brief",
        "Two canvas views show a sheet-triggered lead-report flow; the later view adds a filter before document generation.",
        [("Start", "Sheet row or subworkflow trigger"), ("Transform", "Format lead data and create Google Doc"), ("Output", "Export PDF and Gmail notification nodes")],
        "The screenshots show a configured route, not a generated document, delivered email or production run.",
    )
    + workflow_example(
        4, "wf-instagram-api", "Scheduled Publishing", "Design shown",
        "Instagram Scheduling Canvas",
        "A publishing design reads approved scheduled posts, checks timing, creates an Instagram media container and routes toward publish and status-update nodes.",
        [("Start", "Schedule or subworkflow trigger"), ("Transform", "Approved-post lookup and eligibility check"), ("Output", "Meta publish, sheet update and notification nodes")],
        "The editor view shows the design and a warning on a notification node. A successful post or connected client account is not established.",
    )
    + workflow_example(
        5, "wf-telegram-bot", "Human Approval", "Design shown",
        "Telegram Review and Approval",
        "A review flow reads candidate items from a sheet, sends a Telegram message, waits for an approval decision and branches to sheet status updates.",
        [("Start", "Schedule or subworkflow trigger"), ("Transform", "Loop, Telegram message and Wait"), ("Output", "Approve/reject branches and confirmation")],
        "Two supplied captures are byte-identical views of this design. Neither proves that a reviewer responded or that a downstream publication occurred.",
    )
    + workflow_example(
        6, "wf-news-prompt", "News Processing", "Design shown",
        "News Sources to AI Summary",
        "A canvas combines two news-search requests, merges results, transforms them with JavaScript and routes an AI-generated result to a sheet.",
        [("Start", "Schedule or subworkflow trigger"), ("Transform", "Two HTTP sources, merge, JavaScript and AI request"), ("Output", "Append row in sheet")],
        "A design view shows the node sequence; there are no visible execution indicators or verified generated outputs.",
    )
    + workflow_example(
        7, "wf-social-orchestrator", "Generative Media", "Design shown",
        "Caption to Image Asset",
        "A related canvas reads captions from a sheet, calls an image-generation API, uploads the result to Drive and writes its URL back to the sheet.",
        [("Start", "Manual or subworkflow trigger"), ("Transform", "Caption loop and image-generation request"), ("Output", "Drive upload and sheet update nodes")],
        "The design is visible, but successful image generation and asset sharing are not shown. It may be a stage of a larger content workflow.",
    )
    + workflow_example(
        8, "wf-subworkflow-router", "Outreach Prototype", "Test harness design",
        "AI Outreach and Team Notification Skeleton",
        "A mock-lead test canvas branches on qualification and sketches an AI outreach message, email action and team notification.",
        [("Start", "Manual trigger with mock lead data"), ("Transform", "Qualification branch and AI request"), ("Output", "Gmail and Slack nodes")],
        "The canvas labels itself a skeleton; communication nodes show configuration warnings. No live outreach or sent messages are established.",
    )
    + explore_more("automation-evidence.html"),
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
    '<p class="eyebrow">Official Verification Archive</p>'
    '<h2>Google Drive Certificate Archive</h2>'
    '<p class="status-desc">Records in this library comprise primary-document verified government certifications (ISRO/IIRS), university extension awards (DLLE, EMSA), and accredited course completions, alongside enterprise job simulations and competitive nominations.</p>'
    '<div class="card-actions" style="margin-top: 1rem;">'
    + link(DRIVE_CREDENTIALS_URL, "Open Google Drive Verification Archive ↗", "button", external=True)
    + '</div>'
    '</div>'
    '<h2>Browse Credential Records</h2>'
    '<div class="filter-pills" role="tablist" aria-label="Credential Domain Filter">'
    '<button type="button" class="filter-pill active" data-filter-domain="all">All Records</button>'
    '<button type="button" class="filter-pill" data-filter-domain="geospatial & remote sensing">Geospatial & Remote Sensing</button>'
    '<button type="button" class="filter-pill" data-filter-domain="ai, ml & data science">AI, ML & Data Science</button>'
    '<button type="button" class="filter-pill" data-filter-domain="generative ai & automation">Generative AI & Automation</button>'
    '<button type="button" class="filter-pill" data-filter-domain="software engineering">Software Engineering</button>'
    '<button type="button" class="filter-pill" data-filter-domain="professional development">Professional Development</button>'
    '<button type="button" class="filter-pill" data-filter-domain="academic & extension honors">Academic Honors & DLLE</button>'
    '</div>'
    '<div class="filter-bar">'
    '<label for="credentialSearch">Search credentials</label>'
    '<input id="credentialSearch" type="search" placeholder="Search by title, issuer, keyword..." data-filter-search>'
    '<label for="credentialType">Type</label>'
    '<select id="credentialType" data-filter-type>'
    '<option value="">All Types</option>'
    '<option>Government Training</option>'
    '<option>Industry Program</option>'
    '<option>Enterprise Simulation</option>'
    '<option>Technical Masterclass</option>'
    '<option>Course Certification</option>'
    '<option>Hands-on Bootcamp</option>'
    '<option>Internship Credential</option>'
    '<option>University Extension Award</option>'
    '<option>Institutional Leadership</option>'
    '<option>National Examination</option>'
    '</select>'
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
        '<p>All listed credentials are authenticated by verified government certificates, official institutional letters, or digital verification IDs from:</p>'
        '<ul class="prose-list">'
        '<li><strong>ISRO / IIRS Outreach:</strong> Indian Institute of Remote Sensing (Dehradun), Department of Space, Government of India.</li>'
        '<li><strong>BCG X via Forage:</strong> Boston Consulting Group enterprise simulation verification.</li>'
        '<li><strong>University of Mumbai DLLE:</strong> Department of Lifelong Learning and Extension formal certification.</li>'
        '<li><strong>Nasscom Foundation & Zikshaa:</strong> Industry partner machine learning certification.</li>'
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
        '<article class="card clickable-card" id="sih-dbtdecoders">'
        '<div class="card-top">'
        + eyebrow("SIH 2025 · Team DBTDecoders")
        + badge("Round 1 Winner & Nominee")
        + '</div>'
        '<h3><a class="card-main-link" href="#sih-dbtdecoders">SIH 2025: Round 1 College Winner & Principal Nomination</a></h3>'
        f'<p class="prose">Selected as the internal college round winner and officially nominated by the Principal of <a class="text-link" href="{COLLEGE_URL}" target="_blank" rel="noopener noreferrer">{COLLEGE_NAME_SHORT}</a> on 23 September 2025 (Ref: <code>VC/SFC/2025-26/0604</code>) as a core member of Team DBTDecoders representing the institution at <strong>Smart India Hackathon 2025</strong>.</p>'
        '<p class="prose">Engineered a conversational AI assistant for the National Scholarship Portal (NSP / DBT scheme) providing automated eligibility guidance and verified compliance retrieval.</p>'
        '<p class="meta">Verified by official Principal-signed nomination letter and demonstration video.</p>'
        '</article>'
        '<article class="card clickable-card" id="karigar-setu">'
        '<div class="card-top">'
        + eyebrow("SIH 2026 · Team Echo Logic")
        + badge("Selected Architecture")
        + '</div>'
        '<h3><a class="card-main-link" href="#karigar-setu">SIH 2026: KARIGAR-SETU Artisan Platform (PS SIH26090)</a></h3>'
        '<p class="prose">Selected team architecture for Problem Statement SIH26090 (Heritage & Culture theme). Designed an AI-powered smart cataloging and direct marketplace mobile application for marginalized artisans.</p>'
        '<p class="prose">Engineered the technical blueprint incorporating on-device MobileNet/TensorFlow.js computer vision for product image enhancement, Google Gemini Flash API for catalog generation, and Web Speech API multilingual voice assistance.</p>'
        '<p class="meta">Verified by official SIH idea submission presentation and architecture blueprint.</p>'
        '</article>'
        '</div>',
    )
    + section(
        "Academic Examination Distinctions (VESASC Autonomous)",
        '<article class="card">'
        '<div class="card-top">'
        + eyebrow("B.Sc. Artificial Intelligence · University of Mumbai")
        + badge("Official ERP Marksheet Verified")
        + '</div>'
        '<h3>Consistent High-Honors Academic Performance (Semesters I–IV)</h3>'
        '<p class="prose">Cumulative academic performance across 88 completed credits at Vivekanand Education Society\'s College of Arts, Science & Commerce (Autonomous):</p>'
        '<div class="grid two" style="margin-top: 1rem;">'
        '<div class="evidence-node-col">'
        '<h4>Aggregated Degree Standing</h4>'
        '<ul>'
        '<li><strong>Cumulative CGPA:</strong> 8.14 / 10.0 (Across Semesters I–IV)</li>'
        '<li><strong>Semester IV SGPA:</strong> 9.27 / 10.0 (Grade O Distinction)</li>'
        '<li><strong>Semester III SGPA:</strong> 8.18 / 10.0 (Grade A+ Standing)</li>'
        '<li><strong>Total Earned Credits:</strong> 88.00 / 88.00 Completed</li>'
        '</ul>'
        '</div>'
        '<div class="evidence-node-col">'
        '<h4>Verified Coursework Scores (Out of 50)</h4>'
        '<ul>'
        '<li><strong>AI in IoT:</strong> 49/50 (98.00%, Grade O)</li>'
        '<li><strong>Web Programming (React & Angular):</strong> 49/50 (98.00%, Grade O)</li>'
        '<li><strong>GenAI & Prompt Engineering:</strong> 47/50 (94.00%, Grade O)</li>'
        '<li><strong>Data Analytics using Python:</strong> 47/50 (94.00%, Grade O)</li>'
        '<li><strong>AI in Drone Technology:</strong> 46/50 (92.00%, Grade O)</li>'
        '</ul>'
        '</div>'
        '</div>'
        '<p class="meta" style="margin-top: 1rem;">Authenticated by official college ERP examination marksheets (Seat: 24FA128 & 25SA134).</p>'
        '</article>',
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
        '</article>',
    )
    + section(
        "Institutional Governance & Leadership",
        '<div class="grid two">'
        '<article class="card">'
        + eyebrow("VESASC (Autonomous) · 2024–2025")
        + '<h3>EMSA Technical & Media Committee</h3>'
        '<p class="prose">Elected member of the Electronics & Media Student Association (EMSA) executive committee. Organized technical workshops, managed digital media broadcasting, and coordinated inter-collegiate student events.</p>'
        '</article>'
        '<article class="card">'
        + eyebrow("SEBI & NISM · October 2024")
        + '<h3>National Financial Literacy Examination</h3>'
        '<p class="prose">Achieved a <strong>perfect 100% score</strong> in the national World Investor Week examination administered under the joint auspices of the Securities and Exchange Board of India (SEBI) and NISM at VESASC.</p>'
        '</article>'
        '</div>',
    )
    + explore_more("activities.html"),
)

# 15. CONTACT: contact.html
PAGES["contact.html"] = (
    "Contact",
    "Rehan Memon | Contact",
    "Get in touch for Applied AI, full-stack development, and workflow automation opportunities.",
    intro(
        "Contact",
        "Let's Build Together",
        "I am actively exploring opportunities in Applied AI Engineering, Machine Learning, Full-Stack Backend Development, and Workflow Automation. Reach out through any of the direct channels below.",
    )
    + section(
        "Curriculum Vitae",
        '<article class="card resume-hero-card">'
        '<div class="card-top">'
        + eyebrow("Verified Candidate Credentials")
        + badge("Available Online & PDF")
        + '</div>'
        '<h3>Professional Resume</h3>'
        f'<p class="prose">Authoritative technical resume personally maintained by Rehan in Google Docs, detailing engineering projects, commercial client deployments, n8n automations, academic honors at <a class="text-link" href="{COLLEGE_URL}" target="_blank" rel="noopener noreferrer">{COLLEGE_NAME_SHORT}</a> (9.27 SGPA), and verified skill sets.</p>'
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
        + f'<p>{link(f"mailto:{EMAIL}", EMAIL)}</p>'
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
    "jobTitle": "Applied AI Engineer & Software Developer",
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
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{escape(description, quote=True)}">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{escape(title, quote=True)}">
  <meta property="og:description" content="{escape(description, quote=True)}">
  <meta property="og:url" content="{SITE_URL}/{filename}">
  <meta property="og:image" content="{SITE_URL}/assets/social-card.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <link rel="canonical" href="{SITE_URL}/{filename}">
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
      <p>Rehan Juned Memon · Applied AI &amp; Software Engineering</p>
      <div class="footer-links">
        {link('projects.html', 'Projects')}
        {link('experience.html', 'Experience')}
        {link('automation-evidence.html', 'Evidence Gallery')}
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
