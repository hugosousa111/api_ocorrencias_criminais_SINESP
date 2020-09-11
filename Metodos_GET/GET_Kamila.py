from flask_restful import Resource
from flask import jsonify

import sys
sys.path.insert(0, '../Funcoes')

# Funcoes
from Funcoes.Kamila import Kamila
f_kamila = Kamila()

class Municipio_com_Estado (Resource):
    def get(self, sigla, municipio):
        try:
            result = f_kamila.municipio_com_estado(sigla, municipio)
        except:
            result = []
        finally:
            return jsonify(result)
class Municipio_com_Estado_datas (Resource):
    def get(self, sigla, municipio, data_inicio, data_fim):
        try:
            result = f_kamila.datas_municipios(sigla, municipio, data_inicio, data_fim)
        except:
            result = []
        finally:
            return jsonify(result)