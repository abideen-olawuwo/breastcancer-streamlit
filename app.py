import pandas as pd
import numpy as np
import pickle
import streamlit as st
from PIL import Image

# loading in the model to predict on the data
pickle_in = open('classifier.pkl', 'rb')
classifier = pickle.load(pickle_in)


def welcome():
    return 'welcome all'

# defining the function which will make the prediction using
# the data which the user inputs


def prediction(radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean,
               compactness_mean, concavity_mean, concave_points_mean, symmetry_mean,
               fractal_dimension_mean, radius_se, texture_se, perimeter_se, area_se,
               smoothness_se, compactness_se, concavity_se, concave_points_se,
               symmetry_se, fractal_dimension_se, radius_worst, texture_worst,
               perimeter_worst, area_worst, smoothness_worst,
               compactness_worst, concavity_worst, concave_points_worst,
               symmetry_worst, fractal_dimension_worst):

    prediction = classifier.predict(
        [[radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean,
          compactness_mean, concavity_mean, concave_points_mean, symmetry_mean,
          fractal_dimension_mean, radius_se, texture_se, perimeter_se, area_se,
          smoothness_se, compactness_se, concavity_se, concave_points_se,
          symmetry_se, fractal_dimension_se, radius_worst, texture_worst,
          perimeter_worst, area_worst, smoothness_worst,
          compactness_worst, concavity_worst, concave_points_worst,
          symmetry_worst, fractal_dimension_worst]])
    return prediction


# this is the main function in which we define our webpage
def main():
    # giving the webpage a title
    st.title("Breast Cancer Prediction")
    st.title('Is the Cancer Malign or Benign')

    # the following lines create text boxes in which the user can enter
    # the data required to make the prediction
    radius_mean = st.number_input('Insert the Radius Mean')
    texture_mean = st.number_input('Insert the texture_mean ')
    perimeter_mean = st.number_input('Insert the perimeter_mean')
    area_mean = st.number_input('Insert the area_mean')
    smoothness_mean = st.number_input('Insert the smoothness_mean')
    compactness_mean = st.number_input('Insert the compactness_mean')
    concavity_mean = st.number_input('Insert the concavity_mean')
    concave_points_mean = st.number_input('Insert the concave_points_mean')
    symmetry_mean = st.number_input('Insert the symmetry_mean')
    fractal_dimension_mean = st.number_input(
        'Insert the fractal_dimension_mean')
    radius_se = st.number_input('Insert the radius_se')
    texture_se = st.number_input('Insert the texture_se')
    perimeter_se = st.number_input('Insert the perimeter_se')
    area_se = st.number_input('Insert the area_se')
    smoothness_se = st.number_input('Insert the smoothness_se')
    compactness_se = st.number_input('Insert the compactness_se')
    concavity_se = st.number_input('Insert the concavity_se')
    concave_points_se = st.number_input('Insert the concave_points_se')
    symmetry_se = st.number_input('Insert the symmetry_se')
    fractal_dimension_se = st.number_input('Insert the fractal_dimension_se')
    radius_worst = st.number_input('Insert the radius_worst')
    texture_worst = st.number_input('Insert the texture_worst')
    perimeter_worst = st.number_input('Insert the perimeter_worst')
    area_worst = st.number_input('Insert the area_worst')
    smoothness_worst = st.number_input('Insert the smoothness_worst')
    compactness_worst = st.number_input('Insert the compactness_worst')
    concavity_worst = st.number_input('Insert the concavity_worst')
    concave_points_worst = st.number_input('Insert the concave_points_worst')
    symmetry_worst = st.number_input('Insert the symmetry_worst')
    fractal_dimension_worst = st.number_input('Insert fractal dimension worst')
    result = ""

    # the below line ensures that when the button called 'Predict' is clicked,
    # the prediction function defined above is called to make the prediction
    # and store it in the variable result
    if st.button("Predict"):
        result = prediction(radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean,
                            compactness_mean, concavity_mean, concave_points_mean, symmetry_mean,
                            fractal_dimension_mean, radius_se, texture_se, perimeter_se, area_se,
                            smoothness_se, compactness_se, concavity_se, concave_points_se,
                            symmetry_se, fractal_dimension_se, radius_worst, texture_worst,
                            perimeter_worst, area_worst, smoothness_worst,
                            compactness_worst, concavity_worst, concave_points_worst,
                            symmetry_worst, fractal_dimension_worst)

        # Check the prediction result and display a message
        if result[0] == 1:
            st.success('Cancer is Malign :thumbsup:')
        else:
            st.error('Cancer is Benign :thumbsdown:')


if __name__ == '__main__':
    main()
