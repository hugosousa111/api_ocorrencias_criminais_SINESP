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
from func_auxiliares import agrupa_por_estado
from func_auxiliares import append_municipio


class Thiago:
    def __init__(self):
        self.df_municipio = pd.read_excel('Bases/base_por_municipio.xlsx', sheet_name=["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"])
        self.df_estado = pd.read_excel('Bases/base_por_estado.xlsx', sheet_name=['Ocorrências', 'Vítimas'])

    def estado_top_x(self,tipo, x,crime):
        if tipo == "Vítimas":
            coluna_tipo = "Quant_Vítimas"
        else:
            coluna_tipo = "Quant_Ocorrências"
        palavras_tratadas = trata_vetor_palavra(self.df_estado[tipo]["Tipo Crime"])
        palavra = trata_palavra(crime)

        df_e = self.df_estado[tipo][palavras_tratadas == palavra]

        tabela_estado_crime = agrupa_por_estado(df_e,coluna_tipo)

        x = int(x)

        # Ordenando a base
        result = tabela_estado_crime.sort_values(coluna_tipo, ascending=False)

        # Pegandos os X primeiros
        result = result[:x]

        result = result.values.tolist()

        return result