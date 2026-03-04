import streamlit as st
import pandas as pd
import plotly.express as px
from utils import puxa_dados_api_nasa

st.title('Asteróides Próximos ao Planeta Terra')

st.write('Essa é uma aplicação pra consultar a API da NASA sobre os Asteroides mais próximos da terra e criar uma visualização no Plotly.')

start_date = st.date_input('Data de Início', value=pd.to_datetime("2024-12-01"))
end_date = st.date_input('Data Fim', value=pd.to_datetime("2024-12-03"))

if (end_date - start_date).days > 7:
    st.warning('A diferença de dias é maior do que 7, a API não funcionará. Ajuste o Período pra até 7')
else:
    if st.button('Buscar Dados'):
        with st.spinner('Executando a chamada a API:'):
            df = puxa_dados_api_nasa(start_date=start_date,end_date=end_date)
            if not df.empty:
                st.success('Dataframe coletado com Sucesso da API!')
                st.subheader('DataFrame:')
                st.dataframe(df)

                st.subheader('Diâmetro dos asteróides')
                graf_diametros = px.bar(df,x='name',y='diameter', title='Tamanho dos asteróides (em Km)')
                st.plotly_chart(graf_diametros)

                st.subheader('Velocidade vs Distância dos asteróides')
                graf_vel_vs_distancia = px.scatter(df,x='distancia',y='velocidade', title='Velocidade (em Km/h) vs Distância dos asteróides (em Km)')
                st.plotly_chart(graf_vel_vs_distancia)




