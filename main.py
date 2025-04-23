######################## IMPORT ########################
import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression
from ucimlrepo import fetch_ucirepo 

######################## SVILUPPO MODELLO ########################
#Import dei dati
real_estate_valuation = fetch_ucirepo(id=477)
X1 = real_estate_valuation.data.features[["X5 latitude", "X6 longitude"]]
X2 = real_estate_valuation.data.features[["X2 house age", "X3 distance to the nearest MRT station", "X4 number of convenience stores"]]
y = real_estate_valuation.data.targets

#Creazione dei modelli
modello1 = LinearRegression()
modello1.fit(X1, y)
modello2 = LinearRegression()
modello2.fit(X2, y)


######################## WEB APP CON STREAMLIT ########################
#Titolo pagina
st.title("Stima del prezzo al metro quadro di un'abitazione")

#Selettore modello
scelta = st.selectbox("Scegli il modello:", [
    "Modello 1 (latitudine e longitudine)",
    "Modello 2 (età dell’immobile, distanza dalla stazione MRT più vicina e numero di minimarket)"
])

if scelta == "Modello 1 (latitudine e longitudine)":

    #Input
    lat = st.number_input("Latitudine:", step = 0.00001, format="%0.5f")
    lon = st.number_input("Longitudine:", step = 0.00001, format="%0.5f")
    X_input = [[lat, lon]]

    # Validazione
    if not X1["X5 latitude"].min() <= lat <= X1["X5 latitude"].max() or not X1["X6 longitude"].min() <= lon <= X1["X6 longitude"].max():
        st.error("Latitudine e/o longitudine fuori dai limiti concessi!!!")
    else:
        #Stima
        prezzo = modello1.predict(X_input)[0]
        st.success(f"Prezzo stimato al mq: {round(float(prezzo),2)}")

else:
    #Input
    eta = st.number_input("Età dell’immobile:", step = 0.1, format = "%0.1f")
    distanza_MRT = st.number_input("Distanza dalla stazione MRT più vicina:", step = 0.00001, format="%0.5f")
    numero_MRT = st.number_input("Numero di minimarket:", step = 1, value = 0)
    X_input = [[eta, distanza_MRT, numero_MRT]]

    #Stima
    prezzo = modello2.predict(X_input)[0]
    st.success(f"Prezzo stimato al mq: {round(float(prezzo),2)}")
