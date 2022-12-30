import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.set_page_config(
    page_title='Tuberculosis Treatment Outcomes Detector',
    layout='centered'
)

input_data = None;

st.title('Batch Detection')

def detect(input_data):
    if input_data == None:
        st.error("Please submit a CSV file before detection")
        

csv_file = st.file_uploader("Choose a CSV file", type='csv')

if csv_file is not None:
    input_data = pd.read_csv(csv_file)

if st.button('Predict'):
    detect(input_data)
    
    

