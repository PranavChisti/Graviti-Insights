
# Excel Insights Dashboard

This is a simple Streamlit app that allows users to upload Excel files and generate real-time dashboards, perform edits, and export updated files.

## Features

- Upload `.xlsx` Excel files
- Choose any sheet to view/edit
- Visualize numeric data as interactive line charts
- Download the edited data as Excel
- Cloud-ready for deployment (Streamlit Cloud)

## How to Run (Locally)

```bash
pip install streamlit pandas plotly openpyxl
streamlit run streamlit_app.py
```

## How to Deploy (Streamlit Cloud)

1. Fork this repository to your GitHub account
2. Go to https://streamlit.io/cloud
3. Sign in and click "New App"
4. Connect to this repo and click "Deploy"
