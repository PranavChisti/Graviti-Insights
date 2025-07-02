
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
st.title("Excel-Based Company Insights Dashboard")

uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx"])
if uploaded_file:
    xls = pd.ExcelFile(uploaded_file)
    sheet_names = xls.sheet_names
    selected_sheet = st.selectbox("Select a sheet", sheet_names)
    df = pd.read_excel(xls, sheet_name=selected_sheet)

    st.subheader("Data Preview & Edit")
    edited_df = st.data_editor(df, num_rows="dynamic")

    st.subheader("Summary Statistics")
    st.write(edited_df.describe())

    st.subheader("Visualize Numeric Data")
    numeric_cols = edited_df.select_dtypes(include=['float64', 'int64']).columns
    if len(numeric_cols) >= 2:
        x_col = st.selectbox("X-axis", numeric_cols)
        y_col = st.selectbox("Y-axis", numeric_cols, index=1)
        fig = px.line(edited_df, x=x_col, y=y_col, markers=True)
        st.plotly_chart(fig, use_container_width=True)

    with st.expander("Download Your Edited Data"):
        excel_bytes = edited_df.to_excel(index=False, engine='openpyxl')
        st.download_button("Download as Excel", excel_bytes, file_name="edited_data.xlsx")
else:
    st.info("Please upload an Excel (.xlsx) file to use the dashboard.")
