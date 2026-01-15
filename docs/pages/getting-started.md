---
layout: page
title: Getting Started
permalink: /getting-started/
---

## Technical Requirements

- **Python 3.9+**
- **Jupyter** or **JupyterLab**
- Key packages: `pandas`, `numpy`, `scipy`, `statsmodels`, `econml`, `causalml`, `matplotlib`, `seaborn`
- Data access (varies by notebook): Census API key, BLS API key, or administrative data access

See individual notebooks for specific environment requirements.

---

## Installation

```bash
# Clone the repository
git clone https://github.com/KhipuResearch/KASS.git
cd KASS

# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

## How to Use This

### If you're learning causal inference

Start with the method that matches your data structure. Each notebook includes detailed methodology sections explaining not just *how* to implement the estimator, but *why* the approach works and when it's appropriate.

**Recommended path:**

1. Start with Regression Discontinuity for clean identification
2. Move to Synthetic Control for comparative case studies
3. Explore Heterogeneous Treatment Effects for targeting analysis

### If you're conducting policy analysis

Fork the repository, adapt the relevant notebook to your data and question, modify the specifications as needed. The code is structured to make this straightforward.

### If you're evaluating the KRL platform

These notebooks demonstrate core analytical capabilities. The platform adds data connectivity, automated pipelines, collaboration features, and production-grade infrastructure around these methods.

[Learn more about KRL →](https://krlabs.dev)
