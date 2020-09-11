from flask_restful import Resource
from flask import jsonify

import sys
sys.path.insert(0, '../Funcoes')

# Funcoes
from Funcoes.Thiago import Thiago
f_thiago = Thiago()

class estado_topX_ocorrencias(Resource):
    def get(self,x,crime):
        try:
            result = f_thiago.estado_top_ocorrencias_x(x,crime)
        except:
            result = []
        finally:
            return jsonify(result)

class estado_topX_vitimas(Resource):
    def get(self,x,crime):
        try:
            result = f_thiago.estado_top_vitimas_x(x,crime)
        except:
            result = []
        finally:
            return jsonify(result)
