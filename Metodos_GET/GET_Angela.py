from flask_restful import Resource
from flask import jsonify

import sys
sys.path.insert(0, '../Funcoes')

# Funcoes
from Funcoes.Angela import Angela
f_angela = Angela()


class Municipios_topX_vitimas(Resource):
    def get(self, x):
        try:
            result = f_angela.municipios_top_x(x)
        except:
            result = []
        finally:
            return jsonify(result)


class Municipios_topX_vitimas_periodo(Resource):
    def get(self, x, data_inicio, data_fim):
        try:
            result = f_angela.municipios_top_x_periodo(x, data_inicio, data_fim)
        except:
            result = []
        finally:
            return jsonify(result)

