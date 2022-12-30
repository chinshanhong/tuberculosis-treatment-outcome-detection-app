import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.set_page_config(
    page_title='Tuberculosis Treatment Outcomes Detector',
    layout='centered'
)

st.title('Batch Detection')

csv_file = st.file_uploader("Choose a CSV file", type='csv')
if csv_file is not None:
    input_data = pd.read_csv(csv_file)
    st.write(input_data)