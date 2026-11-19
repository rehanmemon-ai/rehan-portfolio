"""Dependency-free structural checks for generated static pages."""

from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
import re
from urllib.parse import urlsplit

from build_site import CREDENTIALS, IIRS_PUBLIC_KEYS, PAGES, PROJECTS, ROOT, SITE_URL


EXPECTED_WORKFLOWS = [
    "wf-instagram-api", "wf-news-prompt", "wf-social-publisher",
    "wf-subworkflow-router", "wf-social-orchestrator", "wf-itinerary-proposal",
    "wf-maps-scraper", "wf-lead-dossier", "wf-postgres-research",
    "wf-telegram-bot",
]
EXPECTED_PILLARS = {
    "AI & Machine Learning Systems": 5,
    "Client & Collaborative Engineering": 5,
    "AI & Workflow Automation": 4,
}


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.duplicate_ids = set()
        self.hrefs = []
        self.assets = []
        self.headings = []
        self.missing_alts = 0
        self.unsafe_new_tabs = 0
        self.canonical = ""
        self.description = ""
        self.title_text = ""
        self.in_title = False
        self.h1_count = 0
        self.title_count = 0

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if values.get("id"):
            if values["id"] in self.ids:
                self.duplicate_ids.add(values["id"])
            self.ids.add(values["id"])
        if tag == "a" and values.get("href"):
            self.hrefs.append(values["href"])
            if values.get("target") == "_blank" and not {"noopener", "noreferrer"}.issubset(set(values.get("rel", "").split())):
                self.unsafe_new_tabs += 1
        if tag in {"script", "link", "img"}:
            path = values.get("src") or values.get("href")
            if path and not urlsplit(path).scheme:
                self.assets.append(path)
        if tag == "link" and values.get("rel") == "canonical":
            self.canonical = values.get("href", "")
        if tag == "meta" and values.get("name") == "description":
            self.description = values.get("content", "")
        if tag == "img" and "alt" not in values:
            self.missing_alts += 1
        if re.fullmatch(r"h[1-6]", tag):
            self.headings.append(int(tag[1]))
        if tag == "h1":
            self.h1_count += 1
        if tag == "title":
            self.title_count += 1
            self.in_title = True

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False

    def handle_data(self, data):
        if self.in_title:
            self.title_text += data


def main():
    errors = []
    if len(PAGES) != 17:
        errors.append(f"expected 17 routes, found {len(PAGES)}")
    if len(PROJECTS) != 14 or Counter(p["pillar"] for p in PROJECTS) != EXPECTED_PILLARS:
        errors.append("expected 14 projects in 5/5/4 pillar allocation")
    if len(CREDENTIALS) != 48:
        errors.append(f"expected 48 credential records, found {len(CREDENTIALS)}")
    iirs_records = [c for c in CREDENTIALS if c["issuer"] == "IIRS / ISRO Outreach"]
    if len(iirs_records) != 21 or len(IIRS_PUBLIC_KEYS) != 21:
        errors.append("expected 21 IIRS records and public copies")
    for record, key in zip(iirs_records, IIRS_PUBLIC_KEYS):
        expected_pdf = f"assets/documents/iirs-outreach/iirs-{key}-participation.pdf"
        if record.get("public_pdf") != expected_pdf or not (ROOT / expected_pdf).is_file():
            errors.append(f"IIRS public document mapping missing: {record['title']}")
        if key.isdigit() and key not in {"1046", "1048"} and f"Course {key}" not in record["title"]:
            errors.append(f"IIRS title-to-document mapping mismatch: {record['title']}")
    seen_titles = set()
    for name in PAGES:
        page = ROOT / name
        parser = PageParser()
        text = page.read_text(encoding="utf-8")
        parser.feed(text)
        if parser.h1_count != 1 or parser.title_count != 1 or "main" not in parser.ids:
            errors.append(f"{name}: heading/title/main structure")
        if parser.duplicate_ids:
            errors.append(f"{name}: duplicate IDs {sorted(parser.duplicate_ids)}")
        if parser.missing_alts or parser.unsafe_new_tabs:
            errors.append(f"{name}: missing image alt or unsafe new-tab link")
        if any(b > a + 1 for a, b in zip(parser.headings, parser.headings[1:])):
            errors.append(f"{name}: heading level skip")
        expected_canonical = f"{SITE_URL}/" + ("automation.html" if name == "automation-evidence.html" else "" if name == "index.html" else name)
        if parser.canonical != expected_canonical or not parser.description.strip():
            errors.append(f"{name}: canonical or description")
        if parser.title_text in seen_titles or not parser.title_text.strip():
            errors.append(f"{name}: duplicate or empty title")
        seen_titles.add(parser.title_text)
        if re.search(r"[A-Za-z]:\\(?:Users|_Rehan|Documents)", text):
            errors.append(f"{name}: local machine path")
        for url in parser.hrefs + parser.assets:
            parts = urlsplit(url)
            if parts.scheme or url.startswith("//"):
                continue
            if parts.path.startswith("/"):
                errors.append(f"{name}: root-relative local path {url}")
            target = page.parent / parts.path if parts.path else page
            if not target.is_file():
                errors.append(f"{name}: missing {url}")
            if parts.fragment:
                target_parser = PageParser()
                if target.is_file():
                    target_parser.feed(target.read_text(encoding="utf-8"))
                    if parts.fragment not in target_parser.ids:
                        errors.append(f"{name}: missing #{parts.fragment} in {target.name}")
    automation = (ROOT / "automation.html").read_text(encoding="utf-8")
    index_ids = re.findall(r'<a href="#(wf-[^"]+)" class="workflow-index-link"', automation)
    card_positions = [automation.find(f'id="{anchor}"') for anchor in EXPECTED_WORKFLOWS]
    if index_ids != EXPECTED_WORKFLOWS or -1 in card_positions or card_positions != sorted(card_positions):
        errors.append("automation: owner workflow order or card anchors")
    credential_text = (ROOT / "credentials.html").read_text(encoding="utf-8")
    type_select = credential_text.split('<select id="credentialType"', 1)[-1].split('</select>', 1)[0]
    option_types = set(re.findall(r"<option>([^<]+)</option>", type_select))
    if option_types != {c["kind"] for c in CREDENTIALS}:
        errors.append("credentials: type filter does not match credential records")
    sitemap = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
    if "automation-evidence.html" in sitemap:
        errors.append("sitemap: compatibility redirect must not be indexed")
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"Checked {len(PAGES)} pages: routes, assets, anchors and one H1 each")


if __name__ == "__main__":
    main()
