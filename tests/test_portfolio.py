"""Unit and structural tests for Rehan Memon's static portfolio generator."""

import subprocess
import sys
from collections import Counter
from pathlib import Path

# Ensure parent directory is in path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import build_site


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
    """Verify 48 credential records."""
    assert len(build_site.CREDENTIALS) == 48


def test_iirs_outreach_derivatives():
    """Verify 21 IIRS/ISRO public-safe derivatives exist on disk."""
    iirs_records = [c for c in build_site.CREDENTIALS if c["issuer"] == "IIRS / ISRO Outreach"]
    assert len(iirs_records) == 21
    assert len(build_site.IIRS_PUBLIC_KEYS) == 21
    for key in build_site.IIRS_PUBLIC_KEYS:
        expected = ROOT / f"assets/documents/iirs-outreach/iirs-{key}-participation.pdf"
        assert expected.is_file(), f"Missing IIRS public PDF: {expected}"


def test_html_escaping_and_helpers():
    """Verify that helper functions escape dangerous HTML inputs."""
    malicious = '<script>alert("xss")</script>'
    escaped = build_site.link("https://example.com", malicious)
    assert "&lt;script&gt;" in escaped
    assert "<script>" not in escaped

    badge_html = build_site.badge(malicious)
    assert "&lt;script&gt;" in badge_html
    assert "<script>" not in badge_html


def test_check_site_structural_integrity():
    """Verify that the full structural check suite passes with 0 errors."""
    result = subprocess.run(
        [sys.executable, str(ROOT / "check_site.py")],
        cwd=str(ROOT),
        capture_output=True,
        text=True,
        check=False
    )
    assert result.returncode == 0, f"check_site.py failed:\n{result.stderr}\n{result.stdout}"
    assert "Checked 17 pages" in result.stdout


def test_clipboard_copy_implementation_and_fallback():
    """Regression test: verify clipboard implementation, dual-tier fallback, and honest error handling."""
    site_js_path = ROOT / "site.js"
    assert site_js_path.is_file()
    js_content = site_js_path.read_text(encoding="utf-8")

    # 1. Must define dual-tier helper with secureContext check
    assert "copyTextToClipboard" in js_content
    assert "window.isSecureContext" in js_content

    # 2. Must contain legacy execCommand fallback
    assert "document.execCommand('copy')" in js_content

    # 3. Must NOT falsely report success on catch
    assert "Copy failed ✗" in js_content

    # 4. Must update accessibility aria-label
    assert "Email address copied to clipboard" in js_content
    assert "Failed to copy email address" in js_content

    # 5. Verify CSS defines failure state
    site_css_path = ROOT / "site.css"
    css_content = site_css_path.read_text(encoding="utf-8")
    assert ".copy-email-btn.copy-failed" in css_content

    # 6. Verify JavaScript syntax via node --check
    node_res = subprocess.run(
        ["node", "--check", str(site_js_path)],
        capture_output=True,
        text=True,
        check=False
    )
    assert node_res.returncode == 0, f"node --check site.js failed:\n{node_res.stderr}"
