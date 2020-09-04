import pandas as pd
import numpy as np

from func_auxiliares import converte_sigla_em_nome
from func_auxiliares import pega_mes
from func_auxiliares import pega_ano
from func_auxiliares import converte_para_data
from func_auxiliares import append_municipio
from func_auxiliares import pega_meses_menores
from func_auxiliares import pega_meses_intervalo
from func_auxiliares import trata_vetor_palavra
from func_auxiliares import trata_palavra
from func_auxiliares import data_inicio_eh_maior_data_fim
class Renato:
    def __init__(self):
        self.df_municipio = pd.read_excel('Bases/base_por_municipio.xlsx', sheet_name=["AC","AL","AP","AM","BA","CE","DF","ES","GO","MA","MT","MS","MG","PA","PB","PR","PE","PI","RJ","RN","RS","RO","RR","SC","SP","SE","TO"])
        self.df_estado = pd.read_excel('Bases/base_por_estado.xlsx', sheet_name=['Ocorrências','Vítimas'])

    # Metodo Modelo/Teste
    def municipios_regiao(self, regiao):
        # Junta todas as paginas da planilha em um só dataframe e corrige as datas
        base = append_municipio(self.df_municipio) 

        # Trato as palavras para poder comparar
        palavras_tratadas = trata_vetor_palavra(base["Região"])
        regiao_tratado = trata_palavra(regiao)
        
        #Busco todas as vezes que aquele região aparece
        base = base[palavras_tratadas == regiao_tratado]      
        result = base.values.tolist()
        return result

    
    def municipios_regiao_datas(self, regiao, data_inicio, data_fim):
        if data_inicio_eh_maior_data_fim(data_inicio, data_fim):
            result = []
            return result
        
        data_inicio = converte_para_data(data_inicio)
        data_fim = converte_para_data(data_fim)
        # Junta todas as paginas da planilha em um só dataframe e corrige as datas
        base = append_municipio(self.df_municipio) 
        
        # Trato as palavras para poder comparar
        palavras_tratadas = trata_vetor_palavra(base["Região"])
        regiao_tratado = trata_palavra(regiao)
        
        #Busco todas as vezes que aquele municipio aparece
        base = base[palavras_tratadas == regiao_tratado]

        base = base[(base["Mês/Ano"]>=data_inicio) & (base["Mês/Ano"]<=data_fim)]
        
        result = base.values.tolist()
        return result