import streamlit as st
import pandas as pd
import pickle

# Load model
model = pickle.load(open('model_mobil.sav', 'rb'))

st.set_page_config(page_title='Prediksi Harga Mobil')

st.title('Prediksi Harga Mobil')
st.write('Masukkan spesifikasi mobil untuk memprediksi harga.')

# Input user
engine_size = st.number_input('Engine Size', value=2.0)
horsepower = st.number_input('Horsepower', value=150)
wheelbase = st.number_input('Wheelbase', value=100)
width = st.number_input('Width', value=70)
length = st.number_input('Length', value=180)
fuel_efficiency = st.number_input('Fuel Efficiency', value=25)

# Prediksi
if st.button('Prediksi Harga'):

    data = pd.DataFrame({
        'Engine_size': [engine_size],
        'Horsepower': [horsepower],
        'Wheelbase': [wheelbase],
        'Width': [width],
        'Length': [length],
        'Fuel_efficiency': [fuel_efficiency]
    })

    prediction = model.predict(data)

    st.success(f'Perkiraan Harga Mobil: ${prediction[0]:.2f} ribu')