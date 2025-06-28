import pandas as pd
import plotly.express as px
import streamlit as st
    
car_data = pd.read_csv('notebook/vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
    
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    st.write('Creación de un gráfico de dispersión entre el precio y el odómetro')
    fig_scatter = px.scatter(car_data, x="odometer", y="price", 
                             title="Relación entre kilometraje y precio",
                             labels={"odometer": "Kilometraje", "price": "Precio"},
                             opacity=0.6)
    st.plotly_chart(fig_scatter, use_container_width=True)