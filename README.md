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
