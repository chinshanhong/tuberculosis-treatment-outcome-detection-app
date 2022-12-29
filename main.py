import streamlit as st
import pandas as pd
import numpy as np
import pickle

# from sklearn.preprocessing import StandardScaler
# from sklearn.linear_model import LogisticRegression
# from category_encoders import CountEncoder

st.set_page_config(layout="centered", page_title='Tuberculosis Treatment Outcomes Detector')

if 'result' not in st.session_state:
    st.session_state.result = 100

if 'treatment_outcome' not in st.session_state:
    st.session_state.treatment_outcome = ''

st.title("Tuberculosis Treatment Outcomes Detector")

col1, col2 = st.columns(2, gap='small')

with st.form('Single Prediction', clear_on_submit=True):
    with col1:
        # First widget to get the input of rater occupation
        rater_occupation = st.selectbox(
            'Please select your occupation',
            ['Radiologist', 'General practitioner', 'Other', 'Not Reported']
        )

        # Second widget to get the treatment status of TB patient
        treatment_status = st.selectbox("Please select your patient's treatment status",
                                        ['Treatment ended', 'Continuation of Treatment',
                                         'Treatment ineffective due to additional resistance',
                                         'Patient stopped treatment', 'Terminated from study',
                                         'New drugs available', 'Drug(s) no longer available',
                                         'Adverse event', 'Not Reported'])

        # Third widget to select the risk factors that the TB patient currently having
        risk_factors = st.multiselect('Please select all the risk factors that your patient exhibit',
                                      ['Current smoker', 'Documented MDR contact', 'Patient alcohol abuse',
                                       'Ex prisoner', 'TB care worker', 'Homeless', 'Worked abroad',
                                       'Patient drug abuse', 'Immigrants', 'Refugees', 'Internal migrants',
                                       'Not Reported'],
                                      ['Not Reported'])

        # Fourth widget to select the pleural effusion percent of hemithorax involved
        pleural_effusion_percent = st.selectbox('Please select the pleural effusion percent of hemithorax',
                                                ['Less than 50', '0',
                                                 'Greater than or equal to 50',
                                                 'Not Reported'])

        # Fifth widget to select the drug regimen that the patient is taking
        drug_regimen = st.multiselect('Please select the drug regimen that your patient is taking',
                                      ['Bedaquiline', 'Clofazimine', 'Cycloserine', 'Levofloxacin',
                                       'Linezolid', 'Capreomycin', 'p-aminosalicylic acid',
                                       'Prothionamide', 'Ethambutol', 'Kanamycin', 'Pyrazinamide',
                                       'Rifampicin', 'Amoxicillin-clavulanate', 'Delamanid',
                                       'Imipenem-cilastatin', 'Isoniazid', 'Streptomycin',
                                       'Moxifloxacin', 'Pretomanid', 'Aminoglycosides - injectible agents',
                                       'Ofloxacin', 'Amikacin', 'Ethionamide', 'Terizidone',
                                       'Antiretroviral therapy', 'Cotrimoxazol preventive', 'Clarithromycin',
                                       'Fluoroquinolones', 'Not Reported'], ['Not Reported'])

    with col2:
        # Sixth widget to select the location of small nodules that the patient is taking
        small_nodules = st.multiselect('Does small nodules exist?',
                                       ['Lower Left Sextant-Yes', 'Lower Left Sextant-No', 'Lower Right Sextant-Yes',
                                        'Middle Left Sextant-Yes', 'Middle Right Sextant-Yes', 'Upper Left Sextant-Yes',
                                        'Upper Right Sextant-Yes', 'Middle Left Sextant-No', 'Middle Right Sextant-No',
                                        'Upper Left Sextant-No', 'Upper Right Sextant-No', 'Lower Right Sextant-No',
                                        'None', 'Not Reported'],
                                       ['Not Reported'])

        # Seventh widget to select the location of small nodules that the patient is taking
        calcified_nodules = st.multiselect('Does calcified nodules exist?',
                                           ['Lower Left Sextant-Yes', 'Lower Left Sextant-No',
                                            'Lower Right Sextant-Yes',
                                            'Middle Left Sextant-Yes', 'Middle Right Sextant-Yes',
                                            'Upper Left Sextant-Yes',
                                            'Upper Right Sextant-Yes', 'Middle Left Sextant-No',
                                            'Middle Right Sextant-No',
                                            'Upper Left Sextant-No', 'Upper Right Sextant-No', 'Lower Right Sextant-No',
                                            'None', 'Not Reported'],
                                           ['Not Reported'])

        # Eight widget to select the gene name
        gene_name = st.multiselect('Please select your patient genomic sequence',
                                   ['katG', 'rpoB', 'rpsL', 'embB', 'inhA-Pro',
                                    'gyrA', 'rrs', 'pncA', 'inhA', 'Not Reported'],
                                   ['Not Reported'])

        # Ninth widget to select the result of drug sensitivity test
        hain_rifampicin = st.selectbox('Please select the drug sensitivity test result of rifampicin',
                                       ['Resistant', 'Sensitive', 'Not Reported'])

        # Tenth widget to select the result of drug sensitivity test
        hain_isoniazid = st.selectbox('Please select the drug sensitivity test result of isoniazid',
                                      ['Resistant', 'Sensitive', 'Intermediate', 'Not Reported'])

    submitted = st.form_submit_button("Predict")

    # Add input data into numpy array
    if submitted:
        social_risk_factor_list = ', '.join(risk_factors)

        regimen_drug_list = ', '.join(drug_regimen)

        gene_name_list = ', '.join(gene_name)

        small_nodules_list = ', '.join(small_nodules)

        calcified_nodules_list = ', '.join(calcified_nodules)

        input_data = {
            'treatment_status': [treatment_status],
            'hain_rifampicin': [hain_rifampicin],
            'social_risk_factors': [social_risk_factor_list],
            'rater': [rater_occupation],
            'pleural_effusion_percent_of_hemithorax_involved': [pleural_effusion_percent],
            'regimen_drug': [regimen_drug_list],
            'gene_name': [gene_name_list],
            'hain_isoniazid': [hain_isoniazid],
            'smallnodules': [small_nodules_list],
            'isanynoncalcifiednoduleexist': [calcified_nodules_list]
        }

        df = pd.DataFrame(input_data)

        lr_model = pickle.load(open(
            'lr_model.pkl',
            'rb'))

        encoder = pickle.load(open('encoder.pkl', 'rb'))
        scaler = pickle.load(open('scaler.pkl', 'rb'))

        df = encoder.transform(df)
        df = scaler.transform(df)

        result = lr_model.predict(df)

        if result == 0:
            st.session_state.result = 0
            st.session_state.treatment_outcome = 'Cured'

        elif result == 1:
            st.session_state.result = 1
            st.session_state.treatment_outcome = 'Died'

        elif result == 2:
            st.session_state.result = 2
            st.session_state.treatment_outcome = 'Unknown'

st.subheader("Detection Result")
image_path = ''
col3, col4 = st.columns(2)

with col3:
    if st.session_state.result == 0:
        image_path = 'cured.png'
        st.image(image_path, width=200)
    elif st.session_state.result == 1:
        image_path = 'died.png'
        st.image(image_path, width=200)
    elif st.session_state.result == 2:
        image_path = 'unknown.png'
        st.image(image_path, width=200)

with col4:
    if st.session_state.result == 0:
        st.header(f':green[{st.session_state.treatment_outcome}]')
    elif st.session_state.result == 1:
        st.header(f':red[{st.session_state.treatment_outcome}]')
    elif st.session_state.result == 2:
        st.header(f'{st.session_state.treatment_outcome}')
