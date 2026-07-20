# LingoMux website

This repository contains the public website for [LingoMux](https://github.com/lingomux/lingomux).

The site is plain HTML and CSS. It has no runtime dependencies, analytics, or external font requests.

## Local preview

Run a local HTTP server from the repository root:

```console
python -m http.server 8000
```

Open `http://localhost:8000` in a browser.

## Publishing

Every push to `main` publishes the repository through GitHub Pages. The workflow uploads the static files and deploys them to `https://lingomux.github.io`.

## License

The website source is available under the MIT License.
