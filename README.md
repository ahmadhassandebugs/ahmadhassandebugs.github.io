# Ahmad Hassan — static portfolio

A lightweight personal website built with Python 3’s standard library. No Ruby, Node, theme, or third-party build dependencies.

## Build and preview

```sh
python3 scripts/build.py
python3 -m http.server 8000 --directory dist
```

Open http://localhost:8000. The generated `dist/` folder is the deployable site.

## Content

- Introduction: `scripts/build.py` (homepage section).
- News: `_news/*.md`; May 2026 TikTok announcement is included by the builder.
- Blog: add dated Markdown files to `_posts/` with title and description front matter; the builder supports paragraphs, headings, links, bold text, lists, and existing HTML.
- Selected publications: entries marked `selected={true}` in `_bibliography/papers.bib`.
- CV: `assets/pdf/ahmad_hassan_cv.pdf`.
- Styling: `style.css`.

The previous al-folio sources remain as an archive, but are not used by this build. The deployment workflow builds `dist/` and publishes to the existing `gh-pages` branch on pushes to `main` or `master`. Pull requests build without deploying. Existing GitHub Pages branch settings are retained.
