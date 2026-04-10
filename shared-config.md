---
name: "Library/ajschuit/shared-config"
tags: meta/library
last_updated: 2026-04-10 17:30:03.588203
files:
 - shared-config/scripts/config.md
 - shared-config/scripts/forprefix.md
 - shared-config/scripts/gps.md
 - shared-config/scripts/journal.md
 - shared-config/scripts/snippets.md
 - shared-config/scripts/utilities.md
 - shared-config/scripts/widgets.md
 - shared-config/styles/custom-admonitions.md
 - shared-config/styles/imports.md
 - shared-config/styles/main.md
 - shared-config/templates/page/daily-journal.md
---
This is all of the config values, templates and scripts for silverbullet that I want to share between my work space and personal space. This way, my "setup" can be the same between the two.

# Styles

${query[[from o = index.tag "page" where o.name:startsWith(_CTX.currentPage.name.."styles")]]}

# Scripts

${query[[from o = index.tag "page" where o.name:startsWith(_CTX.currentPage.name.."scripts")]]}

# Templates

${query[[from o = index.tag "page" where o.name:startsWith(_CTX.currentPage.name.."templates")]]}

