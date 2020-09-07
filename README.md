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

<!---# O que alterar?

- No arquivo server.py, na sessão com seu nome, inserir as rotas das suas funções

- Na pasta /Metodos_GET/, no arquivo com seu nome, inserir os métodos GET

- Na pasta /Funcoes/, no arquivo com seu nome, inserir as funções que trabalham com as bases de dados

- Caso precise de funções auxiliares, adicione no arquivo func_auxiliares.py, na sessão com seu nome

- Caso precise, crie outros arquivos

- Criei uma rota pra cada um, que é o seu nome, só pra testar-->

# Padronização da sintaxe das rotas:

1. Estados: <br/>
    Os estados devem ser passados com sua respectiva sigla e em maiúsculo: </br>
    "/CE/" <br/>


2. Datas: <br/>
    Datas devem ser passadas no formato "mês abreviado" + "-" + "ano": </br>
    "fev-2019" <br/>
    

3. Ordem das Datas: <br/>
    Sempre que usar datas, pasar primeiro a data inicial e depois a data final, incluindo na busca os meses de início e fim: <br/>
    "/jan-2017/ago-2019/" <br/>


4. Nomes de Crimes e Cidades: <br/>
    Nas rotas quando o crime/cidade for formado por duas ou mais palavras, usar "_" para separá-las <br/>
    "/Cruzeiro_do_Sul/" <br/>
    "/Roubo_seguido_de_morte_(latrocínio)/" </br>
    

5. Datas passadas na ordem invertidas, o retorno é um []: <br/>
    "/jan-2020/fev-2019/"<br/>
