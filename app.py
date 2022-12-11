import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from tratamento import filtragem, dataset
from plotagem import *

st.set_page_config(layout='wide')

# ---------------- SIDEBAR ---------------------------

filtros = st.sidebar.multiselect(
    label="Filtros",
    options=['Anos', 'Regiões', 'Estações']
)

anos = list(range(1998, 2017, 1))
regioes = ['Norte', 'Nordeste', 'Sudeste', 'Sul', 'Centro Oeste', 'Centro']
estacoes = ['Outono', 'Inverno', 'Primavera', 'Verão']

if 'Estações' in filtros:
    estacoes = st.sidebar.multiselect(
        label='Estações',
        options=['Outono', 'Inverno', 'Primavera', 'Verão'],
        default=['Outono', 'Inverno', 'Primavera', 'Verão']
    )

if 'Regiões' in filtros:
    regioes = st.sidebar.multiselect(
        label="Região",
        options=['Norte', 'Nordeste', 'Sudeste',
                 'Sul', 'Centro Oeste', 'Centro'],
        default=['Norte', 'Nordeste', 'Sudeste',
                 'Sul', 'Centro Oeste', 'Centro']
    )

if 'Anos' in filtros:
    anos = st.sidebar.slider('Anos', 1998, 2017, (1998, 2017))

df = dataset()
df = filtragem(df, anos, regioes, estacoes)

# --------------- Conteúdo principal -------------------
st.title('Queimadas no Brasil')

rotulos = st.checkbox(label='Mostrar cabeçalho', value=False)
if rotulos:
    st.title('Descrição dos dados')
    st.write('Os dados forem obtidos de uma fonte primária, abrangendo ocorrências de queimadas florestais no período de 1998 a 2017.')
    st.write('Os dados estão disponíveis através do kaggle pela URL abaixo:')
    st.write('https://www.kaggle.com/datasets/gustavomodelli/forest-fires-in-brazil')
    st.write('- Filipe Sousa')
    st.write('- Guilherme Oliveira')
    st.write('- Marcelo Mesquita')
    st.write('- Marina Maracajá')

    st.title('Amostra dos Dados')
    st.write(
        'Uma breve análise exploratória para revelar a natureza dos nossos dados:')
    st.dataframe(df.head())

st.title('Objetivos')
st.write('Salientar quais são os intervalos temporais com maiores números de queimadas florestais de acordo com as regiões e estações do ano.')

st.title('Tipos de Análises')

analise = st.selectbox(
    label="Tipo de Análise",
    options=['Análise Univariada', 'Análise Bivariada', 'Análise Multivariada'])

if analise == 'Análise Univariada':

    col1, col2 = st.columns(2)

    col1.plotly_chart(get_line_chart(df), use_column_width=True)

    col2.plotly_chart(get_histogram(df), use_column_width=True)

    st.title("Análise")
    st.write('Pode-se visualizar que houve um crescimento expressivo no número de queimadas a partir do ano 2000, seguido de um período de queda entre 2003 e 2011. Em 2011 pode ser observado um novo aumento na quantidade de queimadas.')
    st.write('Também é notável que as queimadas acontecem majoritariamento durante o inverno (possivelmente devido ao baixa na umidade do ar.')

if analise == 'Análise Bivariada':

    criterios = st.multiselect(
        label="Escolha 2 critérios",
        options=['Anos', 'Regiões', 'Estações'],
        max_selections=2
    )

    col1, col2 = st.columns(2)

    if 'Anos' in criterios and 'Regiões' in criterios:

        col1.plotly_chart(get_line_chart_bivariada(
            df, year=list(range(anos[0], anos[1], 1)), region=regioes), use_column_width=True)
        col2.plotly_chart(get_bar_chart_bivariada(
            df, year=list(range(anos[0], anos[1], 1)), region=regioes), use_column_width=True)

    if 'Anos' in criterios and 'Estações' in criterios:
        col1.plotly_chart(get_line_chart_bivariada(
            df, year=list(range(anos[0], anos[1], 1)), season=estacoes), use_column_width=True)
        col2.plotly_chart(get_bar_chart_bivariada(
            df, year=list(range(anos[0], anos[1], 1)), season=estacoes), use_column_width=True)

    if 'Regiões' in criterios and 'Estações' in criterios:
        col1.plotly_chart(get_line_chart_bivariada(
            df, region=regioes, season=estacoes), use_column_width=True)
        col2.plotly_chart(get_bar_chart_bivariada(
            df, region=regioes, season=estacoes), use_column_width=True)

    st.title("Análise")
    st.write('Pode-se ver que as queimadas acontecem majoritariamente nos estados do norte, nordeste e sudeste do Brasil.')

if analise == 'Análise Multivariada':
    st.title('Análise Multivariada')

    st.title("Análise")
    st.write('Ainda não foi possível concluir as Análise Multivariadas')

st.title("Conclusão")
st.write('Após analisar os dados, podemos concluir que os estados os estados do nordeste são campeões em queimadas e que (embora tenham existidos períodos de queda) existe uma tendência de crescimento no número de queimadas no Brasil.')
