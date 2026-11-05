"""Render the static portfolio pages from reviewed, local content. No dependencies."""

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


def link(href, label, css="text-link", external=False):
    extra = ' target="_blank" rel="noopener noreferrer"' if external else ""
    return f'<a class="{css}" href="{escape(href, quote=True)}"{extra}>{escape(label)}</a>'


def eyebrow(label):
    return f'<p class="eyebrow">{escape(label)}</p>'


def intro(label, title, summary):
    return f'<section class="page-intro container">{eyebrow(label)}<h1>{escape(title)}</h1><p class="lead">{escape(summary)}</p></section>'


def section(title, body, sid=""):
    ident = f' id="{sid}"' if sid else ""
    return f'<section class="section container"{ident}><h2>{escape(title)}</h2>{body}</section>'


def badge(text):
    return f'<span class="badge">{escape(text)}</span>'


PROJECTS = [
    {
        "name": "Signature Verification AI",
        "category": "Computer vision",
        "status": "Research baseline",
        "summary": "An offline signature classification baseline built with image preprocessing, handcrafted features and a support vector machine.",
        "route": "signature-verification.html",
        "repo": SIGNATURE,
    },
    {
        "name": "AI Research Assistant",
        "category": "Generative AI / RAG",
        "status": "In progress",
        "summary": "A document question-answering system with ingestion, chunking, Chroma retrieval and citation mapping components. End-to-end evaluation remains open.",
        "route": "ai-research-assistant.html",
        "repo": RESEARCH,
    },
]

EXPERIENCE = [
    {
        "name": "Advfiction Private Limited",
        "role": "Web Development Intern · AI Automation Developer Intern",
        "dates": "Apr–Sep 2026 · concurrent tracks",
        "summary": "Contributed to collaborative website and lead-API work while separately developing and prototyping n8n automation stages.",
        "route": "advfiction.html",
    },
    {
        "name": "AlgoDevOpss",
        "role": "Full-Stack Development Intern",
        "dates": "May–Aug 2026 · certified phase",
        "summary": "Worked on KJSIEIT EXTC Pedagogy and Result Analysis pages and a separate PHP/CMS prototype.",
        "route": "algodevopss.html",
    },
    {
        "name": "AwareWolf",
        "role": "Content Operating System Intern",
        "dates": "Sep–Oct 2026 · documented pilot period",
        "summary": "Contributed to a JSONL media and storyboard pilot and investigated separate Legacy rendering and image-import workflows.",
        "route": "awarewolf.html",
    },
]

CREDENTIALS = [
    ("Application of AI/ML Model for Specific Crop Acreage Mapping", "IIRS / ISRO Outreach", "2 Apr 2025", "Workshop participation", "AI / ML", "One-day online workshop. Participation certificate; not employment or a course qualification."),
    ("Advanced Image Analysis for Geospatial Professionals", "IIRS / ISRO Outreach", "22 Aug 2025", "Workshop participation", "Image analysis", "One-day online workshop. Participation certificate; not employment or a course qualification."),
    ("GenAI Job Simulation", "BCG X via Forage", "15 Sep 2025", "Job simulation", "Generative AI", "Forage-issued completion covering data extraction/analysis and an AI-powered financial chatbot task. Not BCG X employment."),
    ("Coding-track Micro-Internship Program", "Talerang · Cloudwrk partner", "Date not printed on certificate", "Micro-internship", "Coding", "Certificate of completion with PASS grade. The visible credential names Talerang and Cloudwrk; it does not establish EY employment."),
    ("Certificate of Extension Work", "University of Mumbai DLLE", "30 Apr 2026", "Extension work", "Community", "Certifies at least 120 hours of annual extension activities in academic year 2025–26. The certificate is kept private."),
]


def project_card(item):
    return (f'<article class="card project-card" data-filter-card data-category="{escape(item["category"], quote=True)}">'
            f'{eyebrow(item["category"])}<h3>{escape(item["name"])}</h3>'
            f'<p>{escape(item["summary"])}</p><p class="meta">{escape(item["status"])}</p>'
            f'<div class="card-actions">{link(item["route"], "Read case study", "button button-small")}'
            f'{link(item["repo"], "View repository ↗", external=True)}</div></article>')


