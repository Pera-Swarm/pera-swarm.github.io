# PeraSwarm

[![Scheduled Build - Daily](https://github.com/Pera-Swarm/pera-swarm.github.io/actions/workflows/daily.yml/badge.svg)](https://github.com/Pera-Swarm/pera-swarm.github.io/actions/workflows/daily.yml)
[![Scheduled Build - Weekly](https://github.com/Pera-Swarm/pera-swarm.github.io/actions/workflows/weekly.yml/badge.svg)](https://github.com/Pera-Swarm/pera-swarm.github.io/actions/workflows/weekly.yml)

This repository hosts the PeraSwarm website and provides documentation, updates, and resources about the project.

## Getting Started

Prerequisites:

- Ruby (version 2.7.0 or higher)
- Bundler gem
- Jekyll

To build and run the website locally, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/Pera-Swarm/pera-swarm.github.io
cd pera-swarm.github.io
```

1. Install the required dependencies:

```bash
make install
```

1. Start the local development server:

```bash
make serve
```

This will start a local server at `http://localhost:4000`, where you can view the website. It is already configured to watch for changes and will automatically reload the site when files are modified.

Additionally, the below commands can be used to build the site without serving it:

```bash
make build
```

## Projects

Projects are managed as Markdown pages under `projects/pages/` with `layout: page_project` and front-matter metadata. The Projects index (`projects/index.html`) builds a list from all pages with `parent: Projects` using `_includes/page_tree_builder.html` + `_includes/list_projects.html` and renders a card-style list.

Key front-matter fields:

- `title`, `description`, `permalink`, `parent: Projects`, `navbar_active: Projects`
- `nav_order` controls sort order (lower `nav_order` appears first on the index; the list is reversed in the include for implementation)
- `thumb` is the thumbnail shown on the listing
- Optional: `link_url`, `link_caption`, `api_url`, `gallery` + `gallery_images`, `resources` + `resource_list`

To add a new project, create a new file in `projects/pages/` with the fields above. The listing and detail page are generated automatically.

## News

News items are primarily managed via portal.ce.pdn.ac.lk's [News API](https://portal.ce.pdn.ac.lk/api/news/v2/pera-swarm/). To add a news item, create a new entry in the CE portal with the appropriate fields and tenant set to `Pera-Swarm`. The website fetches news from the API and generates Markdown pages under `news/pages/` using the `python_scripts/update_news.py` Python script (runs daily). The API is the source of truth; Markdown pages are regenerated from the API data, so manual edits to those pages will be overwritten.

## Publications

Publications are managed as Markdown pages under `publications/` with `layout: page_publication` and front-matter metadata. The Publications index (`publications/index.html`) uses `_includes/page_tree_builder.html` + `_includes/list_publications.html` to list pages where `parent: Publications` in reverse order.

- `paper_title`, `published_at`, `doi`
- `authors_list` (array of `{ name, profile }`)
- Optional: `pdf`, `presentation`, `source_code`
- Standard fields: `title`, `permalink`, `parent: Publications`, `navbar_active: Publications`, `nav_order`

To add a publication, create a new Markdown file in `publications/` with those fields. The list page renders the citation, DOI link, and any provided resource links.

## People

People profiles are managed by the following JSON files:

- `_data/team.json`
- `_data/supervisors.json`

Those files will be automatically updated by the Python script, `python_scripts/update.py` (runs daily), based on the API URL provided in the project page's front-matter. Team and Supervisors lists will be obtained from CE API Portal's [Projects API](https://api.ce.pdn.ac.lk/docs/projects/).

## Announcements

Site-wide announcements are rendered via the Jekyll include at `_includes/announcements.html`. Most layouts display announcements through the shared navbar include, while some minimal layouts (such as blank or home-style layouts) include `announcements.html` directly at the top of the page. Each layout should include announcements exactly once (either via the navbar or directly) to avoid duplicate alerts. The include fetches announcements from `https://portal.ce.pdn.ac.lk/api/announcements/v2/pera-swarm`, renders Bootstrap alerts, and filters by `starts_at`/`ends_at` (inclusive) plus `area` set to `both` or `frontend`.

Caching behavior:

- Cookie name: `announcements`
- Cache validity: 30 minutes based on `fetched_at`
- Cookie expiration: 30 minutes

If the cookie is missing or invalid (including JSON parse errors), the include re-fetches the API. Invalid responses or failed requests render nothing and do not break page rendering.

Security and compliance notes:

- Rate-limits: client-side cache prevents repeated fetches within 30 minutes and reduces load on the API.
- Input validation: only renders announcements with valid `type`, `message`, `starts_at`, and `ends_at` fields.
- Secret management: no secrets are stored or required by the include.
