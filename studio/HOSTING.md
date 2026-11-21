# Website ownership and publishing

The canonical studio website is https://simplemindsstudios.com/.
Its source and publishing home is https://github.com/Simple-Minds-Studios/simplemindsstudios.github.io.

The personal Bartron773/simplemindsstudios.github.io repository retains the earlier studio history as a rollback reference. Its live additions were merged into the organization repository, preserving both histories.

The separate Simple-Minds-Studios/public-website.github.io repository contains the Atlas Museum prototype; it is not the canonical studio homepage and is preserved independently.

## Publishing

Pushes to main deploy through `.github/workflows/pages.yml`. The build copies tracked files only, excludes CNAME from the Actions artifact, and uses the configured Pages base path. Manage the custom domain through GitHub Pages settings. Preview builds support the repository path; custom-domain builds use `/`.

Preserve the existing Google Analytics property G-8QL1DX6CTL to retain measurement continuity. Individual projects retain their existing Pages addresses until their own hosting is intentionally changed. The project index is curated; private organization repositories are not automatically published.

## Recovery

Before changing domain ownership, verify the organization preview and preserve both repository histories. If the new site fails, detach the custom domain from the organization repository and reattach it to Bartron773/simplemindsstudios.github.io with its main/root legacy Pages source. Retain the personal source files for this purpose.