def experience_card(item):
    return (f'<article class="card">{eyebrow(item["dates"])}<h3>{escape(item["name"])}</h3>'
            f'<p class="meta">{escape(item["role"])}</p><p>{escape(item["summary"])}</p>'
            f'{link(item["route"], "Explore contribution →")}</article>')


def credential_card(item):
    title, issuer, date, kind, subject, detail = item
    search = " ".join(item).lower()
    return (f'<article class="card credential-card" data-filter-card data-issuer="{escape(issuer, quote=True)}" '
            f'data-type="{escape(kind, quote=True)}" data-subject="{escape(subject, quote=True)}" '
            f'data-search="{escape(search, quote=True)}">{eyebrow(kind)}<h3>{escape(title)}</h3>'
            f'<p class="meta">{escape(issuer)} · {escape(date)}</p>'
            f'<details><summary>View credential details</summary><p>{escape(detail)}</p>'
            '<p class="note">Original document preview and download are unavailable until a redacted public copy is approved.</p>'
            '</details></article>')


def case_row(step, text):
    return f'<li><strong>{escape(step)}</strong><span>{escape(text)}</span></li>'


PAGES = {}

PAGES["index.html"] = (
    "Home", "Rehan Juned Memon — Applied AI & Software Engineering",
    "Rehan Juned Memon is a B.Sc. Artificial Intelligence student working across machine learning, Python and software engineering.",
    '<section class="hero container"><div>' + eyebrow("Applied AI · Python · Software engineering") +
    '<h1>Rehan Juned Memon<span class="accent">.</span></h1>'
    '<p class="hero-lead">I build and investigate practical AI and software systems, from computer vision baselines to document retrieval and web applications.</p>'
    '<p class="meta">B.Sc. Artificial Intelligence · VESASC (Autonomous) · 2024–2027 (in progress)</p>'
    '<div class="actions">' + link("projects.html", "Explore projects", "button") + link("experience.html", "Experience", "button button-quiet") + link("contact.html", "Contact me →") + '</div>'
    '</div><aside class="hero-aside" aria-label="Featured work"><p class="eyebrow">Start with the evidence</p>'
    '<h2>Two public technical case studies</h2><p>Inspect implementation details, scope and open limitations before drawing conclusions.</p>'
    + link("signature-verification.html", "Signature Verification →") + link("ai-research-assistant.html", "AI Research Assistant →") + '</aside></section>'
    + section("Selected engineering work", '<div class="grid two">' + "".join(project_card(p) for p in PROJECTS) + '</div>', "selected-work")
    + section("Experience in context", '<div class="grid three">' + "".join(experience_card(e) for e in EXPERIENCE) + '</div>' +
              '<p class="section-end">' + link("experience.html", "View all experience →") + ' · ' + link("client-work.html", "Selected client deployments →") + ' · ' + link("automation.html", "AI & workflow automation →") + '</p>')
    + section("Learning and recognition", '<div class="grid two"><article class="card"><h3>Academic work</h3><p>B.Sc. Artificial Intelligence in progress. Semester IV SGPA: 9.27/10; cumulative CGPA through Semester IV: 8.14/10.</p>' + link("about.html", "About my background →") + '</article><article class="card"><h3>Selected training</h3><p>IIRS workshop participation and a BCG X job simulation via Forage are listed with their exact credential types.</p>' + link("credentials.html", "Browse credentials →") + '</article></div>')
)

PAGES["about.html"] = (
    "About", "About Rehan Memon — Applied AI & Software Engineering",
    "Education, technical focus and background for Rehan Juned Memon.",
    intro("About", "A practical engineering path", "I am studying Artificial Intelligence at VESASC (Autonomous), University of Mumbai, and use projects to connect ML methods with usable software.")
    + section("Education", '<div class="prose"><p><strong>B.Sc. Artificial Intelligence</strong> · 2024–2027 (in progress).</p><p>The March 2026 Semester IV record shows a <strong>9.27/10 SGPA</strong> and <strong>8.14/10 cumulative CGPA</strong> through that semester. The same record shows 98/100 in AI in IoT and 94/100 in Generative AI & Prompt Engineering.</p><p>The source marksheet contains student identifiers, so it is not published here.</p></div>')
    + section("What I work on", '<div class="grid three"><article class="card"><h3>Machine learning</h3><p>Computer vision preprocessing, feature engineering and classical-model evaluation in the Signature Verification baseline.</p></article><article class="card"><h3>Python and retrieval</h3><p>Document ingestion, chunking, vector retrieval and citations in the separate AI Research Assistant project.</p></article><article class="card"><h3>Web and automation</h3><p>Frontend and API contributions in team projects, plus scoped n8n workflow experiments during the Advfiction internship.</p></article></div>')
    + section("Working principles", '<p class="prose">I describe a prototype as a prototype, identify team contributions, and keep unverified performance claims out of public case studies. The project pages document both implementation and gaps.</p>' + link("projects.html", "Read the case studies →"))
)

