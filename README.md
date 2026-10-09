# 🌸 IrisLab — Bloom & Explore

> An interactive, flower-themed Exploratory Data Analysis dashboard for the classic Iris dataset.

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Data-Pandas-150458?logo=pandas)
![Flask](https://img.shields.io/badge/API-Flask-000000?logo=flask)
![Status](https://img.shields.io/badge/Project-Portfolio%20EDA-DF7AA8)

---

## 🌷 Overview

**IrisLab** bridges the gap between static Jupyter notebooks and interactive web dashboards. It lets you explore flower measurements, distributions, outliers, and species correlations through a clean, browser-based UI backed by a lightweight Python Flask server.

---

## 🚀 Features

* **Dataset Overview**: View high-level metrics, sample records, and feature distributions[cite: 1].
* **Interactive Visualizations**: Inspect scatter plots, histograms, box plots, a correlation heatmap, and pairplots[cite: 1].
* **Data-Driven Conclusions**: Automatically summarize dataset findings and feature separations[cite: 1].
* **Decoupled Architecture**: Notebook calculations export to a CSV bridge, which the Flask backend serves to the frontend via a JSON API[cite: 1].

---

## 🛠️ Technology Stack

* **Analysis**: Python, Pandas, NumPy, Jupyter Notebook[cite: 1]
* **Visualization**: Matplotlib, Seaborn, Plotly[cite: 1]
* **Backend**: Flask (`iris_dashboard_server.py`)[cite: 1]
* **Frontend**: HTML, CSS, JavaScript (`irislab_frontend_connected.html`)[cite: 1]

---

## 💻 Quick Start Guide

### 1. Clone the Repository
```powershell
git clone [https://github.com/YOUR-USERNAME/irislab-bloom-explore.git](https://github.com/YOUR-USERNAME/irislab-bloom-explore.git)
cd irislab-bloom-explore
