import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from tratamento import dataset
from funcoes import *

st.set_page_config( layout='wide' )

st.markdown("<h1 style='text-align: center; color: grey;'>Queimadas no Brasil</h1>", unsafe_allow_html=True)

analise = st.sidebar.selectbox(
    label="Tipo de Análise", 
    options=['Análise Univariada', 'Análise Bivariada', 'Análise Multivariada'])

tipo = st.sidebar.radio(label='Tipo', options=['Linhas', 'Barras', 'Dispersão'], index=0)

if analise != 'Análise Univariada':
    if analise == 'Análise Bivariada': n = 2
    elif analise == 'Análise Multivariada': n = 3

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

    if 'Anos' in criterios: anos = st.sidebar.slider('Anos', 1998, 2017, (1998, 2017))
    
df = dataset()
st.write('Amostra dos Dados')
st.dataframe(df.head())

st.write('Gráfico')

if analise == 'Análise Univariada':
    if tipo == 'Linhas': st.plotly_chart(get_line_chart(df))
    elif tipo == 'Barras': st.plotly_chart(get_histogram(df))
    elif tipo == 'Dispersão': st.write('ADICIONAR GRÁFICO DE DISPERSÃO')#st.plotly_chart(get_dispersion(df))

if analise == 'Análise Bivariada':
    if tipo == 'Linhas':
        if 'Anos' in criterios and 'Regiões' in criterios:
            st.plotly_chart(get_line_chart_bivariada(df, year=list(range(anos[0], anos[1], 1)), region=regioes))
        
        if 'Anos' in criterios and 'Estações' in criterios:
            st.plotly_chart(get_line_chart_bivariada(df, year=list(range(anos[0], anos[1], 1)), season=estacoes))

        if 'Regiões' in criterios and 'Estações' in criterios:
            st.plotly_chart(get_line_chart_bivariada(df, region=regioes, season=estacoes))

    elif tipo == 'Barras': st.plotly_chart(get_histogram(df))
    elif tipo == 'Dispersão': st.plotly_chart(get_histogram(df))

rotulos = st.checkbox(label='Mostrar rótulos', value=False)