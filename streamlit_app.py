import streamlit as st
import pandas as pd
import plotly.express as px
from io import BytesIO

st.set_page_config(page_title="Graviti BI Dashboard", layout="wide")

# ✅ Show logo image at the top
st.image("Logo.png", width=150)

st.title("Graviti Business Intelligence Dashboard")
uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx"])

if uploaded_file is not None:
    xls = pd.ExcelFile(uploaded_file)
    sheet_names = xls.sheet_names

    selected_sheet = st.selectbox("Select a sheet", sheet_names)
    df = xls.parse(selected_sheet)
    st.subheader("Preview of Data")
    edited_df = st.data_editor(df, use_container_width=True, num_rows="dynamic")

    st.markdown("---")
    numeric_cols = edited_df.select_dtypes(include='number').columns.tolist()

    if numeric_cols:
        st.subheader("Visualize Numeric Data")
        y_axis = st.selectbox("Choose column to visualize", numeric_cols)
        fig = px.line(edited_df, y=y_axis, title=f"{y_axis} Over Index")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No numeric columns available for visualization.")

    with st.expander("Download Your Edited Data"):
        output = BytesIO()
        try:
            with pd.ExcelWriter(output, engine='openpyxl') as writer:
                edited_df.to_excel(writer, index=False)
            output.seek(0)
            st.download_button(
                label="Download as Excel",
                data=output,
                file_name="edited_data.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
        except Exception as e:
            st.error(f"Failed to generate Excel file: {e}")
