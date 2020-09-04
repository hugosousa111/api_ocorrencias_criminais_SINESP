from flask_restful import Resource
from flask import jsonify

import sys
sys.path.insert(0, '../Funcoes')

# Funcoes
from Funcoes.Renato import Renato
f_renato = Renato()

class Municipios_regiao(Resource):
    def get(self, regiao):
        try:
            result = f_renato.municipios_regiao(regiao)
        except:
            result = []
        finally:
            return jsonify(result)

class Municipios_regiao_datas(Resource):
    def get(self, regiao, data_inicio, data_fim):
        try:
            result = f_renato.municipios_regiao_datas(regiao, data_inicio, data_fim)
        except:
            result = []
        finally:
            return jsonify(result)
