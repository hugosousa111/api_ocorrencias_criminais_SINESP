from flask_restful import Resource
from flask import jsonify

import sys
sys.path.insert(0, '../Funcoes')

# Funcoes
from Funcoes.Func_Estados import Func_Estados
f = Func_Estados()

ocorrencias = "Ocorrências"
vitimas = "Vítimas"

# Função 01
class Est_ocorrencias(Resource):
    def get(self):
        try:
            result = f.estados(ocorrencias)
        except:
            result = []
        finally:
            return jsonify(result)

# Função 02
class Est_ocorrencias_estado(Resource):
    def get(self, sigla):
        try:
            result = f.estados_estado(ocorrencias,sigla)
        except:
            result = []
        finally:
            return jsonify(result)

# Função 03
class Est_ocorrencias_estado_datas(Resource):
    def get(self, sigla, data_inicio, data_fim):
        try:
            result = f.estados_estado_datas(ocorrencias,sigla, data_inicio, data_fim)
        except:
            result = []
        finally:
            return jsonify(result)

# Função 04
class Est_ocorrencias_crime(Resource):
    def get(self, crime):
        try:
            result = f.estados_crime(ocorrencias, crime)
        except:
            result = []
        finally:
            return jsonify(result)

# Função 05
class Est_ocorrencias_crime_datas(Resource):
    def get(self, crime, data_inicio, data_fim):
        try:
            result = f.estados_crime_datas(ocorrencias, crime, data_inicio, data_fim)
        except:
            result = []
        finally:
            return jsonify(result)

# Função 06
class Est_ocorrencias_estado_crime(Resource):
    def get(self, sigla, crime):
        try:
            result = f.estados_estado_crime(ocorrencias, sigla, crime)
        except:
            result = []
        finally:
            return jsonify(result)

# Função 07
class Est_ocorrencias_estado_crime_datas(Resource):
    def get(self, sigla, crime, data_inicio, data_fim):
        try:
            result = f.estados_estado_crime_datas(ocorrencias, sigla, crime, data_inicio, data_fim)
        except:
            result = []
        finally:
            return jsonify(result)

# Função 08
class estado_topX_ocorrencias(Resource):
    def get(self,x,crime):
        try:
            result = f.estado_top_x(ocorrencias, x,crime)
        except:
            result = []
        finally:
            return jsonify(result)

# Função 09
class Est_vitimas(Resource):
    def get(self):
        try:
            result = f.estados(vitimas)
        except:
            result = []
        finally:
            return jsonify(result)

# Função 10
class Est_vitimas_estado(Resource):
    def get(self, sigla):
        try:
            result = f.estados_estado(vitimas,sigla)
        except:
            result = []
        finally:
            return jsonify(result)

# Função 11
class Est_vitimas_estado_datas(Resource):
    def get(self, sigla, data_inicio, data_fim):
        try:
            result = f.estados_estado_datas(vitimas,sigla, data_inicio, data_fim)
        except:
            result = []
        finally:
            return jsonify(result)

# Função 12
class Est_vitimas_crime(Resource):
    def get(self, crime):
        try:
            result = f.estados_crime(vitimas, crime)
        except:
            result = []
        finally:
            return jsonify(result)

# Função 13
class Est_vitimas_crime_datas(Resource):
    def get(self, crime, data_inicio, data_fim):
        try:
            result = f.estados_crime_datas(vitimas, crime, data_inicio, data_fim)
        except:
            result = []
        finally:
            return jsonify(result)

# Função 14
class Est_vitimas_estado_crime(Resource):
    def get(self, sigla, crime):
        try:
            result = f.estados_estado_crime(vitimas, sigla, crime)
        except:
            result = []
        finally:
            return jsonify(result)

# Função 15
class Est_vitimas_estado_crime_datas(Resource):
    def get(self, sigla, crime, data_inicio, data_fim):
        try:
            result = f.estados_estado_crime_datas(vitimas, sigla, crime, data_inicio, data_fim)
        except:
            result = []
        finally:
            return jsonify(result)

# Função 16
class estado_topX_vitimas(Resource):
    def get(self,x,crime):
        try:
            result = f.estado_top_x(vitimas,x,crime)
        except:
            result = []
        finally:
            return jsonify(result)

# Atualiza
class Atualiza_bases(Resource):
    def get(self):
        try:
            result = f.atualiza_bases()
        except:
            result = ["ERRO ATUALIZACAO"]
        finally:
            return jsonify(result)