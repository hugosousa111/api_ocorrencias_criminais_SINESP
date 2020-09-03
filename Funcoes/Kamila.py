import pandas as pd
import numpy as np

from func_auxiliares import converte_sigla_em_nome
from func_auxiliares import pega_mes
from func_auxiliares import pega_ano
from func_auxiliares import converte_para_data
from func_auxiliares import pega_meses_maiores
from func_auxiliares import pega_meses_menores
from func_auxiliares import pega_meses_intervalo
from func_auxiliares import trata_vetor_palavra
from func_auxiliares import trata_palavra
from func_auxiliares import data_inicio_eh_maior_data_fim
from func_auxiliares import append_municipio

class Kamila:
    def __init__(self):
        self.df_municipio = pd.read_excel('Bases/base_por_municipio.xlsx', sheet_name=["AC","AL","AP","AM","BA","CE","DF","ES","GO","MA","MT","MS","MG","PA","PB","PR","PE","PI","RJ","RN","RS","RO","RR","SC","SP","SE","TO"])
    ##################### Função 23
    def municipio_com_estado(self, sigla, municipio):
        # Junta todas as paginas da planilha em um só dataframe e corrige as datas
        base = append_municipio(self.df_municipio) 

        # Pego só os dados daquele estado
        base = base[(base["Sigla UF"] == sigla)]

        # Trato as palavras para poder comparar
        palavras_tratadas = trata_vetor_palavra(base["Município"])
        municipio_tratado = trata_palavra(municipio)
        
        #Busco todas as vezes que aquele municipio aparece
        base = base[palavras_tratadas == municipio_tratado]      
        result = base.values.tolist()
        return result

        ##################### Função 24
    def datas_municipios(self, sigla, municipio, data_inicio, data_fim):
        if data_inicio_eh_maior_data_fim(data_inicio, data_fim):
            result = []
            return result
        
        data_inicio = converte_para_data(data_inicio)
        data_fim = converte_para_data(data_fim)
        # Junta todas as paginas da planilha em um só dataframe e corrige as datas
        base = append_municipio(self.df_municipio) 
        # Pego só os dados daquele estado
        base = base[(base["Sigla UF"] == sigla)]

        # Trato as palavras para poder comparar
        palavras_tratadas = trata_vetor_palavra(base["Município"])
        municipio_tratado = trata_palavra(municipio)
        
        #Busco todas as vezes que aquele municipio aparece
        base = base[palavras_tratadas == municipio_tratado]

        base = base[(base["Mês/Ano"]>=data_inicio) & (base["Mês/Ano"]<=data_fim)]
        
        result = base.values.tolist()
        return result
        
