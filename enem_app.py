import utils as ut
import enem_utils as eu
import enem_menus as menus

def main():
    enem_datas = eu.read_file("enem2014_dados.csv")#leitura dos dados do enem
    print(menus.menu())
    option = ut.get_number_between("Digite a opção desejada: ",0,10)

    while option != 0:
        if option == 1:
            n_values = ut.get_positive_number("Digite o número de valores desejados: ")
            print(eu.position_exibition(n_values, enem_datas))
        elif option == 2:
            #lembrar de ordenar pela area
            print(menus.area_menu())
            criterio = eu.get_area("Digite a área desejada: ")
            top_area = ut.my_filter(lambda a: a[criterio], enem_datas)
            n_values = ut.get_number_between("Digite o número de valores desejados: ", 0, len(top_area))
            top_area = ut.ordenar(top_area[:n_values],lambda a: a[criterio],reverse=False)#bubble não é nada eficiente
            print(eu.position_exibition(n_values,top_area))
        elif option == 3:
            print(menus.states_menu())
            state = eu.get_state("Digite o estado desejado: ")
            top_states = ut.my_filter(lambda a: a['UF'] == state, enem_datas)
            n_values = ut.get_number_between("Digite o número de valores desejados: ", 0, len(top_states))
            print(eu.position_exibition(n_values,top_states))
        elif option == 4:
            print(menus.states_menu())
            state = eu.get_state("Digite o estado desejado: ")
            print(menus.rede_menu())
            type_rede = eu.get_rede("Digite o tipo rede desejada: ")
            states_school = ut.my_filter(lambda a: a['UF'] == state, enem_datas)
            type_school = ut.my_filter(lambda a: a['REDE'] in type_rede, states_school)
            n_values = ut.get_number_between("Digite o número de valores desejados: ", 0, len(type_school))
            print(eu.position_exibition(n_values, type_school))
        elif option == 5:
            print(eu.avarage_areas(enem_datas))
        elif option == 6:
            print(menus.area_menu())
            area = eu.get_area("Digite a área desejada: ")
            print(menus.menu_filter())
            choice = ut.get_number_between("Digite a opção desejada: ", 1, 2)
            if choice == 1:
                print(menus.states_menu())
                state = eu.get_state("Digite o estado desejado: ")
                schools_found = ut.my_filter(lambda a: a['UF'] == state, enem_datas)
            else:
                schools_found = enem_datas
            top_schools = ut.my_reduce(lambda a,b:a if a[area] > b[area] else b, schools_found,schools_found[0])
            print(menus.exibition_school(top_schools))
        elif option == 7:
            print(menus.states_menu())
            state = eu.get_state("Digite o estado desejado: ")
            schools_found = ut.my_filter(lambda a: a['UF'] == state, enem_datas)
            print(menus.menu_icome())
            choice = ut.get_number_between("Digite a opção desejada: ", 1, 2)
            sorted_schools = ut.ordenar(schools_found, lambda a: eu.income_transformator(a['NIVEL SOCIO ECONOMICO']),True if choice == 2 else False)
            print(eu.position_exibition(len(sorted_schools),sorted_schools))
        elif option == 8:
            #busca especifica por nome
            name = ut.upper_case(input("Digite o nome da escola: "))
            schools_found = ut.my_filter(lambda a: name in a['NOME'],enem_datas)
            for i in schools_found:
                print(menus.exibition_school(i))
        elif option == 9:
            #rank enem por estado
            print(menus.states_menu())
            state = eu.get_state("Digite o estado desejado: ")
            schools_found = ut.my_filter(lambda a: a['UF'] == state, enem_datas)
            print(eu.position_exibition(len(schools_found),schools_found))
        elif option == 10:
            print(menus.menu_filter_region())
            choice = ut.get_number_between("Informe a opção desejada: ", 1, 2)
            if choice == 1:
                print(menus.region_menu())
                region = eu.get_region("Digite a região desejada: ")
                states = eu.region_states(region)
                schools_found = ut.my_filter(lambda a: a['UF'] in states, enem_datas)
                print(eu.position_exibition(len(schools_found), schools_found))
            else:
                all_regions = ['NORTE', 'NORDESTE', 'SUDESTE', 'SUL', 'CENTRO-OESTE']
                for i in all_regions:
                    print(f'[{i}]')
                    states = eu.region_states(i)
                    schools_found = ut.my_filter(lambda a: a['UF'] in states, enem_datas)
                    print(eu.position_exibition(len(schools_found), schools_found))

        print(menus.menu())
        option = ut.get_number_between("Digite a opção desejada: ", 0, 10)


main()