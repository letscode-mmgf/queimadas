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


