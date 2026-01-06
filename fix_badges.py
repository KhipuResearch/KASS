#!/usr/bin/env python3
"""Replace shields.io badges with plain text for LaTeX compatibility."""

import json
import os
import re

notebooks = [
    "notebooks/applied-econometrics/07-labor-market-intelligence.ipynb",
    "notebooks/applied-econometrics/20-opportunity-zone-evaluation.ipynb", 
    "notebooks/applied-econometrics/22-workforce-development-roi.ipynb",
    "notebooks/causal-inference/11-heterogeneous-treatment-effects.ipynb",
    "notebooks/causal-inference/14-synthetic-control-policy-lab.ipynb",
    "notebooks/causal-inference/15-regression-discontinuity-toolkit.ipynb",
]

# Mapping of notebook to its plain text badge line
badge_replacements = {
    "07": "**KRL Suite v2.0** | **Tier: Community** | **Data: BLS + FRED**\n",
    "20": "**KRL Suite v2.0** | **Tier: Professional** | **Data: FRED County Economics**\n",
    "22": "**KRL Suite v2.0** | **Tier: Professional** | **Data: FRED Labor Market**\n",
    "11": "**KRL Suite v2.0** | **Tier: Pro + Enterprise** | **Data: FRED State Economics**\n",
    "14": "**KRL Suite v2.0** | **Tier: Community** | **Data: FRED State Economics**\n",
    "15": "**KRL Suite v2.0** | **Tier: Community** | **Data: FRED County Economics**\n",
}

for nb_path in notebooks:
    print(f"Processing {nb_path}...")
    
    # Get notebook number from filename
    nb_num = os.path.basename(nb_path).split("-")[0]
    
    with open(nb_path, 'r') as f:
        nb = json.load(f)
    
    for cell in nb['cells']:
        if cell['cell_type'] == 'markdown':
            new_source = []
            i = 0
            badge_inserted = False
            
            while i < len(cell['source']):
                line = cell['source'][i]
                
                # Skip badge lines
                if '[![KRL Suite]' in line or '[![Tier]' in line or '[![Data]' in line:
                    i += 1
                    continue
                
                # After series title, insert plain text badge before the ---
                if ('| Applied Econometrics Series' in line or '| Causal Inference Series' in line) and not badge_inserted:
                    new_source.append(line)
                    new_source.append("\n")
                    new_source.append(badge_replacements[nb_num])
                    badge_inserted = True
                    i += 1
                    continue
                
                new_source.append(line)
                i += 1
            
            cell['source'] = new_source
    
    with open(nb_path, 'w') as f:
        json.dump(nb, f, indent=1)
    
    print(f"  Updated {nb_path}")

print("\nDone! All badges replaced with plain text.")
