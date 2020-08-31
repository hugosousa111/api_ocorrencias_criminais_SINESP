from flask_restful import Resource
from flask import jsonify

import sys
sys.path.insert(0, '../Funcoes')

# Funcoes
from Funcoes.Angela import Angela
f_angela = Angela()

class metodo_get_angela(Resource):
    def get(self):
        try:
            result = f_angela.funcao_angela()
        except:
            result = []
        finally:
            return jsonify(result)

class Municipios_topX_vitimas(Resource):
    def get(self, x):
        try:
            result = f_angela.municipios_top_x(x)
        except:
            result = []
        finally:
            return jsonify(result)
