from flask_restful import Resource
from flask import jsonify

import sys
sys.path.insert(0, '../Funcoes')

# Funcoes
from Funcoes.Fabricio import Fabricio
f_fabricio = Fabricio()

class metodo_get_fabricio(Resource):
    def get(self):
        try:
            result = f_fabricio.funcao_fabricio()
        except:
            result = []
        finally:
            return jsonify(result)
class Municipios_top_estado(Resource):
    def get(self,X,sigla):
        try:
            result = f_fabricio.Municipio_top_estado(X,sigla)
        except:
            result = []
        finally:
            return jsonify(result)
class Municipios_top_estado_por_periodo(Resource):
    def get(self,X,sigla,data_inicio,data_fim):
        try:
            result = f_fabricio.Municipio_top_estado_periodo(X,sigla,data_inicio, data_fim)
        except:
            result = []
        finally:
            return jsonify(result)