PAGES["experience.html"] = (
    "Experience", "Experience — Rehan Memon",
    "Scoped engineering contributions at Advfiction, AlgoDevOpss and AwareWolf.",
    intro("Experience", "Work, with the boundaries visible", "Three documented internship contexts. The pages distinguish my contribution from team ownership and separate implemented work from prototypes.")
    + section("Internship work", '<div class="grid three">' + "".join(experience_card(e) for e in EXPERIENCE) + '</div>')
    + section("How these records are presented", '<p class="prose">Periods are limited to documented phases where an ongoing status is unresolved. Client assets, repositories and customer data are not reproduced. The Advfiction web and automation tracks overlap in time and are not counted as separate months.</p>')
)

PAGES["advfiction.html"] = (
    "Advfiction", "Advfiction experience — Rehan Memon",
    "Two concurrent Advfiction internship workstreams: collaborative web development and scoped AI automation.",
    intro("Experience / Advfiction", "Two workstreams, one internship period", "Apr–Sep 2026 · Web Development Intern and AI Automation Developer Intern. The tracks overlap; they do not represent twice the experience duration.")
    + section("Contribution overview", '<div class="grid two"><article class="card"><p class="eyebrow">01 / Web development</p><h3>Interface and lead API work</h3><p>Contributed layouts to a collaborative website revamp and worked on an Express lead API with validation and Supabase insertion. The source review identifies specific commits; it does not prove sole ownership of the site or successful live contact submissions.</p><p class="meta">Team context: company web team. Other LMS and client-site assignments require project-specific attribution before publication.</p></article><article class="card"><p class="eyebrow">02 / AI automation</p><h3>n8n workflow stages</h3><p>Developed lead-capture and reporting stages using Apify, filtering, Google Sheets and PDF-oriented steps. Human-review, Telegram and publishing API canvases were prototypes or designs in the available evidence.</p><p class="meta">The screenshot index describes an Apify/Sheets editor test of five items. It does not establish production deployment, distinct workflow count or unique leads.</p></article></div>')
    + section("Automation flow and evidence", '<ol class="flow">' + case_row("Collect", "Apify-based capture is described in the editor index.") + case_row("Transform", "Filter and map fields before a Google Sheets test append.") + case_row("Report", "PDF dossier stages are documented as workflow designs; successful end-to-end output remains unverified.") + case_row("Review", "Telegram approval and Meta publishing canvases are prototypes, not proven live publishing.") + '</ol>')
    + section("Related work", '<p class="prose">The collaborative LMS, company website and selected client deployments are grouped on the client work page. Automation experiments are described in their own collection, with evidence status attached to each stage.</p>' + link("client-work.html", "Explore client work →") + ' · ' + link("automation.html", "Explore automation →"))
    + section("Boundaries", '<p class="prose">No client records, unredacted workflow screenshots, credentials or private source links are shown. A derivative screenshot index is weaker than original exports and run logs. These would be needed for a deeper public technical walkthrough.</p>')
)

