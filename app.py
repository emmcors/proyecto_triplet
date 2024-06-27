import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')

st.header('Anuncios de Venta de Autos')




build_histogram = st.checkbox('Construir un histograma')# crear una casilla de verificación
build_disp = st.checkbox('Construir un gráfico de dispersión')# crear una casilla de verificación

start_button = st.button('Crear')

if start_button and build_histogram:
    st.write('Numeros de Autos por Kilometraje')
    fig1 = px.histogram(car_data, x="odometer") # crear un histograma
    st.plotly_chart(fig1, use_container_width=True)
elif start_button and build_disp:
    st.write('Precios de los Autos en Relación con los Kilometros Recorridos')
    fig2 = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión
    st.plotly_chart(fig2, use_container_width=True)