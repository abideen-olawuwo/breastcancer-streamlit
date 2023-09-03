import streamlit as st
from utils import PrepProcesor, columns
import preprocessor

import numpy as np
import pandas as pd
import joblib

model = joblib.load('breastcancer.joblib')


st.title('Is the Cancer Malign or  Benign')

radius_mean = st.number_input('Insert the Radius Mean')
st.write('The Radius Mean  is ', radius_mean)

texture_mean = st.number_input('Insert the texture_mean ')
st.write('The texture mean is ', texture_mean)

perimeter_mean = st.number_input('Insert the perimeter_mean')
st.write('The perimeter mean is ', perimeter_mean)

area_mean = st.number_input('Insert the area_mean')
st.write('The area mean is ', area_mean)

smoothness_mean = st.number_input('Insert the smoothness_mean')
st.write('The smoothness mean is ', smoothness_mean)

compactness_mean = st.number_input('Insert the compactness_mean')
st.write('The compactness mean is ', compactness_mean)

concavity_mean = st.number_input('Insert the concavity_mean')
st.write('The concavity mean is ', concavity_mean)

concave_points_mean = st.number_input('Insert the concave_points_mean')
st.write('The concave points mean is ', concave_points_mean)

symmetry_mean = st.number_input('Insert the symmetry_mean')
st.write('The symmetry mean is ', symmetry_mean)

fractal_dimension_mean = st.number_input('Insert the fractal_dimension_mean')
st.write('The fractal dimension mean is ', fractal_dimension_mean)

radius_se = st.number_input('Insert the radius_se')
st.write('The radius se is ', radius_se)

texture_se = st.number_input('Insert the texture_se')
st.write('The texture se is ', texture_se)

perimeter_se = st.number_input('Insert the perimeter_se')
st.write('The perimeter se is ', perimeter_se)

area_se = st.number_input('Insert the area_se')
st.write('The area se is ', area_se)

smoothness_se = st.number_input('Insert the smoothness_se')
st.write('The smoothness se is ', smoothness_se)

compactness_se = st.number_input('Insert the compactness_se')
st.write('The compactness se is ', compactness_se)

concavity_se = st.number_input('Insert the concavity_se')
st.write('The concavity se is ', concavity_se)

concave_points_se = st.number_input('Insert the concave_points_se')
st.write('The concave points se is ', concave_points_se)

symmetry_se = st.number_input('Insert the symmetry_se')
st.write('The symmetry se is ', symmetry_se)

fractal_dimension_se = st.number_input('Insert the fractal_dimension_se')
st.write('The fractal_dimension_se is ', fractal_dimension_se)

radius_worst = st.number_input('Insert the radius_worst')
st.write('The radius worst is ', radius_worst)

texture_worst = st.number_input('Insert the texture_worst')
st.write('The texture worst is ', texture_worst)

perimeter_worst = st.number_input('Insert the perimeter_worst')
st.write('The perimeter worst is ', perimeter_worst)

area_worst = st.number_input('Insert the area_worst')
st.write('The area worst is ', area_worst)

smoothness_worst = st.number_input('Insert the smoothness_worst')
st.write('The smoothness worst is ', smoothness_worst)

compactness_worst = st.number_input('Insert the compactness_worst')
st.write('The compactness worst is ', compactness_worst)

concavity_worst = st.number_input('Insert the concavity_worst')
st.write('The concavity worst is ', concavity_worst)

concave_points_worst = st.number_input('Insert the concave_points_worst')
st.write('The concave points worst is ', concave_points_worst)

symmetry_worst = st.number_input('Insert the symmetry_worst')
st.write('The symmetry_worst is ', symmetry_worst)

fractal_dimension_worst = st.number_input('Insert fractal dimension worst')
st.write('The fractal dimension worst is ', fractal_dimension_worst)





def predict():
    row = np.array([radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean,
                    compactness_mean, concavity_mean, concave_points_mean, symmetry_mean,
                    fractal_dimension_mean, radius_se, texture_se, perimeter_se, area_se,
                    smoothness_se, compactness_se, concavity_se, concave_points_se,
                    symmetry_se, fractal_dimension_se, radius_worst, texture_worst,
                    perimeter_worst, area_worst, smoothness_worst,
                    compactness_worst, concavity_worst, concave_points_worst,
                    symmetry_worst, fractal_dimension_worst])
    
    X = pd.DataFrame([row], columns=columns)
    prediction = model.predict(X)[0]

    if prediction == 1:
        st.success('The Patient Cancer is Malign')
    else:
        st.error('The Patient Cancer is Benign')

st.button('Predict', on_click = predict)