PAGES["algodevopss.html"] = (
    "AlgoDevOpss", "AlgoDevOpss experience — Rehan Memon",
    "KJSIEIT EXTC page contributions and a separate PHP/CMS prototype during an AlgoDevOpss internship.",
    intro("Experience / AlgoDevOpss", "Department pages and a PHP prototype", "Full-Stack Development Intern · certified phase 1 May–31 Aug 2026. Work after the certificate period has not been presented as independently certified.")
    + section("KJSIEIT EXTC contribution", '<div class="prose"><p>Worked within a team repository on the <strong>Pedagogy</strong> and <strong>Result Analysis</strong> department pages. The local Next.js/TypeScript source contains dedicated `page.tsx` routes and a typed `results-data.ts` module for result tables and examination cards.</p><p>The pages import shared navigation, footer and heading components. Authorship headers name Rehan, while the broader site remains a collaborative institutional project. The short commit IDs cited in older reports remain unresolved as contribution proof.</p></div>')
    + section("Separate PHP/CMS prototype", '<p class="prose">A university field report describes modular PHP pages and a database-backed admin/CMS prototype. This is separate from the KJSIEIT Next.js work. The available evidence does not justify describing it as a complete deployed client system.</p>')
    + section("Boundaries", '<p class="prose">No claim is made that I built or deployed the full KJSIEIT site. Institutional screenshots, production links and private source are withheld pending attribution and publication review.</p>')
)

PAGES["awarewolf.html"] = (
    "AwareWolf", "AwareWolf experience — Rehan Memon",
    "Sanitised account of JSONL pilot and separate Legacy media workflow investigations.",
    intro("Experience / AwareWolf", "A media workflow pilot, with limits", "Content Operating System Intern · documented Sep–Oct 2026 workstream. Formal end or continuation status remains unresolved.")
    + section("JSONL pilot", '<p class="prose">Contributed to a React/TypeScript and FastAPI pilot around media-library search, authenticated previews and editable five-scene storyboards with revisions. This was collaborative pilot work, not a claim that the entire operating system was delivered or deployed.</p>')
    + section("Legacy workflow", '<p class="prose">Separately investigated FFmpeg/API render, trim, poll and save behavior, and validated JPEG/PNG image-import paths with focused checks. These investigations do not establish end-to-end renderer acceptance or live publishing.</p>')
    + section("Evaluation and disclosure", '<p class="prose">Reviewed generative-video approaches; evaluating tools is distinct from developing the underlying models. No private repository, client media, screenshots, database contents or internal endpoints are published here.</p>')
)

PAGES["projects.html"] = (
    "Projects", "Projects — Rehan Memon",
    "Evidence-backed public projects in computer vision and document retrieval.",
    intro("Projects", "Inspect the implementation", "A curated index of public projects with code links, current status and honest validation limits. Private client work remains under the relevant experience context.")
    + '<section class="section container"><h2>Public technical work</h2><div class="filter-bar"><label for="projectSearch">Search projects</label><input id="projectSearch" type="search" placeholder="Project or technique" data-filter-search><label for="projectCategory">Area</label><select id="projectCategory" data-filter-category><option value="">All areas</option><option>Computer vision</option><option>Generative AI / RAG</option></select></div><p class="filter-count" data-filter-count aria-live="polite"></p><div class="grid two" data-filter-list>'
    + "".join(project_card(p) for p in PROJECTS) + '</div><p class="no-results" data-no-results hidden>No projects match these filters.</p></section>'
    + section("Other work", '<p class="prose">Collaborative web deployments and n8n workflow stages are grouped separately so they are not confused with independently documented public repositories.</p>' + link("client-work.html", "Selected client deployments →") + ' · ' + link("automation.html", "AI & workflow automation →"))
)

