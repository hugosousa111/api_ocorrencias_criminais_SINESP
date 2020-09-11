from flask_restful import Resource
from flask import jsonify

import sys
sys.path.insert(0, '../Funcoes')

# Funcoes
from Funcoes.Alice import Alice
f_alice = Alice()
        
class Municipios_estado(Resource):
    def get(self, sigla):
        try:
            result = f_alice.municipios_estado(sigla)
        except:
            result = []
        finally:
            return jsonify(result) 
        
        
class Municipios_estado_datas(Resource):
    def get(self, sigla, data_inicio, data_fim):
        try:
            result = f_alice.municipios_estado_datas(sigla, data_inicio, data_fim)
        except:
            result = []
        finally:
            return jsonify(result)         
