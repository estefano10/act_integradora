import metodos


def opciones():
    op = input("ingrese la opcion que desea realizar: \n"
               "[1] para cargar una nota\n"
               "[2] para mostrar la lista de notas\n"
               "[3] para mostrar la lista de alumnos promocionados\n"
               "[4] para mostrar el porcentaje de reprobados, regulares y promocionados\n"
               "[5] para cargar los 3 mejores promedios\n"
               "[0] para salir del menu\n"
               "opcion : ")

    return op


def menu():
    lista_notas = []
    opcion = opciones()

    while opcion != "0":
        if opcion == "1":
            nota = input("ingrese la nota: ")
            lista_notas.append(nota)

        elif opcion == "2":
            metodos.mostrar_notas(lista_notas)

        elif opcion == "3":
            metodos.promocionados(lista_notas)

        elif opcion == "4":
            metodos.porcentajes(lista_notas)

        elif opcion == "5":
            metodos.mejores_promedios()

        opcion = opciones()




menu()