import pandas as pd
import numpy as np

from func_auxiliares import append_municipio
from func_auxiliares import agrupa_por_municipio
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

class Angela:
    def __init__(self):
        self.df_municipio = pd.read_excel('Bases/base_por_municipio.xlsx', sheet_name=["AC","AL","AP","AM","BA","CE","DF","ES","GO","MA","MT","MS","MG","PA","PB","PR","PE","PI","RJ","RN","RS","RO","RR","SC","SP","SE","TO"])
        self.df_estado = pd.read_excel('Bases/base_por_estado.xlsx', sheet_name=['Ocorrências','Vítimas'])

    # Metodo Modelo/Teste
    def funcao_angela(self):
        result = "Angela"
        return result

    def municipios_top_x(self, x):
        x = int(x)
        baseMun = append_municipio(self.df_municipio)
        result = agrupa_por_municipio(baseMun)

        # Ordenando a base
        result = result.sort_values('Quant_Vítimas', ascending=False)

        # Pegandos os X primeiros
        result = result[:x]
        result = result.values.tolist()
        return result
