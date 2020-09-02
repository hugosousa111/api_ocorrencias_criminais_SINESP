from flask_restful import Resource
from flask import jsonify

import sys
sys.path.insert(0, '../Funcoes')

# Funcoes
from Funcoes.Alice import Alice
f_alice = Alice()

class metodo_get_alice(Resource):
    def get(self):
        try:
            result = f_alice.funcao_alice()
        except:
            result = []
        finally:
            return jsonify(result)class

        
class municipio_estado(Resource):
    def get(self, tipo, sigla):
        try:
            result = f_alice.municipio_estado(tipo, sigla)
        except:
            result = []
        finally:
            return jsonify(result) 
        
        
class municipio_estado_datas(Resource):
    def get(self, tipo, sigla, data_inicio, data_fim):
        try:
            result = f_alice.municipio_estado_datas(tipo, sigla, data_inicio, data_fim)
        except:
            result = []
        finally:
            return jsonify(result)         
