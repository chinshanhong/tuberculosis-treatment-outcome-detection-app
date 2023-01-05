import streamlit as st

st.set_page_config(
    page_title='TB Outcomes Oracle',
    layout='wide',
    page_icon="🔮"
)


st.title("TB Outcomes Oracle User Manual :book:")

st.markdown(
    """
    #### What is TB Outcomes Oracle?
    TB Outcomes Oracle is a prototype used for detecting the treatment outcomes of tuberculosis
    patients. 
    #### How to use TB Outcomes Oracle?
    Users can enter the medical data of tuberculosis patients manually in the 'Single Detection' page or upload an
    CSV file in the 'Batch Detection' page to detect the treatment outcome of their patients.
    #### What machine learning model is used in the TB Outcomes Oracle?
    Logistic regression is used to predict the treatment outcomes of the tuberculosis patients.
    #### What are the treatment outcomes that will be assigned to the tuberculosis patients when using this detector?
    The treatment outcome that will be assigned to the tuberculosis patients and its respective definitions are listed 
    below.
    | Treatment Outcome | Definition |
    | ----------------- | ----------- |
    | Cured             | Treatment completed as recommended by the national policy without evidence of failure AND three or more consecutive cultures taken at least 30 days apart are negative after the intensive phase |
    | Died             | A patient who dies for any reason during the course of treatment. |
    | Unknown             | A patient for whom no treatment outcome is assigned. (This includes cases “transferred out” to another treatment unit and whose treatment outcome is unknown). |
    
    #### Who developed TB Outcomes Oracle?
    This prototype is developed by Chin Shan Hong.
"""
)
