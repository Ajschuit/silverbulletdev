import os
from datetime import datetime 

BASE_DIR = "shared-config"
OUTPUT_FILE = "shared-config.md"

# folders you care about
SECTIONS = sorted([d for d in os.listdir(BASE_DIR) if os.path.isdir(os.path.join(BASE_DIR, d)) and not d.startswith(".")])
def collect_files():
    files = []
    for section in SECTIONS:
        section_path = os.path.join(BASE_DIR, section)
        for root, _, filenames in os.walk(section_path):
            for f in filenames:
                if f.endswith(".md"):
                    rel_path = os.path.join(root, f)
                    files.append(rel_path.replace("\\", "/"))
    return sorted(files)

def build_sections():
    blocks = []
    for section in SECTIONS:
        title = section.capitalize()

        query = f"""${{template.each(
    query[[from o = index.tag "page" where o.name:startsWith(_CTX.currentPage.name.."/{section}")]],
    template.new [==[# ${{displayName or ref}} [[${{ref}}|ℹ]==])}}"""

        blocks.append(f"# {title}\n\n{query}\n")

    return "\n".join(blocks)

def generate():
    files = collect_files()
    sections = build_sections()

    file_list = "\n".join([f" - {f}" for f in files])

    content = f"""---
name: "Library/ajschuit/shared-config"
tags: meta/library
last_updated: {datetime.now()}
files:
{file_list}
---
This is all of the config values, templates and scripts for silverbullet that I want to share between my work space and personal space. This way, my "setup" can be the same between the two.

{sections}
"""

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    generate()
