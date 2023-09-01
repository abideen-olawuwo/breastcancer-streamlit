import streamlit as st
from utils import PrepProcesor, columns
import numpy as np
import pandas as pd
import joblib


model = joblib.load('breastcancer.joblib')



st.title('Is the Cancer Malign or  Benign')



import streamlit as st

number = st.number_input('Insert a number')
st.write('The current number is ', number)








radius_mean = st.number_input('radius_mean', radius_mean)
texture_mean = st.number_input('texture_mean')
perimeter_mean = st.number_input('perimeter_mean')
area_mean = st.number_input('area_mean')
smoothness_mean = st.number_input('smoothness_mean')
compactness_mean = st.number_input('compactness_mean')
concavity_mean = st.number_input('concavity_mean')
concave points_mean = st.number_input('concave points_mean')
symmetry_mean = st.number_input('symmetry_mean')
fractal_dimension_mean = st.number_input('fractal_dimension_mean')
radius_se = st.number_input('radius_se')
texture_se = st.number_input('Insert a number')
perimeter_se = st.number_input('Insert a number')
area_se = st.number_input('Insert a number')
smoothness_se = st.number_input('Insert a number')
compactness_se = st.number_input('Insert a number')
concavity_se = st.number_input('Insert a number')
concave points_se = st.number_input('Insert a number')
symmetry_se = st.number_input('Insert a number')
fractal_dimension_se = st.number_input('Insert a number')
radius_worst = st.number_input('Insert a number')
texture_worst = st.number_input('Insert a number')
perimeter_worst = st.number_input('Insert a number')
area_worst = st.number_input('Insert a number')
smoothness_worst = st.number_input('Insert a number')
compactness_worst = st.number_input('Insert a number')
concavity_worst = st.number_input('Insert a number')
concave points_worst = st.number_input('Insert a number')
symmetry_worst = st.number_input('Insert a number')
fractal_dimension_worst = st.number_input('Insert a number')






def predict():
    row = np.array([diagnosis, radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, compactness_mean, concavity_mean, 
                    concave points_mean, symmetry_mean, fractal_dimension_mean,
                    radius_se, texture_se, perimeter_se, area_se, smoothness_se,
                    compactness_se, concavity_se, concave points_se, symmetry_se,
                    fractal_dimension_se, radius_worst, texture_worst,
                    perimeter_worst, area_worst, smoothness_worst,
                    compactness_worst, concavity_worst, concave points_worst,
                    symmetry_worst, fractal_dimension_worst])
    
    X = pd.DataFrame([row], columns=columns)
    prediction = model.predict(X)[0]

    if prediction == 1:
        st.success('The Patient Cancer is Malign')
    else:
        st.error('The Patient Cancer is Benign')




st.button('Predict', on_click=predict)





