import os

# NO PUEDEN INGRESARSE EXPONENTES MAYORES A 9999
# https://es.wikipedia.org/wiki/Funci%C3%B3n_algebraica
# EVALUAR FUNCION EN UN PUNTO

#################################-- VARIABLES GLOBALES --#################################

value = False
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#################################-- FUNCIONES --#################################


def ingresarFuncion():
    global value, funcion
    if value:
        return funcion
    else:
        value = True
        while True:
            funcion = str(input("Ingrese una función: f(x) = "))
            try:
                funcion = funcion.lower()
                int(funcion.index("x"))
                funcion = funcion.replace(" ", "")
                break
            except ValueError:
                print("Por favor, ingrese correctamente la incógnita")
        return funcion


def exponente():
    list_exponente = []
    funcion = ingresarFuncion()
    
    inicio = int(funcion.find("x**"))
    fraccion()

    while inicio != -1:
        num = 2
        for i in funcion[inicio+3: ]:
            if i not in str(numeros):
                break
            num += 1
        if num == 3:
            num = 4
        exponente = int(funcion[inicio+3: inicio+num])
        list_exponente.append(exponente)
        funcion = funcion[inicio+num: ]
        inicio = int(funcion.find("x**"))
    try: 
        exp_alto = max(list_exponente)
    except ValueError:
        exp_alto = 0
    
    return exp_alto


def raiz():
    funcion = ingresarFuncion()
    find_raiz = int(funcion.find("raiz("))
    
    if find_raiz != -1:
        for i in funcion[find_raiz+5: ]:
            if i != ")":
                if i == "x":
                    return True
            else:
                break
    

def fraccion():
    funcion = ingresarFuncion()
    find_fraccion = int(funcion.find("/("))

    if find_fraccion != -1:
        for i in funcion[find_fraccion+2: ]:
            if i != ")":
                if i == "x":
                    return True
            else:
                break
    else:
        find_fraccion = int(funcion.find("/"))
        if find_fraccion != -1:
            for i in funcion[find_fraccion+1: ]:
                if i not in str(numeros):
                    if i == "x":
                        return True
                else:
                    break
                

def error(valor):
    while True:
        try:
            opcion = int(input(valor))
            return opcion
        except ValueError:
            print("Ingrese la opción correctamente")
            input("Presione ENTER para continuar...")
            


#################################-- MAIN --#################################


while True:
    os.system("cls")

    cadena = "¡Bienvenido a Pipo's Functions!"

    print(cadena.center(70, " "))

    print("""
ANTES DE USAR EL PROGRAMA, ES NECESARIO TENER EN CUENTA QUE...
a) UTILIZAREMOS X COMO INCÓGNITA
b) Una potencia se indica con "**"
c) Una raíz se indica dentro de "raiz()"

-------------------------------------------------------------------------

Menú de opciones
    1. Conocer tipos de funciones
    2. Analizar qué tipo de función es
    3. Salir

""")
    opcion = error(">>> ")
    if opcion == 1:
        print("Tipos de funciones")
    elif opcion == 2:
        if raiz():
            print("Es una función irracional")
        else:
            if fraccion():
                print("Es una función racional")
            else:
                print("Es una función polinómica")
                exp_alto = exponente()
                if exp_alto == 0:
                    print("Es una función lineal")
                elif exp_alto >= 2:
                    if exp_alto == 2:
                        print("Es una función cuadrática")
                    elif exp_alto == 3:
                        print("Es una función cúbica")
                    elif exp_alto >= 4:
                        print("Es una función de " + str(exp_alto) + " grado")

        value = False
    elif opcion == 3:
        break
    else:
        print("Ingrese alguna de las opciones especificadas.")

    input("Presione ENTER para continuar...")
    