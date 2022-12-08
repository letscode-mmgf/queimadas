import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from tratamento import dataset
from funcoes import *

st.set_page_config( layout='wide' )

st.markdown("<h1 style='text-align: center; color: grey;'>Queimadas no Brasil</h1>", unsafe_allow_html=True)

st.image(Image.open('mapa-do-brasil.png'))

st.title('Introdução')
st.write('Analisar as ocorrências de queimadas no Brasil, analisando critérios como regiões, meses, estações e evolução durante os anos')

analise = st.sidebar.selectbox(
    label="Tipo de Análise", 
    options=['Análise Univariada', 'Análise Bivariada', 'Análise Multivariada'])

if analise == 'Análise Univariada': n = 1
elif analise == 'Análise Bivariada': n = 2
elif analise == 'Análise Multivariada': n = 3

tipo = st.sidebar.radio(label='Tipo', options=['Linhas', 'Barras', 'Dispersão'], index=0)

criterios = st.sidebar.multiselect(
        label="Critérios", 
        options=['Anos', 'Regiões', 'Estações'],
        max_selections=n
)

if 'Estações' in criterios:
    estacoes = st.sidebar.multiselect(
        label='Estações', 
        options=['Outono', 'Inverno', 'Primavera', 'Verão'],
        default=['Outono', 'Inverno', 'Primavera', 'Verão']
    )

if 'Regiões' in criterios:
    regioes = st.sidebar.multiselect(
        label="Região", 
        options=['Norte', 'Nordeste', 'Sudeste', 'Sul', 'Centro Oeste', 'Centro'],
        default=['Norte', 'Nordeste', 'Sudeste', 'Sul', 'Centro Oeste', 'Centro']
    )

if 'Anos' in criterios:
    anos = st.sidebar.select_slider(label='Anos', options=(list(range(1998, 2018, 1))))
    
st.title('Descrição dos dados')
st.write('Os dados forem obtidos de uma fonte primária, abrangendo ocorrências de queimadas florestais no período de 1998 a 2017.')
st.write('Os dados estão disponíveis através do kaggle pela URL abaixo:')
st.write('https://www.kaggle.com/datasets/gustavomodelli/forest-fires-in-brazil')


st.write('Uma breve análise exploratória revela a natureza dos nossos dados:')

df = dataset()
st.dataframe(df.head())

st.write('Gráfico')

""" 


#st.table(df.info())
#descobrir como imprimir um info no streamlit


st.write(regioes)
filtro_regiao = []

st.write(teste(regioes))

if analise == 'Análise Univariada' and tipo == 'Linhas':
    st.plotly_chart(get_line_chart(df))

st.plotly_chart(get_histogram(df, filtro_regiao))

rotulos = st.checkbox(label='Mostrar rótulos', value=False) """
