import streamlit as st
import pandas as pd
from scipy.stats import chi2_contingency


st.title('Turkey Political Opinions Chi-Squared Test')

st.write('The dataset used in this application consists of a ressearch that reveals he point of view of Turkish people towards political events. These are the features:')
features_data = {
    "Cinsiyet/Gender": {"Erkek": "Male", "Kadın": "Female"},
    "Egitim/Education Level": {"İlkokul": "Primary School", "OrtaOkul": "Junior High School", "Lise": "High School", "Lisans": "University", "Lisans Üstü": "MA"},
    "Soru1/Question1: Do you think our Economic Status is good?": {"Evet": "Yes", "Hayır": "No"},
    "Soru2/Question2: Need Reform in Education?": {"Evet": "Yes", "Hayır": "No"},
    "Soru3/Question3: Resolve Privatization Are You?": {"Evet": "Yes", "Hayır": "No"},
    "Soru4/Question4: Should the state use a penalty like death penalty for certain crimes?": {"Evet": "Yes", "Hayır": "No"},
    "Soru5/Question5: Do you find our journalists neutral enough?": {"Evet": "Yes", "Hayır": "No"},
    "Soru6/Question6: From 22:00 am Then Are You Supporting the Prohibition to Buy Drinks?": {"Evet": "Yes", "Hayır": "No"},
    "Soru7/Question7: Do You Want to Live in a Secular State?": {"Evet": "Yes", "Hayır": "No"},
    "Soru8/Question8: Are you supporting the abortion ban?": {"Evet": "Yes", "Hayır": "No"},
    "Soru9/Question9: Do you think that the extraordinary state (Ohal) restricts Freedoms?": {"Evet": "Yes", "Hayır": "No"},
    "Soru10/Question10: Would you like a new part of the parliament to enter?": {"Evet": "Yes", "Hayır": "No"},
}

def show_list_items(features_data):
    for key, value in features_data.items():
        if isinstance(value, dict):
            st.subheader(key)
            for k, v in value.items():
                st.write(f"- {k}: {v}")
        else:
            st.write(f"{key}: {value}")

show_list_items(features_data)

st.subheader("Chi-Squared Test")
options = ['Cinsiyet', 'Egitim', 'soru1', 'soru2', 'soru3', 'soru4', 'soru5', 'soru6', 'soru7', 'soru8', 'soru9', 'soru10']
st.write("Chose two different features to conclude if they are related to each other not. ")
v1 = st.selectbox("Chose the first feature:", options)
v2 = st.selectbox("Chose the second feature:", options)

if v1==v2:
    st.write("Choose different variables.")
else:
    if st.button('TEST'):
        file_path = 'data/data.csv'
        df = pd.read_csv(file_path)

        frequency_table = df.groupby(v1)[v2].value_counts()

        array_2d = frequency_table.unstack().fillna(0).values

        stat, p, dof, expected = chi2_contingency(array_2d)

        st.write("p-value result:")
        st.write(p)
        
        alpha = 0.05
        print("p value is " + str(p))
        if p <= alpha:
            st.write("It means that ", v1, " is **DEPENDENT** to ", v2, " and the null hypothesis is rejected.")
        else:
            st.write("It means that ", v1, " is **INDEPENDENT** to ", v2, " and the null hypothesis holds true.")