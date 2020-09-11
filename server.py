from flask import Flask
from flask_restful import Api

'''
#Ambiente de Development
class DevelopmentConfig(object):
    ENV = 'development'
    DEBUG = True #live reload

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
api = Api(app)

# Ou roda assim:
#env FLASK_ENV=development FLASK_APP=server.py flask run
'''

app = Flask(__name__)
api = Api(app)

# Metodos GET da API
from Metodos_GET.GET_Estados import *
from Metodos_GET.GET_Municipios import *

# Base Estados por Ocorrencias
# Função 01
api.add_resource(Est_ocorrencias, '/estados_ocorrencias')
# Função 02
api.add_resource(Est_ocorrencias_estado, '/estados_ocorrencias/estado/<sigla>')
# Função 03
api.add_resource(Est_ocorrencias_estado_datas, '/estados_ocorrencias/estado/<sigla>/<data_inicio>/<data_fim>')
# Função 04
api.add_resource(Est_ocorrencias_crime, '/estados_ocorrencias/crime/<crime>')
# Função 05
api.add_resource(Est_ocorrencias_crime_datas, '/estados_ocorrencias/crime/<crime>/<data_inicio>/<data_fim>')
# Função 06
api.add_resource(Est_ocorrencias_estado_crime, '/estados_ocorrencias/estado/crime/<sigla>/<crime>')
# Função 07
api.add_resource(Est_ocorrencias_estado_crime_datas, '/estados_ocorrencias/estado/crime/<sigla>/<crime>/<data_inicio>/<data_fim>')
# Função 08
api.add_resource(estado_topX_ocorrencias, '/estados_ocorrencias/top/crime/<x>/<crime>') 

# Base Estados por Vitimas
# Função 09
api.add_resource(Est_vitimas, '/estados_vitimas') 
# Função 10
api.add_resource(Est_vitimas_estado, '/estados_vitimas/estado/<sigla>')
# Função 11
api.add_resource(Est_vitimas_estado_datas, '/estados_vitimas/estado/<sigla>/<data_inicio>/<data_fim>')
# Função 12
api.add_resource(Est_vitimas_crime, '/estados_vitimas/crime/<crime>')
# Função 13
api.add_resource(Est_vitimas_crime_datas, '/estados_vitimas/crime/<crime>/<data_inicio>/<data_fim>')
# Função 14
api.add_resource(Est_vitimas_estado_crime, '/estados_vitimas/estado/crime/<sigla>/<crime>')
# Função 15
api.add_resource(Est_vitimas_estado_crime_datas, '/estados_vitimas/estado/crime/<sigla>/<crime>/<data_inicio>/<data_fim>')
# Função 16
api.add_resource(estado_topX_vitimas, '/estados_vitimas/top/crime/<x>/<crime>')

# Base dividida por municipios
# Função 17
api.add_resource(Municipios, '/municipios') 
# Função 18
api.add_resource(Municipios_datas, '/municipios/<data_inicio>/<data_fim>') 
# Função 19
api.add_resource(Municipios_regiao, '/municipios/regiao/<regiao>')
# Função 20
api.add_resource(Municipios_regiao_datas, '/municipios/regiao/<regiao>/<data_inicio>/<data_fim>')
# Função 21
api.add_resource(Municipios_estado, '/municipios/estado/<sigla>')
# Função 22
api.add_resource(Municipios_estado_datas, '/municipios/estado/<sigla>/<data_inicio>/<data_fim>')
# Função 23
api.add_resource(Municipio_com_Estado, '/municipios/estado/municipio/<sigla>/<municipio>') 
# Função 24
api.add_resource(Municipio_com_Estado_datas, '/municipios/estado/municipio/<sigla>/<municipio>/<data_inicio>/<data_fim>')
# Função 25
api.add_resource(Municipios_topX_vitimas, '/municipios/top/<x>')
# Função 26
api.add_resource(Municipios_topX_vitimas_periodo, '/municipios/top/<x>/<data_inicio>/<data_fim>')
# Função 27
api.add_resource(Municipios_top_estado, '/municipios/top/estado/<X>/<sigla>')
# Função 28
api.add_resource(Municipios_top_estado_por_periodo, '/municipios/top/estado/<X>/<sigla>/<data_inicio>/<data_fim>')
# Função 29
api.add_resource(Municipios_total, '/municipios/total')
# Função 30
api.add_resource(Municipios_total_datas, '/municipios/total/<data_inicio>/<data_fim>')
# Função 31
api.add_resource(Municipios_total_estado, '/municipios/total/estado/<sigla>')
# Função 32
api.add_resource(Municipios_total_estado_datas, '/municipios/total/estado/<sigla>/<data_inicio>/<data_fim>')

# Atualizar bases
api.add_resource(Atualiza_bases, '/atualiza')

if __name__ == '__main__':
    #app.run(host="0.0.0.0", port=80) # sudo python3 server.py
    app.run(host="localhost", port=3000)
