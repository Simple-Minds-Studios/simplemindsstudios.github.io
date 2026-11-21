# Simple Minds Studios

**A studio for intelligent systems — clarity for human systems.**

This repository powers the public website and project hub for **Simple Minds Studios**, the independent creative and systems practice of Bart Salazar in Hart, Michigan.

Live website: **https://simplemindsstudios.com/**. Publishing and recovery details: [Hosting](studio/HOSTING.md).

## What the studio explores

Simple Minds Studios brings together:

- human–AI cognitive partnership and research
- creative systems and narrative design
- AI-assisted prototyping and human-centered interfaces
- civic and policy concepts
- fashion, visual identity, music, and editorial projects
- speculative architecture and future systems
- research-oriented tools and public experiments

The website is the curated exhibition. GitHub is the working archive containing source files, documentation, versions, licensing, and development history.

## Public reading guide

For people and AI assistants, start with [llms.txt](llms.txt) and the [public content guide](studio/PUBLIC_CONTENT.md). These link directly to readable project descriptions, sources, credits, and prototype status. Requested AI reading, summary, and citation are permitted under the [AI policy](repository-standard/AI_POLICY.md); model training and bulk reuse remain restricted.

## Studio documents

- [The Ethos of Simple Minds Studios](studio/ETHOS.md) — founding document and living reference
- [Manifesto](studio/MANIFESTO.md)
- [Project Index](studio/PROJECTS.md)
- [Repository standards and rights information](repository-standard/)

## Website

[Visit Simple Minds Studios](https://simplemindsstudios.com)

## Status

Active studio website and evolving portfolio archive. New exhibits, research, films, images, and experimental projects will be added as they are prepared.

## Rights and use

This is a **source-visible, all-rights-reserved** repository. Public access permits viewing and evaluation; it does not grant permission to copy, adapt, redistribute, commercialize, train AI systems on, or create derivative works from the studio’s code, writing, visual systems, or project materials.

See [`repository-standard/LICENSE`](repository-standard/LICENSE), [`repository-standard/COPYRIGHT.md`](repository-standard/COPYRIGHT.md), [`repository-standard/AI_POLICY.md`](repository-standard/AI_POLICY.md), and [`repository-standard/ATTRIBUTION.md`](repository-standard/ATTRIBUTION.md).

---

**Created by Bart Salazar / Simple Minds Studios**  
Hart, Michigan — 2026


## Public collection coverage

The homepage and searchable directory use `projects/catalog.json` as the reviewed public inventory. Both family-history exhibits are featured in the visual homepage collection. The **All projects** header link remains visible on phones.

Before deployment, `scripts/check_public_catalog.py --live` compares the catalog with GitHub’s public organization repositories. Missing or stale entries stop the deployment with an explicit report; private source is never imported automatically. The build synchronizes the homepage directory panel and static project directory from the catalog.

## Visual homepage

The November 21 visual edition uses `assets/homepage/homepage.css` and `assets/homepage/homepage.js`, real project imagery, six featured projects plus Hart, in Motion, and the integrated podcast. All public repositories remain in the searchable All projects panel and the static project directory. The primary contact is [bart@simplemindsstudios.com](mailto:bart@simplemindsstudios.com). Existing deep pages remain available.
