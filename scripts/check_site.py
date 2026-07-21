from __future__ import annotations

from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parent.parent
HTML_FILES = (ROOT / "index.html", ROOT / "404.html")
TEXT_FILES = (*HTML_FILES, ROOT / "assets" / "styles.css", ROOT / "assets" / "site.js")
BROKEN_TEXT_MARKERS = ("Â", "Ã", "â", "Ø", "Ù", "Ú", "Û", "\ufffd")


class SiteParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: list[str] = []
        self.references: list[tuple[str, str]] = []
        self.controls: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if identifier := values.get("id"):
            self.ids.append(identifier)
        if controls := values.get("aria-controls"):
            self.controls.extend(controls.split())
        for name in ("href", "src"):
            if reference := values.get(name):
                self.references.append((name, reference))


def main() -> None:
    for path in TEXT_FILES:
        check_text(path)
    for path in HTML_FILES:
        check_html(path)
    for path in (ROOT / "assets").iterdir():
        if path.is_file() and path.stat().st_size == 0:
            raise RuntimeError(f"Empty site asset: {path.relative_to(ROOT)}")
    print("Site check passed")


def check_text(path: Path) -> None:
    content = path.read_text(encoding="utf-8")
    markers = [marker for marker in BROKEN_TEXT_MARKERS if marker in content]
    if markers:
        shown = ", ".join(repr(marker) for marker in markers)
        raise RuntimeError(f"Broken text marker in {path.relative_to(ROOT)}: {shown}")
    if "\u2014" in content or "\u2013" in content:
        raise RuntimeError(f"Restricted dash character in {path.relative_to(ROOT)}")


def check_html(path: Path) -> None:
    content = path.read_text(encoding="utf-8")
    parser = SiteParser()
    parser.feed(content)
    duplicate_ids = sorted(name for name, count in Counter(parser.ids).items() if count > 1)
    if duplicate_ids:
        raise RuntimeError(f"Duplicate IDs in {path.name}: {', '.join(duplicate_ids)}")
    available_ids = set(parser.ids)
    for controls in parser.controls:
        if controls not in available_ids:
            raise RuntimeError(f"Missing aria-controls target in {path.name}: {controls}")
    for attribute, reference in parser.references:
        check_reference(path, available_ids, attribute, reference)


def check_reference(
    source: Path,
    available_ids: set[str],
    attribute: str,
    reference: str,
) -> None:
    parsed = urlsplit(reference)
    if parsed.scheme or parsed.netloc:
        return
    if not parsed.path and parsed.fragment:
        if parsed.fragment not in available_ids:
            raise RuntimeError(f"Missing anchor in {source.name}: #{parsed.fragment}")
        return
    target = ROOT / "index.html" if parsed.path == "/" else ROOT / parsed.path.lstrip("/")
    if not target.is_file():
        raise RuntimeError(f"Missing {attribute} target in {source.name}: {reference}")


if __name__ == "__main__":
    main()
