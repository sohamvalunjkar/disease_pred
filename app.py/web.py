import os
import pickle  # pre-trained model loading
import streamlit as st  # web app
from streamlit_option_menu import option_menu

st.set_page_config(page_title=' Prediction of Disease Outbreaks',
                   layout='wide',
                   page_icon="🧑‍⚕")

# Load pre-trained models
diabetes_model = pickle.load(open(r"D:\machine learning\ml projects\disease predication model\models\db_dataset.sav", 'rb'))
heart_disease_model = pickle.load(open(r"D:\machine learning\ml projects\disease predication model\models\ht_dataset.sav", 'rb'))
parkinsons_model = pickle.load(open(r"D:\machine learning\ml projects\disease predication model\models\pk_dataset.sav", 'rb'))

with st.sidebar:
    selected = option_menu('Prediction of disease outbreak system',
                           ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons prediction'],
                           menu_icon='hospital-fill', icons=['activity', 'heart', 'person'], default_index=0)

if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose level')
    with col3:
        Bloodpressure = st.text_input('Blood Pressure value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin = st.text_input('Insulin level')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age = st.text_input('Age of the person')

    diab_diagnosis = ''
    if st.button('Diabetes Test Result'):
        user_input = [Pregnancies, Glucose, Bloodpressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]
        user_input = [float(x) for x in user_input]
        diab_prediction = diabetes_model.predict([user_input])
        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'
    st.success(diab_diagnosis)

elif selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.text_input('Age')
    with col2:
        sex = st.selectbox('Sex', [0, 1])  # 0: Female, 1: Male
    with col3:
        cp = st.selectbox('Chest Pain Type', [0, 1, 2, 3])  # 0-3: Different types of chest pain
    with col1:
        trestbps = st.text_input('Resting Blood Pressure (in mm Hg)')
    with col2:
        chol = st.text_input('Serum Cholesterol (in mg/dl)')
    with col3:
        fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', [0, 1])  # 0: No, 1: Yes
    with col1:
        restecg = st.selectbox('Resting Electrocardiographic Results', [0, 1, 2])  # 0-2: Different results
    with col2:
        thalach = st.text_input('Maximum Heart Rate Achieved')
    with col3:
        exang = st.selectbox('Exercise Induced Angina', [0, 1])  # 0: No, 1: Yes
    with col1:
        oldpeak = st.text_input('Oldpeak (depression induced by exercise relative to rest)')
    with col2:
        slope = st.selectbox('Slope of the Peak Exercise ST Segment', [0, 1, 2])  # 0-2: Different slopes
    with col3:
        ca = st.selectbox('Number of Major Vessels (0-3) Colored by Fluoroscopy', [0, 1, 2, 3])
    with col1:
        thal = st.selectbox('Thalassemia', [0, 1, 2, 3])  # 0-3: Different thalassemia types

    heart_diagnosis = ''
    if st.button('Heart Disease Test Result'):
        heart_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        heart_input = [float(x) for x in heart_input]
        heart_prediction = heart_disease_model.predict([heart_input])
        if heart_prediction[0 ] == 1:
            heart_diagnosis = 'The person has heart disease'
        else:
            heart_diagnosis = 'The person does not have heart disease'
    st.success(heart_diagnosis)

elif selected == 'Parkinsons prediction':
    st.title('Parkinsons Disease Prediction using ML')
    col1, col2, col3 = st.columns(3)
    with col1:
        MDVP_Fo = st.text_input('MDVP:Fo(Hz)')
    with col2:
        MDVP_Fhi = st.text_input('MDVP:Fhi(Hz)')
    with col3:
        MDVP_Flo = st.text_input('MDVP:Flo(Hz)')
    with col1:
        MDVP_Jitter = st.text_input('MDVP:Jitter(%)')
    with col2:
        MDVP_Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
    with col3:
        MDVP_RAP = st.text_input('MDVP:RAP')
    with col1:
        MDVP_PPQ = st.text_input('MDVP:PPQ')
    with col2:
        Jitter_DDP = st.text_input('Jitter:DDP')
    with col3:
        MDVP_Shimmer = st.text_input('MDVP:Shimmer')
    with col1:
        MDVP_Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
    with col2:
        Shimmer_APQ3 = st.text_input('Shimmer:APQ3')
    with col3:
        Shimmer_APQ5 = st.text_input('Shimmer:APQ5')
    with col1:
        MDVP_APQ = st.text_input('MDVP:APQ')
    with col2:
        Shimmer_DDA = st.text_input('Shimmer:DDA')
    with col3:
        NHR = st.text_input('NHR')
    with col1:
        HNR = st.text_input('HNR')
    with col2:
        status = st.text_input('Status')
    with col3:
        RPDE = st.text_input('RPDE')
    with col1:
        DFA = st.text_input('DFA')
    with col2:
        spread1 = st.text_input('spread1')
    with col3:
        spread2 = st.text_input('spread2')
    with col1:
        D2 = st.text_input('D2')

    parkinsons_diagnosis = ''
    if st.button('Parkinsons Test Result'):
        parkinsons_input = [MDVP_Fo, MDVP_Fhi, MDVP_Flo, MDVP_Jitter, MDVP_Jitter_Abs,
                            MDVP_RAP, MDVP_PPQ, Jitter_DDP, MDVP_Shimmer, MDVP_Shimmer_dB,
                            Shimmer_APQ3, Shimmer_APQ5, MDVP_APQ, Shimmer_DDA, NHR, HNR,
                            status, RPDE, DFA, spread1, spread2, D2]
        parkinsons_input = [float(x) for x in parkinsons_input]
        parkinsons_prediction = parkinsons_model.predict([parkinsons_input])
        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = 'The person has Parkinsons disease'
        else:
            parkinsons_diagnosis = 'The person does not have Parkinsons disease'
    st.success(parkinsons_diagnosis)
