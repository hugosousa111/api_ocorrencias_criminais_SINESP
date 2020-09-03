from flask import Flask
from flask_restful import Api

# A sessão a seguir esta comentada para rodar mais rápido(para os Testes)
'''
from download_df import download
download() #download das bases
'''

app = Flask(__name__)
api = Api(app)

# Metodos GET da API
from Metodos_GET.GET_Alice import *
from Metodos_GET.GET_Angela import *
from Metodos_GET.GET_Fabricio import *
from Metodos_GET.GET_Hugo import *
from Metodos_GET.GET_Kamila import *
from Metodos_GET.GET_Renato import *
from Metodos_GET.GET_Thiago import *

### Rotas Hugo
# Base Estados por Ocorrencias
api.add_resource(Est_ocorrencias, '/estados_ocorrencias')
api.add_resource(Est_ocorrencias_estado, '/estados_ocorrencias/estado/<sigla>')
api.add_resource(Est_ocorrencias_estado_datas, '/estados_ocorrencias/estado/<sigla>/<data_inicio>/<data_fim>')

api.add_resource(Est_ocorrencias_crime, '/estados_ocorrencias/crime/<crime>')
api.add_resource(Est_ocorrencias_crime_datas, '/estados_ocorrencias/crime/<crime>/<data_inicio>/<data_fim>')

api.add_resource(Est_ocorrencias_estado_crime, '/estados_ocorrencias/estado/crime/<sigla>/<crime>')
api.add_resource(Est_ocorrencias_estado_crime_datas, '/estados_ocorrencias/estado/crime/<sigla>/<crime>/<data_inicio>/<data_fim>')

# Base Estados por Vitimas
api.add_resource(Est_vitimas, '/estados_vitimas') 
api.add_resource(Est_vitimas_estado, '/estados_vitimas/estado/<sigla>')
api.add_resource(Est_vitimas_estado_datas, '/estados_vitimas/estado/<sigla>/<data_inicio>/<data_fim>')

api.add_resource(Est_vitimas_crime, '/estados_vitimas/crime/<crime>')
api.add_resource(Est_vitimas_crime_datas, '/estados_vitimas/crime/<crime>/<data_inicio>/<data_fim>')

api.add_resource(Est_vitimas_estado_crime, '/estados_vitimas/estado/crime/<sigla>/<crime>')
api.add_resource(Est_vitimas_estado_crime_datas, '/estados_vitimas/estado/crime/<sigla>/<crime>/<data_inicio>/<data_fim>')

api.add_resource(Municipios, '/municipios') 

api.add_resource(Municipios_total, '/municipios/total')
api.add_resource(Municipios_total_datas, '/municipios/total/<data_inicio>/<data_fim>')

api.add_resource(Municipios_total_estado, '/municipios/total/estado/<sigla>')
api.add_resource(Municipios_total_estado_datas, '/municipios/total/estado/<sigla>/<data_inicio>/<data_fim>')

### Rotas Alice
# Base dividida por municipios
api.add_resource(Municipios_estado, '/municipios/estado/<sigla>')
api.add_resource(Municipios_estado_datas, '/municipios/estado/<sigla>/<data_inicio>/<data_fim>')

### Rotas Angela
api.add_resource(metodo_get_angela, '/angela')
api.add_resource(Municipios_topX_vitimas, '/municipios/top/<x>')
api.add_resource(Municipios_topX_vitimas_periodo, '/municipios/top/<x>/<data_inicio>/<data_fim>')

### Rotas Fabricio
api.add_resource(metodo_get_fabricio, '/fabricio') 

### Rotas Kamila
api.add_resource(function23, '/municipios/estado/municipio/<sigla>/<municipio>') 
api.add_resource(function24, '/municipios/estado/municipio/<sigla>/<municipio>/<data_inicio>/<data_fim>')

### Rotas Renato
api.add_resource(metodo_get_renato, '/renato') 

### Rotas Thiago
api.add_resource(metodo_get_thiago, '/thiago') 

if __name__ == '__main__':
    app.run(host="localhost", port=3000)