PAGES["signature-verification.html"] = (
    "Signature Verification", "Signature Verification AI — case study",
    "Classical computer vision signature verification baseline using OpenCV features and an RBF SVM.",
    intro("Case study / Computer vision", "Signature Verification AI", "A classical offline handwritten-signature baseline. The public repository contains implementation and a README-reported evaluation; this page describes the method without claiming a reproduced score.")
    + section("My role and scope", '<p class="prose">Academic project implementation in the public `signature-verification` repository. The repository owner and code provenance do not by themselves partition every line of personal versus AI-assisted work. This page describes the inspected system, not sole authorship of every dependency or dataset.</p>')
    + section("Processing architecture", '<figure class="diagram"><img src="diagrams/signature-pipeline.svg" width="1000" height="172" loading="lazy" alt="Signature images flow through OpenCV preprocessing, 331 features, a scaled RBF SVM and writer-disjoint evaluation."><figcaption>Method shown in the public repository; evaluation results were not reproduced here.</figcaption></figure><ol class="flow">' + case_row("Input", "Genuine and forged signature images are loaded from an external CEDAR-format dataset.") + case_row("Preprocess", "OpenCV grayscale, blur, Otsu binarization, crop and 256 × 256 normalization.") + case_row("Represent", "331 handcrafted geometric, ink-density, projection and Hu-moment features.") + case_row("Classify", "StandardScaler and an RBF-kernel SVM are packaged in a model pipeline.") + case_row("Evaluate", "Writer-disjoint split logic is present in source; the dataset and reported metrics were not reproduced for this portfolio.") + '</ol>')
    + section("Application surface", '<p class="prose">The repository also contains a FastAPI backend and a React/TypeScript frontend for an interactive demonstration. The existence of these components is not evidence of a deployed service or a validated security review.</p>')
    + section("Validation and limits", '<div class="prose"><p>The repository includes dataset/split tests and an evaluation runner. The CEDAR data is external; dataset access and licensing were not assumed. The README lists accuracy and F1 values, but this portfolio does not present them as independently reproduced results.</p><p>The code and documented method are the evidence here. A repeatable evaluation with dataset provenance, pinned environment and test output would strengthen the case study.</p></div>')
    + section("Source", link(SIGNATURE, "Inspect the public repository ↗", "button", True))
)

PAGES["ai-research-assistant.html"] = (
    "AI Research Assistant", "AI Research Assistant — case study",
    "An in-progress document retrieval assistant with Chroma, citations and incomplete end-to-end evaluation.",
    intro("Case study / Retrieval", "AI Research Assistant", "An in-progress document question-answering system. Its current implementation and status are separate from the private Client Research Assistant Bot.")
    + section("My role and scope", '<p class="prose">The public repository contains Python ingestion, chunking, embedding, Chroma retrieval and citation-mapping modules, alongside a FastAPI backend. It remains in progress. The inspected dependency list does not establish LangChain use, so that technology is not claimed here.</p>')
    + section("Processing architecture", '<figure class="diagram"><img src="diagrams/research-pipeline.svg" width="1000" height="172" loading="lazy" alt="Documents are parsed, chunked, embedded in Chroma, retrieved and mapped to citations."><figcaption>Implemented components in the public repository; the complete service path still needs end-to-end validation.</figcaption></figure><ol class="flow">' + case_row("Ingest", "Parse supported documents and normalize text.") + case_row("Chunk", "Split content into retrievable sections.") + case_row("Embed & store", "Create embeddings and maintain an embedded Chroma vector index.") + case_row("Retrieve & cite", "Select relevant chunks and map answers back to source references.") + case_row("Evaluate", "End-to-end quality and CI coverage remain incomplete in the reviewed evidence.") + '</ol>')
    + section("Implemented and planned", '<div class="grid two"><article class="card"><h3>Implemented in source</h3><p>Document parsing and normalization, token-aware chunking, embedding and Chroma storage, workspace-scoped retrieval, citation mapping and API modules.</p></article><article class="card"><h3>Still to validate</h3><p>A complete ingestion-to-answer run, citation accuracy, answer quality, deployment readiness and repeatable integration coverage remain open.</p></article></div>')
    + section("Validation and limits", '<p class="prose">Components and tests exist, but mocked tests are not proof of a fully exercised ingestion-to-answer pipeline. No production deployment, latency, answer-quality score or reduced analyst time is claimed. The separate local pgvector/MinIO project is not represented here.</p>')
    + section("Source", link(RESEARCH, "Inspect the public repository ↗", "button", True))
)

