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

## News

## Publications

## Announcements

Site-wide announcements are rendered via the Jekyll include at `_includes/announcements.html`, which is included at the top of all layouts. The include fetches announcements from `https://portal.ce.pdn.ac.lk/api/announcements/v2/pera-swarm`, renders Bootstrap alerts, and filters by `starts_at`/`ends_at` (inclusive) plus `area` set to `both` or `frontend`.

Caching behavior:

- Cookie name: `announcements`
- Cache validity: 30 minutes based on `fetched_at`
- Cookie expiration: 30 minutes

If the cookie is missing or invalid (including JSON parse errors), the include re-fetches the API. Invalid responses or failed requests render nothing and do not break page rendering.

Security and compliance notes:

- Rate-limits: client-side cache prevents repeated fetches within 30 minutes and reduces load on the API.
- Input validation: only renders announcements with valid `type`, `message`, `starts_at`, and `ends_at` fields.
- Secret management: no secrets are stored or required by the include.
