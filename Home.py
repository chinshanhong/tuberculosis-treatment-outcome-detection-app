import streamlit as st
import pandas as pd

st.set_page_config(
    page_title='TB Outcomes Oracle',
    layout='wide',
    page_icon="🔮"
)

st.title("TB Outcomes Oracle :crystal_ball:")

st.markdown(
    """
    #### Introduction
    Welcome to the main page of TB Outcomes Oracle. TB Outcomes Oracle is a prototype used for helping the medical staffs 
    to detect the treatment outcomes of tuberculosis patients. **Logistic Regression** model is used as the detector 
    in this web application. TB Outcomes Oracle consist of three major functionalities, which are **Exploratory Data Analysis**, **Single Detection** and 
    **Batch Detection**. Users can upload their dataset that contains treatment data of their TB patients and explore it in the **Exploratory Data Analysis** page. 
    Besides that, users can enter the medical data of tuberculosis patients manually in the **Single Detection** 
    page or upload a CSV file in the **Batch Detection** page to detect the treatment outcome of their patients.  
    
    #### What is Tuberculosis? 
    Tuberlosis (TB) is a deadly and infectious disease caused by the infection of *Mycobacterium tuberculosis* (Mtb). Mtb is airbone and can be spread when people inhaled 
    the Mtb spores released by persons infected with TB through coughing or speaking. Tuberculosis patients tend to experience symptoms such as weight loss, fever, night sweats,
     weakness, chest pain, and coughing blood.
     
     #### Video About Tuberculosis Facts
     """
)
col1, col2 = st.columns(2)

video_file = open("What makes tuberculosis (TB) the world's most infectious killer - Melvin Sanicas.mp4", 'rb')
video_bytes = video_file.read()

with col1: 
    st.video(video_bytes)


st.markdown("""
    
    #### What are the treatment outcomes that will be assigned to the tuberculosis patients when using this detector?
    The treatment outcome that will be assigned to the tuberculosis patients and its respective definitions are listed 
    below.
    | Treatment Outcome | Definition |
    | ----------------- | ----------- |
    | Cured             | Treatment completed as recommended by the national policy without evidence of failure AND three or more consecutive cultures taken at least 30 days apart are negative after the intensive phase |
    | Died             | A patient who dies for any reason during the course of treatment. |
    | Unknown             | A patient for whom no treatment outcome is assigned. (This includes cases “transferred out” to another treatment unit and whose treatment outcome is unknown). |
    
    #### User Manual
    To undertstnad how to use the TB Outcomes Oracle in details, please read the [TB Outcomes Oracle User Manual](https://drive.google.com/file/d/13Q-lUBe5uA9yyu1syBOolFjgnlo-OoKq/view?usp=sharing).
    
"""
)

