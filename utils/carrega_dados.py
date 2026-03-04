import pandas as pd
import requests
import json
import streamlit as st

url = "https://api.nasa.gov/neo/rest/v1/feed"
api_key = "VS8knobJ4CUll5fGNAeSK5W14ubHiXx1a6sjsRiK"

@st.cache_data
def puxa_dados_api_nasa(start_date='2024-12-01',end_date='2024-12-07'):

    params = {'start_date':start_date, 'end_date':end_date, 'api_key': api_key }

    resposta = requests.get(params=params, url=url)

    if resposta.status_code == 200:
        data = (resposta.json())
        with open ('dados/asteroide.json', 'w') as f:
            json.dump(data,f)
        dados_asteroide = []
        for dia in data['near_earth_objects']:
            for asteroide in data['near_earth_objects'][dia]:
                dia = dia
                name = asteroide['name']
                diameter = asteroide['estimated_diameter']['kilometers']['estimated_diameter_max']
                velocidade = asteroide['close_approach_data'][0]['relative_velocity']['kilometers_per_hour']
                distancia = asteroide['close_approach_data'][0]['miss_distance']['kilometers']
                dados_asteroide.append({"dia":dia,"name":name,"diameter":diameter,"velocidade":velocidade,"distancia":distancia})
    df = pd.DataFrame(dados_asteroide)

    return df