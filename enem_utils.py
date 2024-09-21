import utils
import enem_menus as menus

def read_file(file_name):
    values = utils.open_file(file_name)
    enem_dates = []
    for i in values:
        line = {}
        date = i.split(";")
        line["NOME"] = date[1]
        line["MUNICIPIO"] = date[2]
        line["UF"] = date[3]
        line["REDE"] = date[4]
        line["PERMANENCIA"] = date[5]
        line["NIVEL SOCIO ECONOMICO"] = date[6]
        line["MEDIA OBJETIVAS"] = float_conversion(date[7])
        line["LINGUAGENS"] = float_conversion(date[8])
        line["MATEMATICA"] = float_conversion(date[9]) 
        line["CIENCIAS DA NATUREZA"] = float_conversion(date[10])
        line["HUMANAS"] = float_conversion(date[11])
        line["REDACAO"] = float_conversion(date[12])

        enem_dates.append(line)
    return enem_dates

def float_conversion(string): #função que converte número em formato 1,3 para formato float
    float_format = utils.my_map(lambda a: a if a != ',' else '.',string)
    float_format = utils.my_reduce(lambda a,b : a+b,float_format,'')
    return float(float_format)

def filter_by_state(datas, state, criterion = 'MEDIA OBJETIVAS'):
    datas_states = utils.my_filter(lambda a: a['UF'] == state, datas)
    top_school = utils.my_reduce(lambda a, b:a if a[criterion] > b[criterion] else b, datas_states, datas_states[0])   
    return top_school

def get_area(text):
    all_areas = ['MATEMATICA', 'LINGUAGENS', 'CIENCIAS DA NATUREZA','HUMANAS','REDACAO']
    area = utils.upper_case(input(text))
    while area not in all_areas:
        print('Área inválida')
        area = utils.upper_case(input(text))
    return area

def get_state(text):
    brazilian_states = ["AC", "AL", "AM", "AP", "BA", "CE", "DF", "ES", "GO", "MA",
    "MG", "MS", "MT", "PA", "PB", "PE", "PI", "PR", "RJ", "RN",
    "RO", "RR", "RS", "SC", "SE", "SP", "TO"]
    state = utils.upper_case(input(text))
    while state not in brazilian_states:
        print('Sigla de estado inválida')
        state = utils.upper_case(input(text))
    return state

def get_rede(text):
    all_rede = ['Publica','Privada', 'Federal', 'Estadual', 'Municipal']
    rede = utils.my_capitalize(input(text))
    while rede not in all_rede:
        print('Rede inválida')
        rede = utils.my_capitalize(input(text))
    if rede == 'Publica':
        return ['Federal', 'Estadual', 'Municipal']
    return rede

def avarage(datas, criterion):
    sum = utils.my_reduce(lambda a,b:a+b[criterion],datas,datas[0][criterion])
    return sum/len(datas)

def avarage_areas(datas):
    return f"""[MATEMATICA]           | MÉDIA: [{avarage(datas,'MATEMATICA'):.2f}]
[LINGUAGENS]           | MÉDIA: [{avarage(datas,'LINGUAGENS'):.2f}]
[CIENCIAS DA NATUREZA] | MÉDIA: [{avarage(datas,'CIENCIAS DA NATUREZA'):.2f}]
[HUMANAS]              | MÉDIA: [{avarage(datas,'HUMANAS'):.2f}]
[REDACAO]              | MÉDIA: [{avarage(datas,'REDACAO'):.2f}]"""

def get_region(text):
    all_regions = ['NORTE', 'NORDESTE', 'SUDESTE', 'SUL', 'CENTRO-OESTE']
    region = utils.upper_case(input(text))
    while region not in all_regions:
        print('Região inválida')
        region = utils.upper_case(input(text))
    return region

def region_states(region):
    #retornar os estados correspondentes pra cada região
    if region == 'NORDESTE':
        return ['PI', 'MA', 'PE','BA','RN','CE','SE','PB','AL']
    elif region == 'SUDESTE':
        return ['MG', 'SP', 'RJ','ES']
    elif region == 'SUL':
        return ['PR', 'SC', 'RS']
    elif region == 'CENTRO-OESTE':
        return ['MT', 'GO', 'DF']
    return ['AC', 'AP', 'AM','RO','RR','PA','TO']

def income_transformator(type):
    incomes_type = ['Muito Alto', 'Alto', 'Mï¿½dio Alto', 'Mï¿½dio', 'Mï¿½dio Baixo', 'Baixo', 'Muito Baixo','Sem informaï¿½ï¿½o']
    position = utils.linear_search(type, incomes_type)
    return len(incomes_type) - position

def position_exibition(size,values):
    exibition = ''
    for i in range(size):
        exibition += f'\n[ POSIÇÃO ] -> [{i + 1}°]\n'
        exibition += menus.exibition_school(values[i])
    return exibition