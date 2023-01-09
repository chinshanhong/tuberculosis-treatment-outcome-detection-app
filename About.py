import streamlit as st
import pandas as pd

st.set_page_config(
    page_title='TB Outcomes Oracle',
    layout='wide',
    page_icon="🔮"
)

st.title("Tuberculosis Treament Outcomes Oracle :crystal_ball:")

st.markdown(
    """
    #### Introduction
    Welcome to the main page of TB Outcomes Oracle. TB Outcomes Oracle is a prototype used for helping the medical staffs 
    to detect the treatment outcomes of tuberculosis patients. **Logistic Regression** model is used as the detector 
    in this web application. TB Outcomes Oracle consist of two major functionalities, which are **Single Detection** and 
    **Batch Detection**. Users can enter the medical data of tuberculosis patients manually in the **Single Detection** 
    page or upload a CSV file in the **Batch Detection** page to detect the treatment outcome of their patients.  
    
    #### What is Tuberculosis? 
    
    
    5. Download results as CSV.
    
    
    #### Q&A
    ##### What are the treatment outcomes that will be assigned to the tuberculosis patients when using this detector?
    The treatment outcome that will be assigned to the tuberculosis patients and its respective definitions are listed 
    below.
    | Treatment Outcome | Definition |
    | ----------------- | ----------- |
    | Cured             | Treatment completed as recommended by the national policy without evidence of failure AND three or more consecutive cultures taken at least 30 days apart are negative after the intensive phase |
    | Died             | A patient who dies for any reason during the course of treatment. |
    | Unknown             | A patient for whom no treatment outcome is assigned. (This includes cases “transferred out” to another treatment unit and whose treatment outcome is unknown). |
    
"""
)

