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
from func_auxiliares import append_municipio
from func_auxiliares import agrupa_por_municipio
class Fabricio:
    def __init__(self):
        self.df_municipio = pd.read_excel('Bases/base_por_municipio.xlsx', sheet_name=["AC","AL","AP","AM","BA","CE","DF","ES","GO","MA","MT","MS","MG","PA","PB","PR","PE","PI","RJ","RN","RS","RO","RR","SC","SP","SE","TO"])
        self.df_estado = pd.read_excel('Bases/base_por_estado.xlsx', sheet_name=['Ocorrências','Vítimas'])

    def Municipio_top_estado(self,X,sigla):
        X = int(X)
        baseMun = append_municipio(self.df_municipio)
        baseMun = baseMun[(baseMun["Sigla UF"] == sigla)]
        result = agrupa_por_municipio(baseMun)

        # Ordenando a base
        result = result.sort_values('Quant_Vítimas', ascending=False)

        # Pegandos os X primeiros
        result = result[:X]
        result = result.values.tolist()
        return result
        
        """
        estado = self.df_municipio[sigla].values.tolist()
        count = Counter()
        for municipio, uf, regiao, date, vitimas in estado:
            count.update({municipio: vitimas})
        final = list(count.items())
        final.sort(key=lambda x: x[1], reverse=True)
        return final[0:X]
        """
    def Municipio_top_estado_periodo(self,X,sigla,data_inicio, data_fim):
        X = int(X)

        if data_inicio_eh_maior_data_fim(data_inicio, data_fim):  # Se ordem das datas é passada errada
            result = ['Erro: data inicial maior que a data final']
            return result

        data_inicio = converte_para_data(data_inicio)
        data_fim = converte_para_data(data_fim)

        baseMun = append_municipio(self.df_municipio)  # Já corrige a coluna de datas
        baseMun = baseMun[(baseMun["Sigla UF"] == sigla)]
        baseMun = baseMun[(baseMun['Mês/Ano'] >= data_inicio) & (baseMun['Mês/Ano'] <= data_fim)]  # Pega apenas o intervalo passado por parâmetro
        baseMun = agrupa_por_municipio(baseMun)

        # Ordenando a base
        result = baseMun.sort_values('Quant_Vítimas', ascending=False)

        # Pegandos os X primeiros
        result = result[:X]
        result = result.values.tolist()
        return result

        
        """
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
        """