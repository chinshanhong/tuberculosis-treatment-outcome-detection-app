import streamlit as st
import pandas as pd
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report

st.set_page_config(layout="wide", page_title='TB Outcomes Oracle', page_icon='🔮')

st.title("Exploratory Data Analysis")

st.markdown("""
    You can upload TB medical data of your TB patients here and explore it with our tools!
""")

data = None

def explore(data):
    
    if data is None:
        st.error("Please submit a CSV file before exploration")
    elif data is not None:
        empty_columns = []
        for column in data.columns:
            if data[column].isnull().values.any():
                empty_columns.append(column)
        if len(empty_columns) != 0:
            st.error(f"Your TB medical data have empty column(s) {empty_columns}. Please fill in all the columns before exploration.")
        else:
            pr = data.profile_report()
            st_profile_report(pr)

uploaded_file = st.file_uploader("Choose a CSV file", type='csv')
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

if st.button("Explore"):
    explore(data)
