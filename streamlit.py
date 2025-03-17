#!/usr/bin/env python
# coding: utf-8

# ## 9. User Interface Development with Streamlit 

# ### Import Necessory Libraries

# In[ ]:


import streamlit as st
import requests


# In[ ]:


# FastAPI endpoint URL
FASTAPI_URL = "http://127.0.0.1:8000/predict"

# Dropdown options based on Pandera schema
WORKCLASS_OPTIONS = ["Self-emp-not-inc", "Private", "State-gov", "Federal-gov", "Local-gov", "Self-emp-inc", "Without-pay", "Never-worked", "None"]
EDUCATION_OPTIONS = ["Bachelors", "HS-grad", "11th", "Masters", "9th", "Some-college", "Assoc-acdm", "Assoc-voc", "7th-8th", "Doctorate", "Prof-school", "5th-6th", "10th", "1st-4th", "Preschool", "12th", "None"]
MARITAL_STATUS_OPTIONS = ["Married-civ-spouse", "Divorced", "Married-spouse-absent", "Never-married", "Separated", "Married-AF-spouse", "Widowed", "None"]
OCCUPATION_OPTIONS = ["Exec-managerial", "Handlers-cleaners", "Prof-specialty", "Other-service", "Adm-clerical", "Sales", "Craft-repair", "Transport-moving", "Farming-fishing", "Machine-op-inspct", "Tech-support", "Protective-serv", "Armed-Forces", "Priv-house-serv", "None"]
RELATIONSHIP_OPTIONS = ["Husband", "Not-in-family", "Wife", "Own-child", "Unmarried", "Other-relative", "None"]
RACE_OPTIONS = ["White", "Black", "Asian-Pac-Islander", "Amer-Indian-Eskimo", "Other", "None"]
SEX_OPTIONS = ["Male", "Female", "None"]
NATIVE_COUNTRY_OPTIONS = ["United-States", "Cuba", "Jamaica", "India", "Mexico", "South", "Puerto-Rico", "Honduras", "England", "Canada", "Germany", "Iran", "Philippines", "Italy", "Poland", "Columbia", "Cambodia", "Thailand", "Ecuador", "Laos", "Taiwan", "Haiti", "Portugal", "Dominican-Republic", "El-Salvador", "France", "Guatemala", "China", "Japan", "Yugoslavia", "Peru", "Outlying-US(Guam-USVI-etc)", "Scotland", "Trinadad&Tobago", "Greece", "Nicaragua", "Vietnam", "Hong", "Ireland", "Hungary", "Holand-Netherlands", "None"]

def main():
    st.title("Income Prediction App")
    st.write("Enter the details below to predict income category.")

    # User input fields
    age = st.number_input("Age", min_value=17, step=1)
    workclass = st.selectbox("Workclass", WORKCLASS_OPTIONS)
    fnlwgt = st.number_input("Final Weight", min_value=1, step=1)
    education = st.selectbox("Education", EDUCATION_OPTIONS)
    education_num = st.slider("Education Number", min_value=1, max_value=16, step=1)
    marital_status = st.selectbox("Marital Status", MARITAL_STATUS_OPTIONS)
    occupation = st.selectbox("Occupation", OCCUPATION_OPTIONS)
    relationship = st.selectbox("Relationship", RELATIONSHIP_OPTIONS)
    race = st.selectbox("Race", RACE_OPTIONS)
    sex = st.selectbox("Sex", SEX_OPTIONS)
    capital_gain = st.number_input("Capital Gain", min_value=0, step=1)
    capital_loss = st.number_input("Capital Loss", min_value=0, step=1)
    hours_per_week = st.slider("Hours per Week", min_value=1, max_value=99, step=1)
    native_country = st.selectbox("Native Country", NATIVE_COUNTRY_OPTIONS)

    if st.button("Predict Income"):
        # Prepare data payload
        input_data = {
            "age": age,
            "workclass": workclass,
            "fnlwgt": fnlwgt,
            "education": education,
            "education_num": education_num,
            "marital_status": marital_status,
            "occupation": occupation,
            "relationship": relationship,
            "race": race,
            "sex": sex,
            "capital_gain": capital_gain,
            "capital_loss": capital_loss,
            "hours_per_week": hours_per_week,
            "native_country": native_country
        }

        # Send request to FastAPI
        try:
            response = requests.post(FASTAPI_URL, json=input_data)
            result = response.json()
            if "predicted_income" in result:
                st.success(f"Predicted Income: {result['predicted_income']}")
            else:
                st.error(f"Error: {result.get('error', 'Unknown error')}")
        except Exception as e:
            st.error(f"Failed to connect to FastAPI: {str(e)}")

if __name__ == "__main__":
    main()    


# In[ ]:


# !streamlit run streamlit.py

