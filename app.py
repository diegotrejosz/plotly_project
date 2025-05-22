import pandas as pd
import plotly.express as px
import streamlit as st
     
car_data = pd.read_csv('vehicles_us.csv') # leer los datos

st.title('Creación de gráficos de regresión e histograma de la venta de autos')

# crear botón
hist_button = st.button('Construir histograma') # crear un botón
sct_button = st.button('Construir Scatter') # crear un botón

if hist_button: # al hacer clic en el botón
   # escribir un mensaje
   st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de autos en EEUU')
   # crear un histograma
   fig = px.histogram(car_data, x="odometer")
   # mostrar un gráfico Plotly interactivo
   st.plotly_chart(fig, use_container_width=True)
   
   
if sct_button:
   st.write('Creación de un gráfico de regresión entre odómetro y precio')
   fig_regression = px.scatter(car_data, x="odometer", y="price") 
   st.plotly_chart(fig_regression, use_container_width=True)