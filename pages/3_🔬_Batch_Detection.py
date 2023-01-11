import streamlit as st
import pandas as pd
import numpy as np
import pickle
import plotly.graph_objects as go

st.set_page_config(
    page_title='TB Outcomes Oracle',
    layout='centered',
    page_icon='🔮'
)

data = None;

st.title('Batch Detection')

st.markdown(
    """
    #### Important Note
    Before uploading your CSV file, please make sure that your CSV files have the following column headers and in the correct order. You can download the CSV template below
    to key in your TB patients' data.
    The list of accepted values for each column are listed in this [document](https://drive.google.com/file/d/1chvgeHxyZ5kwfyZL9UFcclYUyTHIUe-A/view?usp=sharing)
    1. Treatment Status
    2. Hain Rifampicin
    3. Social Risk Factors
    4. Rater
    5. Pleural Effusion Percent of Hemithorax Involved
    6. Drug Regimen
    7. Gene Name
    8. Hain Isoniazid
    9. Small Nodules
    10. Calcified Nodules
    """
)

def convert_df(df):
    return df.to_csv(index=False)


template = pd.DataFrame(columns=['Treatment Status', 'Hain Rifampicin', 'Social Risk Factors', 'Rater', 
                                 'Pleural Effusion Percent of Hemithorax Involved', 'Drug Regimen', 'Gene Name', 'Hain Isoniazid', 
                                 'Small Nodules', 'Calcified Nodules'])
template = convert_df(template)

st.download_button(
            label='Download template CSV',
            data=template,
            file_name='Template.csv',
            mime='text/csv'
        )

def detect(data):
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
            st.markdown("## Detection Results Preview")

            lr_model = pickle.load(open(
                'lr_model.pkl',
                'rb'))

            encoder = pickle.load(open('encoder.pkl', 'rb'))
            scaler = pickle.load(open('scaler.pkl', 'rb'))

            data.columns = ['treatment_status', 'hain_rifampicin', 'social_risk_factors', 'rater',
                            'pleural_effusion_percent_of_hemithorax_involved', 'regimen_drug', 'gene_name',
                            'hain_isoniazid',
                            'smallnodules', 'isanynoncalcifiednoduleexist']

            data['hain_rifampicin'] = data['hain_rifampicin'].map({'Resistant': 'R', 'Sensitive': 'S', 'Not Reported': 'Not Reported'})
            data['hain_isoniazid'] = data['hain_isoniazid'].map({'Resistant': 'R', 'Sensitive': 'S', 'Intermediate': 'I', 'Not Reported': 'Not Reported'})

            input_data = data.copy(deep=True)
            input_data = encoder.transform(input_data)
            input_data = scaler.transform(input_data)

            result = lr_model.predict(input_data)

            output_data = data.assign(Outcome=result)
            output_data['Outcome'] = output_data['Outcome'].map({0: 'Cured', 1: 'Died', 2: 'Unknown'})

            st.write(output_data)

            csv = convert_df(output_data)

            treatment_outcome_count = output_data['Outcome'].value_counts()

            colors = ['mediumturquoise', 'darkorange', 'lightgreen']

            fig = go.Figure(data=[go.Pie(labels=['Cured', 'Died', 'Unknown'],
                                         values=[treatment_outcome_count['Cured'], treatment_outcome_count['Died'],
                                                 treatment_outcome_count['Unknown']], hole=.3,
                                         textinfo='label+percent')])

            fig.update_traces(marker=dict(colors=colors))

            st.plotly_chart(fig, theme='streamlit')

            st.download_button(
                label='Download result as CSV',
                data=csv,
                file_name='Detection Result.csv',
                mime='text/csv'
            )

csv_file = st.file_uploader("Choose a CSV file", type='csv')

if csv_file is not None:
    data = pd.read_csv(csv_file)

if st.button('Detect'):
    detect(data)
