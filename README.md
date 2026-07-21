# LingoMux website

This repository contains the public website for the [LingoMux organization](https://github.com/lingomux).

The implementation repository is private during pre-alpha development. The website describes
the current command surface, its external requirements, and known limits without presenting the
private source as publicly available.

The site uses plain HTML and CSS. A small script handles mobile navigation and command controls. It has no runtime dependencies, analytics, or external font requests. The social card is stored with the site assets. The Studio and phone-control sections reflect the local interfaces shipped in the private implementation repository. Acquisition examples cover hash-first provider matching, checked ZIP members, and optional audio synchronization.

## Local preview

Run a local HTTP server from the repository root:

```console
python -m http.server 8000
```

Open `http://localhost:8000` in a browser.

Check the desktop and mobile layouts, command tabs, keyboard focus, copy buttons, local links, and browser console before publishing.

Run the repository checks before a push:

```console
python scripts/check_site.py
node --check assets/site.js
```

The Python check rejects missing local files, broken page anchors, duplicate element IDs, invalid `aria-controls` targets, broken encoding markers, and restricted dash characters.

## Publishing

Every push to `main` validates the files and then publishes the repository through GitHub Pages. The workflow uploads the static files and deploys them to `https://lingomux.github.io`.

## License

The website source is available under the MIT License.
