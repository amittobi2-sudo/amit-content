# Amit Tobi website source

Build: `python3 site-src/build2.py site https://amit-tobi.onrender.com` (keep site/robots.txt, site/img/og.png and the IndexNow key .txt; copy them back after a clean build).
Facts: only use `site-src/facts.md`. No phone numbers, no invented results.
New articles: append dicts to ARTICLES_B in `articles_b.py` (keys: slug, title, desc, kw, body).
Deploy: push to main, then trigger a deploy of Render service srv-db72ejk9v7es73a8k9jg.
