---
name: "Library/ajschuit/shared-config"
tags: meta/library
files:
- scripts/config.md
- scripts/forprefix.md
- scripts/gps.md
- scripts/journal.md
- scripts/snippets.md
- scripts/utilities.md
- scripts/widgets.md
- styles/custom-admonitions.md
- styles/imports.md
- styles/main.md
- templates/page/daily-journal.md
---

This is all of the config values, templates and scripts for silverbullet that I want to share between my work space and personal space. This way, my "setup" can be the same between the two.

# Templates

${query[[from o = index.tag "page" where o.name:startsWith(_CTX.currentPage.name:gsub("shared--config","templates"))]]}

# Scripts

${query[[from o = index.tag "page" where o.name:startsWith(_CTX.currentPage.name:gsub("shared--config","scripts"))]]}

# Styles

${query[[from o = index.tag "page" where o.name:startsWith(_CTX.currentPage.name:gsub("shared--config","styles"))]]}