PAGES["credentials.html"] = (
    "Credentials", "Credentials and training — Rehan Memon",
    "Curated workshop, job simulation, micro-internship and extension-work records.",
    intro("Credentials", "Training, classified precisely", "A selected set of records relevant to engineering and community work. Participation, simulation and micro-internship are distinct from employment or professional certification.")
    + '<section class="section container"><h2>Browse records</h2><div class="filter-bar"><label for="credentialSearch">Search</label><input id="credentialSearch" type="search" placeholder="Title or subject" data-filter-search><label for="credentialType">Type</label><select id="credentialType" data-filter-type><option value="">All types</option><option>Workshop participation</option><option>Job simulation</option><option>Micro-internship</option><option>Extension work</option></select><label for="credentialIssuer">Issuer</label><select id="credentialIssuer" data-filter-issuer><option value="">All issuers</option><option value="IIRS / ISRO Outreach">IIRS / ISRO Outreach</option><option value="BCG X via Forage">BCG X via Forage</option><option value="Talerang · Cloudwrk partner">Talerang · Cloudwrk partner</option><option value="University of Mumbai DLLE">University of Mumbai DLLE</option></select><label for="credentialSubject">Subject</label><select id="credentialSubject" data-filter-subject><option value="">All subjects</option><option>AI / ML</option><option>Image analysis</option><option>Generative AI</option><option>Coding</option><option>Community</option></select></div><p class="filter-count" data-filter-count aria-live="polite"></p><div class="grid two" data-filter-list>'
    + "".join(credential_card(c) for c in CREDENTIALS) + '</div><p class="no-results" data-no-results hidden>No credentials match these filters.</p></section>'
    + section("Document access", '<p class="prose">The original certificates include identifiers or require publication review. Details above provide a text preview; original PDF viewing and downloads are deliberately unavailable until redacted copies and sharing rights are approved.</p>')
)

PAGES["activities.html"] = (
    "Activities", "Activities and recognition — Rehan Memon",
    "Verified team nomination and university extension-work participation.",
    intro("Activities", "Participation with clear outcomes", "A focused record of activities supported by original institutional documents. A nomination is not presented as a competition victory.")
    + section("Smart India Hackathon 2025", '<article class="card"><p class="eyebrow">Team DBTDecoders · VESASC</p><h3>Institutional nomination</h3><p>A Principal-signed letter dated 23 September 2025 lists Rehan as a team member nominated for SIH 2025. The available original does not establish a Round 1 win, national selection or a finished personal chatbot contribution.</p><p class="meta">Team project · nomination verified · project/result details held for review</p></article>')
    + section("University extension work", '<article class="card"><p class="eyebrow">Academic year 2025–26</p><h3>DLLE Certificate of Extension Work</h3><p>The University of Mumbai certificate records at least 120 hours of annual extension activities. This is one academic year and separate from any field-project hours.</p><p class="meta">Original certificate retained privately because it includes personal details.</p></article>')
    + section("Further records", '<p class="prose">Campus design roles, NCC, SIH 2026 proposal details and other reported activities are held until attributable records and publication permissions are established.</p>')
)

PAGES["client-work.html"] = (
    "Client work", "Selected client deployments — Rehan Memon",
    "A scoped view of collaborative web and API work, with attribution limits.",
    intro("Client work", "Selected client deployments", "These live sites show project context. Source and commit evidence support specific contributions; a working URL alone does not establish sole authorship or a production outcome.")
    + section("Advfiction LMS", '<article class="card"><p class="eyebrow">Collaborative frontend and backend</p><h3>Lead management system</h3><p>The live frontend exposes a login screen. Local source uses static HTML, CSS and JavaScript with a Node/Express API and Supabase integration. Rehan-authored commits include a frontend production API configuration, backend CORS change and a public lead-submission API. Authenticated workflows and live lead delivery were not tested.</p><p class="meta">Contribution: specific frontend and API commits · team ownership</p><div class="card-actions">' + link("https://advfiction-lms.vercel.app/pages/login.html", "LMS frontend ↗", external=True) + link("https://advfiction-lms-backend.onrender.com/api/health", "API health endpoint ↗", external=True) + '</div></article>')
    + section("Advfiction company website", '<article class="card"><p class="eyebrow">Collaborative company website</p><h3>Website revamp and contact integration</h3><p>Local source is a static HTML/CSS/JavaScript site. Rehan-authored commits document UI changes and contact-form integration with the LMS backend. The live company website is reachable; this review did not submit the form or establish successful message delivery.</p><p class="meta">Contribution: UI and contact-integration commits · not sole site ownership</p>' + link("https://advfiction.vercel.app/", "Visit company website ↗", external=True) + '</article>')
    + section("LMS Girls Higher Secondary School", '<article class="card"><p class="eyebrow">Collaborative school website</p><h3>Website and admin modules</h3><p>The live site loads, and local Next.js/TypeScript/Supabase source contains Rehan-authored commits for admin pages and an events API fix. Other authors also contributed. The public homepage still displays placeholder principal content, so it is presented as a live preview rather than a validated official publication.</p><p class="meta">Contribution: identified admin and API commits · live backend behavior untested</p>' + link("https://girlshss.netlify.app/", "View live preview ↗", external=True) + '</article>')
    + section("Marthandam Star Honey", '<article class="card"><p class="eyebrow">Related live deployment · attribution pending</p><h3>Honey website</h3><p>The public site loads and displays a product catalogue. A local React/Vite/Tailwind candidate source exists, but the available evidence does not firmly tie specific commits or personal implementation scope to this deployment. It is listed for context, without an authorship claim.</p><p class="meta">Contribution and deployment linkage: unresolved</p>' + link("https://msh-website.netlify.app/", "View live site ↗", external=True) + '</article>')
    + section("Publication boundary", '<p class="prose">No client records, private repository links, form submissions, marketing counters or testimonials are reproduced. Client-site descriptions require continued Career HQ attribution and content review.</p>')
)

