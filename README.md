# LingoMux website

This repository contains the public website for [LingoMux](https://github.com/lingomux/lingomux).

The site uses plain HTML, CSS, and a small script for command tabs and copy buttons. It has no runtime dependencies, analytics, or external font requests. The social card is stored with the site assets.

## Local preview

Run a local HTTP server from the repository root:

```console
python -m http.server 8000
```

Open `http://localhost:8000` in a browser.

Check the desktop and mobile layouts, command tabs, keyboard focus, copy buttons, local links, and browser console before publishing.

## Publishing

Every push to `main` publishes the repository through GitHub Pages. The workflow uploads the static files and deploys them to `https://lingomux.github.io`.

## License

The website source is available under the MIT License.
