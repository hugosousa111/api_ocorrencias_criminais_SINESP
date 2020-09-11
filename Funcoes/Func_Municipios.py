import pandas as pd
import numpy as np

from func_auxiliares import *

class Func_Municipios:
    def __init__(self):
        self.df_municipio = pd.read_excel('Bases/base_por_municipio.xlsx', sheet_name=["AC","AL","AP","AM","BA","CE","DF","ES","GO","MA","MT","MS","MG","PA","PB","PR","PE","PI","RJ","RN","RS","RO","RR","SC","SP","SE","TO"])    
    
    # Função 17
    def municipios(self):
        result = append_municipio(self.df_municipio)

        result = result.values.tolist()
        return result

    # Função 18
    def municipios_datas(self, data_inicio, data_fim):
        if data_inicio_eh_maior_data_fim(data_inicio, data_fim):
            result = []
            return result
        
        data_inicio = converte_para_data(data_inicio)
        data_fim = converte_para_data(data_fim)

        base = append_municipio(self.df_municipio)

        result = base[(base["Mês/Ano"]>=data_inicio) & (base["Mês/Ano"]<=data_fim)]

        result = result.values.tolist()
        return result

    # Função 19
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
   
    # Função 20
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

    # Função 21
    def municipios_estado(self, sigla):
        
        base = append_municipio(self.df_municipio) 

        base = base[(base["Sigla UF"] == sigla)]

        result = base.values.tolist()
        return result
        
    # Função 22    
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

    # Função 23
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
    
    # Função 24     
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
    
    # Função 25
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

    # Função 26
    def municipios_top_x_periodo(self, x, data_inicio, data_fim):
        x = int(x)

        if data_inicio_eh_maior_data_fim(data_inicio, data_fim):  # Se ordem das datas é passada errada
            result = ['Erro: data inicial maior que a data final']
            return result

        data_inicio = converte_para_data(data_inicio)
        data_fim = converte_para_data(data_fim)

        baseMun = append_municipio(self.df_municipio)  # Já corrige a coluna de datas
        baseMun = baseMun[(baseMun['Mês/Ano'] >= data_inicio) & (baseMun['Mês/Ano'] <= data_fim)]  # Pega apenas o intervalo passado por parâmetro
        baseMun = agrupa_por_municipio(baseMun)

        # Ordenando a base
        result = baseMun.sort_values('Quant_Vítimas', ascending=False)

        # Pegandos os X primeiros
        result = result[:x]
        result = result.values.tolist()
        return result

    # Função 27
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
    
    # Função 28
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

    # Função 29
    def municipios_total(self):
        base = append_municipio(self.df_municipio)

        result = agrupa_por_municipio(base)

        result = result.values.tolist()
        return result

    # Função 30
    def municipios_total_datas(self, data_inicio, data_fim):
        if data_inicio_eh_maior_data_fim(data_inicio, data_fim):
            result = []
            return result
        
        data_inicio = converte_para_data(data_inicio)
        data_fim = converte_para_data(data_fim)

        base = append_municipio(self.df_municipio)

        base = base[(base["Mês/Ano"]>=data_inicio) & (base["Mês/Ano"]<=data_fim)]
        result = agrupa_por_municipio(base)

        result = result.values.tolist()
        return result

    # Função 31
    def municipios_total_estado(self, sigla):
        base = append_municipio(self.df_municipio)

        base = base[(base["Sigla UF"] == sigla)]

        result = agrupa_por_municipio(base)

        result = result.values.tolist()
        return result
    
    # Função 32
    def municipios_total_estado_datas(self, sigla, data_inicio, data_fim):
        if data_inicio_eh_maior_data_fim(data_inicio, data_fim):
            result = []
            return result
        
        data_inicio = converte_para_data(data_inicio)
        data_fim = converte_para_data(data_fim)

        base = append_municipio(self.df_municipio)

        base = base[(base["Sigla UF"] == sigla)]
        #result = agrupa_por_municipio(base)

        base = base[(base["Mês/Ano"]>=data_inicio) & (base["Mês/Ano"]<=data_fim)]
        
        result = agrupa_por_municipio(base)

        result = result.values.tolist()
        return result
