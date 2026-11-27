"""Unit, determinism, escaping, and structural tests for Rehan Memon's static portfolio generator."""

import json
import re
import shutil
import subprocess
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import build_site
import check_site


def test_pages_definition():
    """Verify exactly 17 defined routes."""
    assert len(build_site.PAGES) == 17
    assert "index.html" in build_site.PAGES
    assert "projects.html" in build_site.PAGES
    assert "credentials.html" in build_site.PAGES
    assert "automation.html" in build_site.PAGES


def test_projects_allocation():
    """Verify 14 projects across three core pillars in 5/5/4 allocation."""
    assert len(build_site.PROJECTS) == 14
    counts = Counter(p["pillar"] for p in build_site.PROJECTS)
    assert counts["AI & Machine Learning Systems"] == 5
    assert counts["Client & Collaborative Engineering"] == 5
    assert counts["AI & Workflow Automation"] == 4


def test_credentials_count():
    """Verify 48 credential records and all 36 subjects populated."""
    assert len(build_site.CREDENTIALS) == 48
    subjects = {c["subject"] for c in build_site.CREDENTIALS}
    assert len(subjects) == 36


def test_iirs_outreach_derivatives():
    """Verify 21 IIRS/ISRO public-safe derivatives exist on disk."""
    iirs_records = [c for c in build_site.CREDENTIALS if c["issuer"] == "IIRS / ISRO Outreach"]
    assert len(iirs_records) == 21
    assert len(build_site.IIRS_PUBLIC_KEYS) == 21
    for key in build_site.IIRS_PUBLIC_KEYS:
        expected = ROOT / f"assets/documents/iirs-outreach/iirs-{key}-participation.pdf"
        assert expected.is_file(), f"Missing IIRS public PDF: {expected}"


def test_html_escaping_schemes_and_json_ld():
    """Verify helpers escape dangerous HTML inputs, reject unsafe URI schemes, and emit valid JSON-LD."""
    malicious = '<script>alert("xss")</script>'
    escaped = build_site.link("https://example.com", malicious, css='cls" onclick="x()')
    assert "&lt;script&gt;" in escaped
    assert "<script>" not in escaped
    assert "&quot;" in escaped

    badge_html = build_site.badge(malicious)
    assert "&lt;script&gt;" in badge_html
    assert "<script>" not in badge_html

    sec_html = build_site.section("Title", "<p>ok</p>", sid='a" onclick="bad()')
    assert "&quot;" in sec_html

    for bad_href in ("javascript:alert(1)", "data:text/html,<script>", "vbscript:msgbox(1)"):
        try:
            build_site.link(bad_href, "Click")
            raise AssertionError(f"Expected ValueError for unsafe scheme: {bad_href}")
        except ValueError:
            pass

    parsed_ld = json.loads(build_site._SCHEMA_JSON)
    assert parsed_ld["@type"] == "Person"
    assert parsed_ld["affiliation"]["@type"] == "CollegeOrUniversity"


def test_generated_outputs_determinism():
    """Verify all generated HTML files, sitemap.xml, and robots.txt match build_site.py output byte-for-byte."""
    for filename, item in build_site.PAGES.items():
        rendered = build_site.render(filename, item)
        on_disk = (ROOT / filename).read_text(encoding="utf-8")
        assert rendered == on_disk, f"Stale generated HTML file on disk: {filename}"

    expected_sitemap_locs = [
        f"{build_site.SITE_URL}/" if fn == "index.html" else f"{build_site.SITE_URL}/{fn}"
        for fn in build_site.PAGES
        if fn != "automation-evidence.html"
    ]
    disk_sitemap = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
    assert re.findall(r"<loc>([^<]+)</loc>", disk_sitemap) == expected_sitemap_locs
    disk_robots = (ROOT / "robots.txt").read_text(encoding="utf-8")
    assert f"Sitemap: {build_site.SITE_URL}/sitemap.xml" in disk_robots


def test_css_variables_defined():
    """Verify every CSS custom property used in site.css and HTML is defined in site.css."""
    css_text = (ROOT / "site.css").read_text(encoding="utf-8")
    defined = set(re.findall(r"(--[a-z0-9-]+)\s*:", css_text))
    for var_name in re.findall(r"var\((--[a-z0-9-]+)(?:\s*,|\))", css_text):
        assert var_name in defined, f"Undefined CSS variable in site.css: {var_name}"
    for filename in build_site.PAGES:
        html_text = (ROOT / filename).read_text(encoding="utf-8")
        for var_name in re.findall(r"var\((--[a-z0-9-]+)", html_text):
            assert var_name in defined, f"Undefined CSS variable in {filename}: {var_name}"


def test_check_site_structural_integrity():
    """Verify that the full structural check suite passes with 0 errors."""
    result = subprocess.run(
        [sys.executable, str(ROOT / "check_site.py")],
        cwd=str(ROOT),
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, f"check_site.py failed:\n{result.stderr}\n{result.stdout}"
    assert "Checked 17 pages" in result.stdout
    assert check_site.EXPECTED_PILLARS["AI & Workflow Automation"] == 4


def test_clipboard_copy_accessibility_and_syntax():
    """Regression test: verify accessible clipboard copy live status, fallback focus restoration, timer safety, and JS syntax."""
    site_js_path = ROOT / "site.js"
    theme_js_path = ROOT / "theme-init.js"
    assert site_js_path.is_file() and theme_js_path.is_file()
    js_content = site_js_path.read_text(encoding="utf-8")

    assert "copyTextToClipboard" in js_content
    assert "window.isSecureContext" in js_content
    assert "document.execCommand('copy')" in js_content
    assert "prevFocus" in js_content
    assert "clearTimeout(resetTimerId)" in js_content
    assert "copy-email-status" in js_content
    assert "Copy failed ✗" in js_content
    assert "Copy failed: unable to copy email address to clipboard" in js_content

    css_content = (ROOT / "site.css").read_text(encoding="utf-8")
    assert ".copy-email-btn.copy-failed" in css_content
    assert "#b42318" in css_content

    contact_html = (ROOT / "contact.html").read_text(encoding="utf-8")
    assert 'class="sr-only copy-email-status"' in contact_html
    assert 'role="status"' in contact_html

    node_bin = shutil.which("node")
    assert node_bin is not None, "node binary must be available on PATH"
    for script_path in (site_js_path, theme_js_path):
        node_res = subprocess.run(
            [node_bin, "--check", str(script_path)],
            capture_output=True,
            text=True,
            check=False,
        )
        assert node_res.returncode == 0, f"node --check {script_path.name} failed:\n{node_res.stderr}"
