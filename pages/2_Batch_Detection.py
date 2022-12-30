import streamlit as st
import pandas as pd
import numpy as np
import pickle

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


def detect(data):
    if data is None:
        st.error("Please submit a CSV file before detection")
    else:
        st.markdown("## Detection Results Preview")
        
        lr_model = pickle.load(open(
            'lr_model.pkl',
            'rb'))

        encoder = pickle.load(open('encoder.pkl', 'rb'))
        scaler = pickle.load(open('scaler.pkl', 'rb'))

        data.columns = ['treatment_status', 'hain_rifampicin', 'social_risk_factors', 'rater',
                   'pleural_effusion_percent_of_hemithorax_involved', 'regimen_drug', 'gene_name', 'hain_isoniazid',
                   'smallnodules', 'isanynoncalcifiednoduleexist']
        
        input_data = data.copy(deep=True)
        input_data = encoder.transform(input_data)
        input_data = scaler.transform(input_data)

        result = lr_model.predict(input_data)
        
        output_data = data.assign(Outcome=result)
        output_data['Outcome'] = output_data['Outcome'].map({0 : 'Cured', 1 : 'Died', 2 : 'Unknown'})
        
        st.write(output_data)
       

csv_file = st.file_uploader("Choose a CSV file", type='csv')

if csv_file is not None:
    data = pd.read_csv(csv_file)

if st.button('Predict'):
    detect(data)
