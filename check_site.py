"""Dependency-free structural checks for generated static pages."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

from build_site import PAGES, ROOT


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.hrefs = []
        self.assets = []
        self.h1_count = 0
        self.title_count = 0

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if values.get("id"):
            self.ids.add(values["id"])
        if tag == "a" and values.get("href"):
            self.hrefs.append(values["href"])
        if tag in {"script", "link", "img"}:
            path = values.get("src") or values.get("href")
            if path and not urlsplit(path).scheme:
                self.assets.append(path)
        if tag == "h1":
            self.h1_count += 1
        if tag == "title":
            self.title_count += 1


def main():
    errors = []
    for name in PAGES:
        page = ROOT / name
        parser = PageParser()
        parser.feed(page.read_text(encoding="utf-8"))
        if parser.h1_count != 1 or parser.title_count != 1 or "main" not in parser.ids:
            errors.append(f"{name}: heading/title/main structure")
        for url in parser.hrefs + parser.assets:
            parts = urlsplit(url)
            if parts.scheme or url.startswith("//"):
                continue
            target = page.parent / parts.path if parts.path else page
            if not target.is_file():
                errors.append(f"{name}: missing {url}")
            if parts.fragment:
                target_parser = PageParser()
                if target.is_file():
                    target_parser.feed(target.read_text(encoding="utf-8"))
                    if parts.fragment not in target_parser.ids:
                        errors.append(f"{name}: missing #{parts.fragment} in {target.name}")
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"Checked {len(PAGES)} pages: routes, assets, anchors and one H1 each")


if __name__ == "__main__":
    main()
