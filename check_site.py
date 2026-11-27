"""Dependency-free structural, security, and metadata checks for generated static pages."""

import json
import re
from collections import Counter
from html import unescape
from html.parser import HTMLParser
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
WITHHELD_DRIVE_IDS = ("19y3Fa9zD8zqbLnZPS86rt8R5bQopky8A",)
ALLOWED_EXTERNAL_SCHEMES = {"https", "mailto"}


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.duplicate_ids = set()
        self.hrefs = []
        self.all_a_empty = False
        self.assets = []
        self.headings = []
        self.missing_alts = 0
        self.unsafe_new_tabs = 0
        self.canonical = ""
        self.og_url = ""
        self.og_image = ""
        self.robots = ""
        self.description = ""
        self.title_text = ""
        self.in_title = False
        self.h1_count = 0
        self.title_count = 0
        self.main_tabindex = None
        self.inline_style_count = 0
        self.json_ld_blocks = []
        self.in_json_ld = False
        self._json_buf = []

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if "style" in values:
            self.inline_style_count += 1
        if values.get("id"):
            if values["id"] in self.ids:
                self.duplicate_ids.add(values["id"])
            self.ids.add(values["id"])
        if tag == "main":
            self.main_tabindex = values.get("tabindex")
        if tag == "a":
            if "href" in values and not values["href"].strip():
                self.all_a_empty = True
            elif values.get("href"):
                self.hrefs.append(values["href"])
                if values.get("target") == "_blank" and not {"noopener", "noreferrer"}.issubset(set(values.get("rel", "").split())):
                    self.unsafe_new_tabs += 1
        if tag in {"script", "link", "img"}:
            path = values.get("src") or values.get("href")
            if path and not urlsplit(path).scheme:
                self.assets.append(path)
        if tag == "link" and values.get("rel") == "canonical":
            self.canonical = values.get("href", "")
        if tag == "meta" and values.get("property") == "og:url":
            self.og_url = values.get("content", "")
        if tag == "meta" and values.get("property") == "og:image":
            self.og_image = values.get("content", "")
        if tag == "meta" and values.get("name") == "robots":
            self.robots = values.get("content", "")
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
        if tag == "script" and values.get("type") == "application/ld+json":
            self.in_json_ld = True
            self._json_buf = []

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False
        if tag == "script" and self.in_json_ld:
            self.in_json_ld = False
            self.json_ld_blocks.append("".join(self._json_buf))

    def handle_data(self, data):
        if self.in_title:
            self.title_text += data
        if self.in_json_ld:
            self._json_buf.append(data)


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
    for record, key in zip(iirs_records, IIRS_PUBLIC_KEYS, strict=True):
        expected_pdf = f"assets/documents/iirs-outreach/iirs-{key}-participation.pdf"
        if record.get("public_pdf") != expected_pdf or not (ROOT / expected_pdf).is_file():
            errors.append(f"IIRS public document mapping missing: {record['title']}")
        if key.isdigit() and key not in {"1046", "1048"} and f"Course {key}" not in record["title"]:
            errors.append(f"IIRS title-to-document mapping mismatch: {record['title']}")

    css_text = (ROOT / "site.css").read_text(encoding="utf-8")
    defined_css_vars = set(re.findall(r"(--[a-z0-9-]+)\s*:", css_text))
    for used_var in re.findall(r"var\((--[a-z0-9-]+)(?:\s*,|\))", css_text):
        if used_var not in defined_css_vars:
            errors.append(f"site.css: undefined CSS custom property {used_var}")

    if not (ROOT / "assets/social-card.png").is_file():
        errors.append("assets/social-card.png missing")
    if not (ROOT / "theme-init.js").is_file():
        errors.append("theme-init.js missing")

    seen_titles = set()
    sitemap_expected = []
    for name in PAGES:
        page = ROOT / name
        parser = PageParser()
        text = page.read_text(encoding="utf-8")
        parser.feed(text)
        if parser.h1_count != 1 or parser.title_count != 1 or "main" not in parser.ids or parser.main_tabindex != "-1":
            errors.append(f"{name}: heading/title/main structure")
        if parser.duplicate_ids:
            errors.append(f"{name}: duplicate IDs {sorted(parser.duplicate_ids)}")
        if parser.all_a_empty:
            errors.append(f"{name}: empty href attribute detected")
        if parser.missing_alts or parser.unsafe_new_tabs:
            errors.append(f"{name}: missing image alt or unsafe new-tab link")
        if parser.inline_style_count:
            errors.append(f"{name}: {parser.inline_style_count} inline style attributes detected")
        for used_var in re.findall(r"var\((--[a-z0-9-]+)", text):
            if used_var not in defined_css_vars:
                errors.append(f"{name}: undefined CSS variable {used_var}")
        if any(b > a + 1 for a, b in zip(parser.headings, parser.headings[1:], strict=False)):
            errors.append(f"{name}: heading level skip")
        expected_canonical = f"{SITE_URL}/" + ("automation.html" if name == "automation-evidence.html" else "" if name == "index.html" else name)
        if name != "automation-evidence.html":
            sitemap_expected.append(expected_canonical)
        if parser.canonical != expected_canonical or parser.og_url != expected_canonical or not parser.description.strip():
            errors.append(f"{name}: canonical, og:url, or description mismatch")
        if parser.og_image != f"{SITE_URL}/assets/social-card.png":
            errors.append(f"{name}: og:image mismatch")
        if name == "automation-evidence.html" and "noindex" not in parser.robots.lower():
            errors.append(f"{name}: missing noindex robots meta")
        if name == "index.html":
            if not parser.json_ld_blocks:
                errors.append("index.html: missing JSON-LD script")
            else:
                for raw_json in parser.json_ld_blocks:
                    try:
                        parsed = json.loads(raw_json)
                        if parsed.get("@type") != "Person":
                            errors.append("index.html: JSON-LD @type mismatch")
                    except json.JSONDecodeError as exc:
                        errors.append(f"index.html: invalid JSON-LD ({exc})")
        if parser.title_text in seen_titles or not parser.title_text.strip():
            errors.append(f"{name}: duplicate or empty title")
        seen_titles.add(parser.title_text)
        for bad_id in WITHHELD_DRIVE_IDS:
            if bad_id in text:
                errors.append(f"{name}: withheld Drive ID leaked ({bad_id})")
        if re.search(r"[A-Za-z]:\\(?:Users|_Rehan|Documents)", text):
            errors.append(f"{name}: local machine path")
        for url in parser.hrefs + parser.assets:
            parts = urlsplit(url)
            if url.startswith("//"):
                errors.append(f"{name}: protocol-relative external url {url}")
                continue
            if parts.scheme:
                scheme = parts.scheme.lower()
                if scheme not in ALLOWED_EXTERNAL_SCHEMES:
                    errors.append(f"{name}: disallowed URI scheme {url}")
                elif scheme == "https" and not parts.netloc:
                    errors.append(f"{name}: malformed https URL {url}")
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
    option_types = {unescape(opt) for opt in re.findall(r"<option>([^<]+)</option>", type_select)}
    if option_types != {c["kind"] for c in CREDENTIALS}:
        errors.append("credentials: type filter does not match credential records")
    subject_select = credential_text.split('<select id="credentialSubject"', 1)[-1].split('</select>', 1)[0]
    option_subjects = {unescape(opt) for opt in re.findall(r"<option>([^<]+)</option>", subject_select)}
    if option_subjects != {c["subject"] for c in CREDENTIALS}:
        errors.append("credentials: subject filter does not match all 36 credential subjects")

    sitemap = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
    sitemap_locs = re.findall(r"<loc>([^<]+)</loc>", sitemap)
    if sitemap_locs != sitemap_expected:
        errors.append("sitemap: URLs do not match canonical indexable routes")
    if "automation-evidence.html" in sitemap:
        errors.append("sitemap: compatibility redirect must not be indexed")

    robots_txt = (ROOT / "robots.txt").read_text(encoding="utf-8")
    if f"Sitemap: {SITE_URL}/sitemap.xml" not in robots_txt or "Allow: /" not in robots_txt:
        errors.append("robots.txt: missing Allow or Sitemap directive")

    # Scan public source, docs, scripts, and SVGs for leaked local machine paths or withheld Drive IDs
    for scan_file in [ROOT / "README.md", ROOT / "build_site.py", ROOT / "check_site.py", ROOT / "site.js", ROOT / "theme-init.js"]:
        content = scan_file.read_text(encoding="utf-8")
        if re.search(r"[A-Za-z]:\\(?:Users|_Rehan|Documents)", content):
            errors.append(f"{scan_file.name}: local machine path leaked")
    for doc_file in sorted((ROOT / "docs").glob("*.md")):
        content = doc_file.read_text(encoding="utf-8")
        if re.search(r"[A-Za-z]:\\(?:Users|_Rehan|Documents)", content):
            errors.append(f"docs/{doc_file.name}: local machine path leaked")
    build_text = (ROOT / "build_site.py").read_text(encoding="utf-8")
    for bad_id in WITHHELD_DRIVE_IDS:
        if bad_id in build_text:
            errors.append(f"build_site.py: withheld Drive ID leaked ({bad_id})")

    if errors:
        raise SystemExit("\n".join(errors))
    print(f"Checked {len(PAGES)} pages: routes, assets, anchors, CSS tokens, SEO, privacy and one H1 each")


if __name__ == "__main__":
    main()
