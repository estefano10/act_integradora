
def mostrar_notas(lista):
    for nota in lista:
        print(nota)



def promocionados(lista):
    contador = 0
    for item in lista:
        if item >= "7":
            contador = contador + 1
            print(f"la calificacion de promocion N {contador} es: {item}")



def porcentajes(lista):

    contador_desaprobados = 0
    contador_regulares = 0
    contador_promocionados = 0

    for item in lista:
        if item < "4":
            contador_desaprobados = contador_desaprobados +1


        elif item >= "4" and item < "7":
            contador_regulares = contador_regulares + 1


        elif item > "7":
            contador_promocionados = contador_promocionados + 1
    print(f"el porcentaje de desaprobados es: {contador_desaprobados / len(lista)}")
    print(f"el porcentaje de alumnos regulares es: {contador_regulares / len(lista)}")
    print(f"el porcentaje de promocionados es: {contador_promocionados / len(lista)}")



def mejores_promedios():
    nombres = []
    print('ingresar el nombre de los 3 alumnos: ')
    for i in range(1, 4):
        nombre = str(input(f'ingrese el nombre del alumno {i}: '))
        nota = str(input(f'ingrese la nota del alumno {i}: '))
        nombres.append(nombre)


    print(nombres)