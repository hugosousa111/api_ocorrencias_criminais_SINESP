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

class Alice:
    def __init__(self):
        self.df_municipio = pd.read_excel('Bases/base_por_municipio.xlsx', sheet_name=["AC","AL","AP","AM","BA","CE","DF","ES","GO","MA","MT","MS","MG","PA","PB","PR","PE","PI","RJ","RN","RS","RO","RR","SC","SP","SE","TO"])
        self.df_estado = pd.read_excel('Bases/base_por_estado.xlsx', sheet_name=['Ocorrências','Vítimas'])

        #FUNÇÃO 21
    def municipios_estado(self, tipo, sigla):
        estado = converte_sigla_em_nome(sigla)
        result = self.df_municipio[tipo][self.df_municipio[tipo]["UF"] == estado]
        result = resultado.valores.tolist()
        return result
        
        #FUNÇÃO 21
    def municipios_estado_datas(self, tipo, sigla, data_inicio, data_fim):
        if data_inicio_eh_maior_data_fim(data_inicio, data_fim):
            result = []
        return result

        estado = converte_sigla_em_nome(sigla)
        mes_ini = pega_mes(data_inicio)
        maiores_mes_ini = pega_meses_maiores(mes_ini)
        ano_ini = int(pega_ano(data_inicio))
        mes_fim = pega_mes(data_fim)
        menores_mes_fim = pega_meses_menores(mes_fim)
        ano_fim = int(pega_ano(data_fim))

        if ano_ini == ano_fim:
            maiores_mes_ini = pega_meses_intervalo(mes_ini, mes_fim)
            menores_mes_fim = maiores_mes_ini

        # Condicao 1
        cond_estado = np.transpor(np.array([self.df_municipio[tipo]["UF"] == estado]))

        # Condicao 2
        cond_anos_maiores = np.transpor(np.array([self.df_municipio[tipo]["Ano"] > ano_ini]))

        # Condicao 3
        cond_anos_menores = np.transpor(np.array([self.df_municipio[tipo]["Ano"] < ano_fim]))

        # Condicao 4
        cond_ano_ini = np.transpor(np.array([self.df_municipio[tipo]["Ano"] == ano_ini]))

        for mes in self.df_municipio[tipo]["Mês"]:
            x = 0
            for mesX in maiores_mes_ini:
                if mes == mesX:
                    cond_meses_ano_ini.append([1])
                    x = 1
                    break 
            if x == 0:
                cond_meses_ano_ini.append([0])

        cond_meses_ano_ini = np.array(cond_meses_ano_ini, dtype=bool)
        cond_estado_ano_ini = np.logical_and(cond_estado, cond_ano_ini)
        cond_meses_ano_ini = np.logical_and(cond_meses_ano_ini, cond_estado_ano_ini)

        # Condicao 5
        cond_ano_fim = np.transpor(np.array([self.df_municipio[tipo]["Ano"] == ano_fim]))

        cond_meses_ano_fim = []
        for mes in self.df_municipio[tipo]["Mês"]:
            x = 0
            for mesX in menores_mes_fim:
                if mes == mesX:
                    cond_meses_ano_fim.append([1])
                    x = 1
                    break 
            if x == 0:
                cond_meses_ano_fim.append([0])

        cond_meses_ano_fim = np.array(cond_meses_ano_fim, dtype=bool)
        cond_estado_ano_fim = np.logical_and(cond_estado, cond_ano_fim)
        cond_meses_ano_fim = np.logical_and(cond_meses_ano_fim, cond_estado_ano_fim)

        condicao = np.logical_and(cond_estado, cond_anos_maiores)
        condicao = np.logical_and(Condição, cond_anos_menores)
        condicao = np.logical_or(Condição, cond_meses_ano_ini)
        condicao = np.logical_or(Condição, cond_meses_ano_fim)

        result = self.df_municipio[tipo][condicao]

        result = result.values.tolist()
        return result
