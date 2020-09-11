# Arquivos e Pastas do Projeto: 

/info.txt   
- Contém informações sobre instalação de bibliotecas e outros

/server.py  
- Arquivo principal, que une tudo e roda o servidor flask
- Basta executar apenas esse arquivo

/download_df.py 
- Arquivo que faz o download das bases direto do site
- Não é necessário rodar esse arquivo, pois as bases já foram baixadas

/func_auxiliares.py 
- Arquivo com algumas funções auxiliares
- Conversão de siglas, abreviaturas, trabalhar com as datas e outros

/Insomnia_requisicoes_GET.json  
- São as requisições GET para JSON
- Para importar no Insomnia: 
    - Application/Preferences/Data/Import Data/From file

/Bases/ 
- Nessa pasta estão as duas bases de dados(formato xlsx)
- Cada arquivo, é separado por páginas:
    - Base por estados: Ocorrências e Vítimas
    - Base por Municípios: Siglas dos Estados

/Metodos_GET/   
- Nesse arquivo, deve conter apenas as classes e os métodos GET
- Cada método GET, chama uma função da pasta /Funcoes/

/Funcoes/   
- Nesse arquivo deve ser adicionado a função que o GET chama
- É aqui que são realizadas as manipulações de dados das bases para cada requisição à API


# Padronização da sintaxe das rotas:

1. Estados:
    
- Os estados devem ser passados com sua respectiva sigla e em maiúsculo:
    - "/CE/"


2. Datas:
    
- Datas devem ser passadas no formato "mês abreviado" + "-" + "ano":
    - "fev-2019"
    

3. Ordem das Datas:
    
- Sempre que usar datas, passar primeiro a data inicial e depois a data final, incluindo na busca os meses de início e fim:
    - "/jan-2017/ago-2019/"


4. Nomes de Crimes e Cidades:

- Nas rotas quando o crime/cidade for formado por duas ou mais palavras, usar "_" para separá-las:
    - "/Cruzeiro_do_Sul/"
    - "/Roubo_seguido_de_morte_(latrocínio)/"
    

5. Datas passadas na ordem invertidas, o retorno é um []:
    - "/jan-2020/fev-2019/"

