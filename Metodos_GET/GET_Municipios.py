from flask_restful import Resource
from flask import jsonify

import sys
sys.path.insert(0, '../Funcoes')

# Funcoes
from Funcoes.Func_Municipios import Func_Municipios
f = Func_Municipios()

# Função 17
class Municipios(Resource):
    def get(self):
        try:
            result = f.municipios()
        except:
            result = []
        finally:
            return jsonify(result)

# Função 18
class Municipios_datas(Resource):
    def get(self, data_inicio, data_fim):
        try:
            result = f.municipios_datas(data_inicio, data_fim)
        except:
            result = []
        finally:
            return jsonify(result)

#Funcao 19
class Municipios_regiao(Resource):
    def get(self, regiao):
        try:
            result = f.municipios_regiao(regiao)
        except:
            result = []
        finally:
            return jsonify(result)

#Funcao 20
class Municipios_regiao_datas(Resource):
    def get(self, regiao, data_inicio, data_fim):
        try:
            result = f.municipios_regiao_datas(regiao, data_inicio, data_fim)
        except:
            result = []
        finally:
            return jsonify(result)

#Funcao 21
class Municipios_estado(Resource):
    def get(self, sigla):
        try:
            result = f.municipios_estado(sigla)
        except:
            result = []
        finally:
            return jsonify(result) 

#Funcao 22    
class Municipios_estado_datas(Resource):
    def get(self, sigla, data_inicio, data_fim):
        try:
            result = f.municipios_estado_datas(sigla, data_inicio, data_fim)
        except:
            result = []
        finally:
            return jsonify(result)         

#Funcao 23
class Municipio_com_Estado (Resource):
    def get(self, sigla, municipio):
        try:
            result = f.municipio_com_estado(sigla, municipio)
        except:
            result = []
        finally:
            return jsonify(result)

#Funcao 24
class Municipio_com_Estado_datas (Resource):
    def get(self, sigla, municipio, data_inicio, data_fim):
        try:
            result = f.datas_municipios(sigla, municipio, data_inicio, data_fim)
        except:
            result = []
        finally:
            return jsonify(result)

#Funcao 25
class Municipios_topX_vitimas(Resource):
    def get(self, x):
        try:
            result = f.municipios_top_x(x)
        except:
            result = []
        finally:
            return jsonify(result)

#Funcao 26
class Municipios_topX_vitimas_periodo(Resource):
    def get(self, x, data_inicio, data_fim):
        try:
            result = f.municipios_top_x_periodo(x, data_inicio, data_fim)
        except:
            result = []
        finally:
            return jsonify(result)

#Funcao 27
class Municipios_top_estado(Resource):
    def get(self,X,sigla):
        try:
            result = f.Municipio_top_estado(X,sigla)
        except:
            result = []
        finally:
            return jsonify(result)

#Funcao 28
class Municipios_top_estado_por_periodo(Resource):
    def get(self,X,sigla,data_inicio,data_fim):
        try:
            result = f.Municipio_top_estado_periodo(X,sigla,data_inicio, data_fim)
        except:
            result = []
        finally:
            return jsonify(result)

# Função 29
class Municipios_total(Resource):
    def get(self):
        try:
            result = f.municipios_total()
        except:
            result = []
        finally:
            return jsonify(result)

# Função 30
class Municipios_total_datas(Resource):
    def get(self, data_inicio, data_fim):
        try:
            result = f.municipios_total_datas(data_inicio, data_fim)
        except:
            result = []
        finally:
            return jsonify(result)

# Função 31
class Municipios_total_estado(Resource):
    def get(self, sigla):
        try:
            result = f.municipios_total_estado(sigla)
        except:
            result = []
        finally:
            return jsonify(result)

# Função 32
class Municipios_total_estado_datas(Resource):
    def get(self, sigla, data_inicio, data_fim):
        try:
            result = f.municipios_total_estado_datas(sigla, data_inicio, data_fim)
        except:
            result = []
        finally:
            return jsonify(result)
