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


def get_line_chart(df):
    df_plot = df.groupby('year')['number'].sum(
    ).reset_index().sort_values(by='year')
    linha = px.line(data_frame=df_plot, x='year', y='number',
                    markers=True, template='plotly_dark')
    personalizacao(linha, 'Anos', 'Número de Queimadas Registradas', None)
    return linha


def get_histogram(df):

    histogram = px.histogram(data_frame=df,
                             x='state',
                             y='number',
                             color='season',
                             barmode='group',
                             histfunc='avg')

    personalizacao(histogram, 'Estados', 'Média de Queimadas', 'Estações')
    return histogram


def get_dispersion(df):

    grafico = px.scatter(data_frame=df,
                         x='year',
                         y='number',
                         color='species')

    personalizacao(grafico, 'Anos', 'Número de Queimadas Registradas',
                   'Ano', 'Quantidade de ocorrência')
    return grafico


def get_line_chart_bivariada(df, **kwargs):

    colunas = list(kwargs.keys())
    df_agrupado = df.groupby(colunas)['number'].sum().reset_index()
    grafico = px.line(data_frame=df_agrupado,
                      x=colunas[0], y='number', color=colunas[1], markers=False, template='plotly_dark')

    personalizacao(grafico, 'Anos',
                   'Número de Queimadas Registradas', 'Regiões do Brasil')

    return grafico
