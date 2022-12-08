import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from PIL import Image
from tratamento import dataset
from funcoes import personalizacao

st.set_page_config( layout='wide' )

st.markdown("<h1 style='text-align: center; color: grey;'>Queimadas no Brasil</h1>", unsafe_allow_html=True)

st.image(Image.open('mapa-do-brasil.png'))

st.title('Introdução')
st.write('Analisar as ocorrências de queimadas no Brasil, analisando critérios como regiões, meses, estações e evolução durante os anos')

analise = st.sidebar.selectbox(
    label="Tipo de Análise", 
    options=['Análise Univariada', 'Análise Bivariada', 'Análise Multivariada'])

tipo = st.sidebar.radio(label='Tipo', options=['Linhas', 'Barras', 'Dispersão'], index=0)

anos = st.sidebar.select_slider(label='Anos', options=(list(range(1998, 2018, 1))))

regiao = st.sidebar.multiselect(
    label="Região", 
    options=['Norte', 'Nordeste', 'Sudeste', 'Sul', 'Centro Oeste', 'Centro']
)

estacoes = st.sidebar.multiselect(
    label='Estações', 
    options=['Outono', 'Inverno', 'Primavera', 'Verão']
)


st.title('Descrição dos dados')
st.write('Os dados forem obtidos de uma fonte primária, abrangendo ocorrências de queimadas florestais no período de 1998 a 2017.')
st.write('Os dados estão disponíveis através do kaggle pela URL abaixo:')
st.write('https://www.kaggle.com/datasets/gustavomodelli/forest-fires-in-brazil')


st.write('Uma breve análise exploratória revela a natureza dos nossos dados:')

# ---- modularizar essa parte -----
df = dataset()
columns=('col %d' % i for i in range(20))

st.dataframe(df)  # deixar somente isso

st.write('Gráfico')


fig = px.histogram(data_frame=df,
                    x='state', 
                    y='number',
                    color='season', 
                    barmode='group', 
                    histfunc='avg')
personalizacao(fig, 'Estados', 'Média de Queimadas', 'Estações')
st.plotly_chart(fig)


rotulos = st.checkbox(label='Mostrar rótulos', value=False)
