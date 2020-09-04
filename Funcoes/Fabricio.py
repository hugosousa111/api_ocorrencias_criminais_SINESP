import pandas as pd
from collections import Counter
import datetime
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
class Fabricio:
    def __init__(self):
        self.df_municipio = pd.read_excel('Bases/base_por_municipio.xlsx', sheet_name=["AC","AL","AP","AM","BA","CE","DF","ES","GO","MA","MT","MS","MG","PA","PB","PR","PE","PI","RJ","RN","RS","RO","RR","SC","SP","SE","TO"])
        self.df_estado = pd.read_excel('Bases/base_por_estado.xlsx', sheet_name=['Ocorrências','Vítimas'])

    def Municipio_top_estado(self,X,sigla):
        estado = self.df_municipio[sigla].values.tolist()
        count = Counter()
        for municipio, uf, regiao, date, vitimas in estado:
            count.update({municipio: vitimas})
        final = list(count.items())
        final.sort(key=lambda x: x[1], reverse=True)
        return final[0:X]
        
    def Municipio_top_estado_periodo(self,X,sigla,data_fim,data_inicio):
        timeStampConvert = lambda x: datetime.datetime.strptime(x, "%Y-%m-%d")
        inicio = timeStampConvert(converte_para_data(data_fim))
        print(type(inicio))
        fim = timeStampConvert(converte_para_data(data_inicio))
        print(fim)
        estado = self.df_municipio[sigla].values.tolist()
        estado = filter(lambda x: x[3] >= inicio and x[3] <= fim, estado)
        estado = list(estado)
        count = Counter()
        for municipio, uf, regiao, date, vitimas in estado:
            count.update({municipio: vitimas})
        final = list(count.items())
        final.sort(key=lambda x: x[1], reverse=True)
        return final[0:X]