PAGES["automation.html"] = (
    "Automation", "AI and workflow automation — Rehan Memon",
    "Evidence-scoped n8n workflow stages and prototypes from client-oriented work.",
    intro("AI & workflow automation", "Workflow stages, with their status visible", "I have worked with n8n on lead, reporting and approval flows. The available screenshot index supports specific editor tests and designs; client deployment counts and production execution remain unverified.")
    + section("Map-based lead capture", '<article class="card"><p class="eyebrow">01 / Editor-tested flow</p><h3>Apify to Google Sheets</h3><p><strong>Problem:</strong> Organize candidate map-search records for review. <strong>Process:</strong> An Apify actor returns dataset items, a filter keeps selected records, and a Google Sheets node appends rows.</p><figure class="diagram"><img src="diagrams/automation-map-to-sheet.svg" width="1000" height="172" loading="lazy" alt="Map scraper start, Apify actor, dataset items, filter, then Google Sheets append."><figcaption>Redrawn from the workflow canvas; no original screenshot or client data is published.</figcaption></figure><p>The screenshot shows green checks through all five nodes and five items at the append step. This verifies an editor test, not unique leads or a production deployment.</p><p class="meta">Source: n8n(2).jpeg · contribution: user-supplied internship evidence, individual authorship unverified</p></article>')
    + section("Company research and enrichment", '<article class="card"><p class="eyebrow">02 / Partial execution</p><h3>Batch, check and research company records</h3><p><strong>Problem:</strong> Avoid repeated research across a company dataset. <strong>Process:</strong> A manual run fetches PostgreSQL rows, batches and checks records, then routes unprocessed items toward search, an AI request and a proposed save loop.</p><figure class="diagram"><img src="diagrams/automation-research.svg" width="1000" height="172" loading="lazy" alt="Manual start, PostgreSQL fetch, batch and deduplication, search, AI request, and an unverified save step."><figcaption>Early stages show execution; the save and loop are not shown completing.</figcaption></figure><p>The canvas displays a large fetched input count and early node checks. It does not establish completed enrichment, unique lead count or successful downstream storage.</p><p class="meta">Source: n8n.jpeg · contribution and deployment: unverified</p></article>')
    + section("Lead-report preparation", '<article class="card"><p class="eyebrow">03 / Design-stage workflow</p><h3>Document and PDF report flow</h3><p><strong>Problem:</strong> Prepare a reviewable report from lead records. <strong>Process:</strong> A Sheets event or subworkflow supplies data; the canvas formats and filters it, creates a document, exports a PDF and routes a notification.</p><figure class="diagram"><img src="diagrams/automation-report.svg" width="1000" height="172" loading="lazy" alt="Sheet event or subworkflow, format and filter, create document, export PDF, notify team; all design-stage."><figcaption>Proposed architecture; no generated PDF or delivered notification was verified.</figcaption></figure><p>A related canvas uses an AI and HTML-to-PDF path. The screenshots do not establish whether these alternatives were deployed or used for a client.</p><p class="meta">Sources: n8n(10).jpeg, n8n(12).jpeg and related n8n(13).jpeg · execution unverified</p></article>')
    + section("Related prototypes", '<p class="prose">Additional canvases show news and image preparation, Telegram approvals, scheduled social publishing and a mock-lead outreach skeleton. They are related stages or designs, not a demonstrated count of deployed systems. No successful live publishing or outreach is claimed.</p>')
    + section("Evidence needed next", '<p class="prose">Sanitized workflow exports, dated execution logs, deployment ownership records and client publication permission would support deeper public case studies. The screenshot set is not a count of distinct workflows or clients. No credentials, webhook URLs, customer records or original screenshots are published.</p>')
)

