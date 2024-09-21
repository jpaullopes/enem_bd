
def menu():
    return '''------------------------------------- [ ENEM ] ---------------------------------------
[ 0 ]  - SAIR  
[ 1 ]  - TOP N BRASIL (TODAS AS ÁREAS)
[ 2 ]  - TOP N BRASIL POR ÁREA
[ 3 ]  - TOP N POR ESTADO
[ 4 ]  - TOP N POR ESTADO E REDE (PÚBLICA OU PRIVADA)
[ 5 ]  - MEDIA NACIONAL POR ÁREA
[ 6 ]  - MELHOR ESCOLA POR ÁREA E ESTADO OU BR
[ 7 ]  - LISTAS ESCOLAS POR ESTADO ORDENADA POR RENDA
[ 8 ]  - BUSCA ESCOLA ESPECÍFICA POR PARTE DO NOME
[ 9 ]  - RANKING ENEM POR ESTADO
[ 10 ] - RANKING ENEM POR REGIÃO DO PAÍS
--------------------------------------------------------------------------------------'''

def menu_filter():
    return '''---------------------------------- [ FILTRAR ] ---------------------------------------
[ 1 ]  - POR ESTADO
[ 2 ]  - PAÍS
--------------------------------------------------------------------------------------'''

def menu_icome():
    return '''--------------------------------------- [ RENDA ] ------------------------------------
[ 1 ]  - CRESCENTE
[ 2 ]  - DESCRESCENTE
--------------------------------------------------------------------------------------'''

def menu_filter_region():
    return '''
------------------------------------- [ REGIÃO ] -------------------------------------
[ 1 ]  - FILTRAR POR REGIÃO
[ 2 ]  - EXIBIR DE TODAS AS REGIÕES
--------------------------------------------------------------------------------------'''

def rede_menu():
    return '''
-------------------------------------[ REDE ]---------------------------------------
[  Publica  ] | [  Privada  ] | [  Federal  ] | [  Estadual  ] | [ Municipal ]
------------------------------------------------------------------------------------'''

def area_menu():
    return '''-------------------------------------[ ÁREAS ]----------------------------------------
[ MATEMATICA ] | [ LINGUAGENS ] | [ CIENCIAS DA NATUREZA ] | [ HUMANAS ] | [ REDACAO ]
--------------------------------------------------------------------------------------'''

def states_menu():
    return '''------------------------------------[ ESTADOS ]---------------------------------------
[ AC ] | [ AL ] | [ AM ] | [ AP ] | [ BA ] | [ CE ] | [ DF ] | [ ES ] | [ GO ] | [ MA ] 
[ MG ] | [ MS ] | [ MT ] | [ PA ] | [ PB ] | [ PE ] | [ PI ] | [ PR ] | [ RJ ] | [ RN ]
[ RO ] | [ RR ] | [ RS ] | [ SC ] | [ SE ] | [ SP ] | [ TO ]
--------------------------------------------------------------------------------------'''

def exibition_school(school_data):
    return f"""-------------------------------------[ ESCOLA ]---------------------------------------
NOME                   | {school_data["NOME"]}
MUNICIPIO              | {school_data["MUNICIPIO"]}
UF                     | {school_data["UF"]}
REDE                   | {school_data["REDE"]}
PERMANENCIA            | {school_data["PERMANENCIA"]}
NIVEL SOCIO ECONÔMICO  | {school_data["NIVEL SOCIO ECONOMICO"]}
MÉDIA OBJETIVAS        | {school_data["MEDIA OBJETIVAS"]}
LINGUAGENS             | {school_data["LINGUAGENS"]}
MATEMÁTICA             | {school_data["MATEMATICA"]}
CIÊNCIAS DA NATUREZA   | {school_data["CIENCIAS DA NATUREZA"]}
HUMANAS                | {school_data["HUMANAS"]}
REDAÇAO                | {school_data["REDACAO"]}
--------------------------------------------------------------------------------------"""

def region_menu():
    return '''-------------------------------------[ REGIAO ]---------------------------------------
[  NORTE  ] | [  NORDESTE  ] | [  SUDESTE  ] | [  SUL  ] | [  CENTRO-OESTE  ]
------------------------------------------------------------------------------------'''