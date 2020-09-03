from flask_restful import Resource
from flask import jsonify

import sys
sys.path.insert(0, '../Funcoes')

# Funcoes
from Funcoes.Kamila import Kamila
f_kamila = Kamila()

class function23 (Resource):
    def get(sigla, municipio):
        try:
            result = f_kamila.municipio_com_estado(sigla, municipio)
        except:
            result = []
        finally:
            return jsonify(result)
class function24 (Resource):
    def get(self, sigla, data_inicio, data_fim):
        try:
            result = f_kamila.datas_municipios(self, sigla, data_inicio, data_fim)
        except:
            result = []
        finally:
            return jsonify(result)