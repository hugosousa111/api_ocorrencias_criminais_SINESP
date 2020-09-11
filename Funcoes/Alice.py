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

class Alice:
    def __init__(self):
        self.df_municipio = pd.read_excel('Bases/base_por_municipio.xlsx', sheet_name=["AC","AL","AP","AM","BA","CE","DF","ES","GO","MA","MT","MS","MG","PA","PB","PR","PE","PI","RJ","RN","RS","RO","RR","SC","SP","SE","TO"])

        #FUNÇÃO 21
    def municipios_estado(self, sigla):
        
        base = append_municipio(self.df_municipio) 

        base = base[(base["Sigla UF"] == sigla)]

        result = base.values.tolist()
        return result
        
        #FUNÇÃO 22
    def municipios_estado_datas(self, sigla, data_inicio, data_fim):
        #Verifica se a data informada é válida
        if data_inicio_eh_maior_data_fim(data_inicio, data_fim):
            result = []
            return result

        data_inicio = converte_para_data(data_inicio)
        data_fim = converte_para_data(data_fim)
        
        base = append_municipio(self.df_municipio) 

        base = base[(base["Sigla UF"] == sigla)]

        base = base[(base["Mês/Ano"]>=data_inicio) & (base["Mês/Ano"]<=data_fim)]

        result = base.values.tolist()
        return result
