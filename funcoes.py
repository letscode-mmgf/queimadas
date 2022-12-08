import plotly.express as px

def personalizacao(variavel: vars, tit_x: str, tit_y: str, tit_leg: str):
    """Personalização

    Args:
        variavel (vars): Variável correspondente ao gráfico que quer realizar a personalização
        tit_x (str): Título do eixo X do gráfico
        tit_y (str): Título do eixo Y do gráfico
        tit_leg (str): Título do iterável do gráfico

    Returns:
        Figure: Retorna o gráfico personalizado com titulos, padrões de cores e layout dark
    """
    return variavel.update_layout(
                xaxis_title={
                    'text': tit_x,
                    'font_size': 12
                },
                yaxis_title={
                    'text': tit_y,
                    'font_size': 12
                },
                legend_title={
                    'text': tit_leg,
                    'font_size': 12
                },
                font_color='grey',
                font_size=10,
                
                template='plotly_dark')

def get_histogram(df, regioes):

    if len(regioes) == 0: df_filtrado = df

    if len(regioes) > 0:
        filtro = (df['region'] in regioes)
        df_filtrado = df[filtro]

    fig = px.histogram(data_frame=df_filtrado,
                        x='state', 
                        y='number',
                        color='season', 
                        barmode='group', 
                        histfunc='avg')

    personalizacao(fig, 'Estados', 'Média de Queimadas', 'Estações')
    return fig

def get_line_chart(df):
    df_plot = df.groupby('year')['number'].sum().reset_index().sort_values(by= 'year')
    linha = px.line(data_frame=df_plot, x='year', y='number', markers=True, template='plotly_dark')
    personalizacao(linha, 'Anos', 'Número de Queimadas Registradas', None)
    return linha

def teste(regioes):
    filtro_regiao = []
    for i, valor in enumerate(regioes):
        filtro_regiao.append(valor)

    return filtro_regiao