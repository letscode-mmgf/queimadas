estacao = {'Janeiro': 'Verão', 'Fevereiro': 'Verão', 'Março': 'Verão',
            'Abril': 'Outono', 'Maio': 'Outono', 'Junho': 'Outono',
            'Julho': 'Inverno', 'Agosto': 'Inverno', 'Setembro': 'Inverno',
            'Outubro': 'Primavera', 'Novembro': 'Primavera', 'Dezembro': 'Primavera'}


dict_meses = {'Janeiro': '01', 'Fevereiro': '02', 'Março': '03',
            'Abril': '04', 'Maio': '05', 'Junho': '06',
            'Julho': '07', 'Agosto': '08', 'Setembro': '09',
            'Outubro': '10', 'Novembro': '11', 'Dezembro': '12'}

regioes = {'Acre': 'Norte', 'Roraima': 'Norte', 'Amazonas': 'Norte', 'Pará': 'Norte', 'Tocantins': 'Norte',
            'Rondonia': 'Norte', 'Maranhao': 'Nordeste', 'Piau': 'Nordeste', 'Bahia': 'Nordeste',
            'Pernambuco': 'Nordeste', 'Alagoas': 'Nordeste', 'Sergipe': 'Nordeste', 'Rio Grande do Norte': 'Nordeste',
            'Ceara': 'Nordeste', 'Paraiba': 'Nordeste', 'Amapa': 'Sudeste',
            'Mato Grosso': 'Centro-Oeste', 'Distrito Federal': 'Centro-Oeste', 'Goias': 'Centro-Oeste',
            'Minas Gerais': 'Sudeste', 'Espirito Santo': 'Sudeste', 'Rio': 'Sudeste', 'Sao Paulo': 'Sudeste',
            'Parana': 'Sul', 'Santa Catarina': 'Sul', 'Rio Grande do Sul': 'Sul'}

siglas = {'Acre': 'AC', 'Roraima': 'RR', 'Amazonas': 'AM', 'Pará': 'PA', 'Tocantins': 'TO',
            'Rondonia': 'RO', 'Maranhao': 'MA', 'Piau': 'PI', 'Bahia': 'BA',
            'Pernambuco': 'PE', 'Alagoas': 'AL', 'Sergipe': 'SE', 'Rio Grande do Norte': 'RN',
            'Ceara': 'CE', 'Paraiba': 'PB', 'Amapa': 'AP',
            'Mato Grosso': 'MT', 'Distrito Federal': 'DF', 'Goias': 'GO',
            'Minas Gerais': 'MG', 'Espirito Santo': 'ES', 'Rio': 'RJ', 'Sao Paulo': 'SP',
            'Parana': 'PR', 'Santa Catarina': 'SC', 'Rio Grande do Sul': 'RS'}

def dataset():
    """Dataset

    Returns:
        DataFrame: Retorna o dataframe já tratado utilizado para a análise.
    """
    import pandas as pd

    df =pd.read_csv('amazon.csv', sep = ',', encoding='ISO-8859-1')

    df['estacoes'] = df['month'].map(estacao)
    df['date'] = df['month'].map(dict_meses)
    df['regioes'] = df['state'].map(regioes)
    df['state'] = df['state'].map(siglas) 
    df = df.rename(columns={'estacoes':'season', 'regioes': 'region'})  
    return df