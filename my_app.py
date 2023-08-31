# Streamlit Documentation: https://docs.streamlit.io/


import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image  # to deal with images (PIL: Python imaging library)
 

# To load machine learning model
import pickle
filename = "my_model"
model=pickle.load(open(filename, "rb"))

# To take feature inputs
age=st.sidebar.selectbox("What is the age of your car:",(0,1,2,3))
hp_kW=st.sidebar.slider("What is the hp_kw of your car?",25, 1500, step=10)
km=st.sidebar.slider("What is the km of your car", 0,500000, step=1000)
Gearing_type=st.sidebar.radio('Select gear type',('Automatic','Manual','Semi-automatic'))
car_model=st.sidebar.selectbox("Select model of your car", ('Audi A1', 'Audi A3', 'Opel Astra', 'Opel Corsa', 'Opel Insignia', 'Renault Clio', 'Renault Duster', 'Renault Espace'))


# Create a dataframe using feature inputs
my_dict = {
    "age": age,
    'hp_kW': hp_kW,
    'km' : km,
    'Gearing_Type': Gearing_type,
    'make_model' :car_model,
}

df = pd.DataFrame.from_dict([my_dict])
st.table(df)

# Prediction with user inputs
predict = st.button("Predict")
result = model.predict(df)
if predict :
    st.success(result[0])