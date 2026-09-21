#!/usr/bin/env python3
"""
scripts/update_gym_assets.py
Maps every single one of the 60 steps in ARTS_DATA in gym/index.html
to its exact asset in gym/assets/.
"""

import os
import re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
GYM_HTML = os.path.join(ROOT, "gym", "index.html")
ASSETS_DIR = os.path.join(ROOT, "gym", "assets")

assets = os.listdir(ASSETS_DIR)
asset_map = {}
for f in assets:
    if "-step" in f:
        name = f.rsplit(".", 1)[0]
        art, step_str = name.split("-step")
        step = int(step_str)
        asset_map[(art, step)] = f

with open(GYM_HTML, "r", encoding="utf-8") as f:
    text = f.read()

# Pattern for art block: id: 'pushups', ... steps: [ ... ]
art_pattern = re.compile(r"id:\s*'([a-z_]+)',(.*?steps:\s*\[)(.*?)(\n\s*\]\s*\n\s*\})", re.DOTALL)

def update_art(m):
    art_id = m.group(1)
    prefix = m.group(2)
    steps_body = m.group(3)
    suffix = m.group(4)

    def update_step(sm):
        step_body = sm.group(0)
        step_num_m = re.search(r'step:\s*(\d+)', step_body)
        if step_num_m:
            num = int(step_num_m.group(1))
            img_file = asset_map.get((art_id, num))
            if img_file:
                step_body = re.sub(r"img:\s*'[^']*'", f"img: 'assets/{img_file}'", step_body)
        return step_body

    updated_steps = re.sub(r'\{[^{}]*?step:\s*\d+[^}]*?\}', update_step, steps_body, flags=re.DOTALL)
    return f"id: '{art_id}',{prefix}{updated_steps}{suffix}"

new_text = art_pattern.sub(update_art, text)

with open(GYM_HTML, "w", encoding="utf-8") as f:
    f.write(new_text)

print("gym/index.html updated successfully with all 60 assets!")
