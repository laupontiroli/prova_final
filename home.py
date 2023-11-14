import streamlit as st
import requests 

st.title("Informações do País")

pais = st.text_input("escreva o nome de um país")

button =st.button("buscar")

if button:
    try:
        response = requests.get(f'https://restcountries.com/v3.1/name/{pais}')
        response.raise_for_status()
        message = response.json()
        st.write(message)
    except Exception as e : 
        st.warning(e)
    
    with st.expander("Resultado"):
        col1,col2 = st.columns([1,3])

        with col1:
            st.write(f'Nome Oficial: {message[0]["name"]["official"]}')
            paises_fronteira=[]
            for fronteira in message[0]["borders"]:
                paises_fronteira.append(fronteira)
            st.write(f'Países que Fazem Fronteira: {paises_fronteira}')
            st.write(f'latitude: {message[0]["latlng"][0]}')
            st.write(f'longitude: {message[0]["latlng"][1]}')

        with col2:
            st.image(message[0]['coatOfArms']['png'],width=400)

    st.image(message[0]['flags']['png'],use_column_width=True)

    