PAGES["contact.html"] = (
    "Contact", "Contact Rehan Memon",
    "Email and professional profile links for Rehan Juned Memon.",
    intro("Contact", "Start a conversation", "For Applied AI, Python, software engineering and automation opportunities, use the direct contact routes below.")
    + section("Direct channels", '<div class="grid three"><article class="card"><h3>Email</h3><p>Opens your email application.</p>' + link(f"mailto:{EMAIL}", EMAIL) + '</article><article class="card"><h3>GitHub</h3><p>Public repositories and source.</p>' + link(GITHUB, "GitHub profile ↗", external=True) + '</article><article class="card"><h3>LinkedIn</h3><p>Professional profile; sign-in may be required.</p>' + link(LINKEDIN, "LinkedIn profile ↗", external=True) + '</article><article class="card"><h3>LeetCode</h3><p>Coding practice profile.</p>' + link(LEETCODE, "LeetCode profile ↗", external=True) + '</article><article class="card"><h3>Kaggle</h3><p>Data science profile.</p>' + link(KAGGLE, "Kaggle profile ↗", external=True) + '</article></div><p class="note">External profile links open in a new tab.</p>')
    + section("Resume and form", '<p class="prose">A public resume download and message form are not offered yet. The latest resume PDF awaits explicit publication approval, and no approved message-delivery backend exists.</p>')
)

NAV = [
    ("index.html", "Home"), ("about.html", "About"), ("experience.html", "Experience"),
    ("projects.html", "Projects"), ("client-work.html", "Client work"), ("automation.html", "Automation"), ("credentials.html", "Credentials"),
    ("activities.html", "Activities"), ("contact.html", "Contact"),
]


def render(filename, item):
    label, title, description, body = item
    nav = "".join(f'<a href="{href}"' + (' aria-current="page"' if filename == href else "") + f'>{name}</a>' for href, name in NAV)
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{escape(description, quote=True)}">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{escape(title, quote=True)}">
  <meta property="og:description" content="{escape(description, quote=True)}">
  <meta name="theme-color" content="#f7f7f2">
  <title>{escape(title)}</title>
  <link rel="icon" type="image/svg+xml" href="favicon.svg">
  <link rel="stylesheet" href="site.css">
  <script src="site.js" defer></script>
</head>
<body>
  <a class="skip-link" href="#main">Skip to content</a>
  <header class="site-header">
    <div class="container header-inner">
      <a class="brand" href="index.html" aria-label="Rehan Memon, home">RM<span>.</span></a>
      <nav class="desktop-nav" aria-label="Primary">{nav}</nav>
      <div class="header-actions"><button id="themeToggle" class="icon-button" type="button" aria-label="Switch to dark theme"><span id="themeIcon" aria-hidden="true">Dark</span></button><button id="mobileMenuBtn" class="icon-button menu-button" type="button" aria-controls="mobileMenu" aria-expanded="false" aria-label="Open menu">Menu</button></div>
    </div>
    <nav id="mobileMenu" class="mobile-nav" aria-label="Mobile primary" hidden>{nav}</nav>
  </header>
  <main id="main">{body}</main>
  <footer class="site-footer"><div class="container footer-inner"><p>Rehan Juned Memon · Applied AI &amp; software engineering</p><div>{link('projects.html','Projects')}{link(f'mailto:{EMAIL}','Email')}</div></div></footer>
</body>
</html>
'''


def main():
    for filename, item in PAGES.items():
        (ROOT / filename).write_text(render(filename, item), encoding="utf-8", newline="\n")
    print(f"Rendered {len(PAGES)} static pages")


if __name__ == "__main__":
    main()
