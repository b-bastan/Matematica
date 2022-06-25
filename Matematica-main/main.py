import os

# NO PUEDEN INGRESARSE EXPONENTES MAYORES A 9999
# Potencia = **; raiz = //
# SOLUCIONAR QUE NO PUEDAN INGRESAR UNA OPCION EN BLANCO
# VER CÓMO COLOCAR EL ÍNDICE DE LA RAIZ O COMO SE LLAME (AUNQUE NO AFECTE EN EL PROGRAMA)
# VER CÓMO HACER CUANDO EN EL DIVISOR EL EXPONENTE ES UNA X, TIPO 5/6**X
# ¿UNA FUNCIÓN PUEDE SER RACIONAL E IRRACIONAL A LA VEZ?

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
                int(funcion.index("x"))
                funcion = funcion.replace(" ", "")
                break
            except ValueError:
                print("Por favor, ingrese correctamente la incógnita")
        return funcion


def exponente():
    global value
    list_exponente = []
    funcion = ingresarFuncion()
    inicio = int(funcion.find("x**"))
    raiz()
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
    
    value = False
    return exp_alto


def raiz():
    funcion = ingresarFuncion()
    find_raiz = int(funcion.find("raiz("))
    
    if find_raiz != -1:
        for i in funcion[find_raiz+5: ]:
            if i != ")":
                if i == "x":
                    return print("Es una funcion irracional")


def fraccion():
    funcion = ingresarFuncion()
    find_fraccion = int(funcion.find("/("))

    if find_fraccion != -1:
        for i in funcion[find_fraccion+2: ]:
            if i != ")":
                if i == "x":
                    return print("Es una función racional")
    else:
        find_fraccion = int(funcion.find("/"))
        if find_fraccion != -1:
            for i in funcion[find_fraccion+1: ]:
                if i not in str(numeros):
                    if i == "x":
                        return print("Es una función racional")
                    else:
                        break



#################################-- MAIN --#################################


while True:
    os.system("cls")

    cadena = "¡Bienvenido a Pipo's Functions!"

    print(cadena.center(70, " "))

    opcion = int(input("""
ANTES DE USAR EL PROGRAMA, ES NECESARIO TENER EN CUENTA QUE...
a) UTILIZAREMOS X COMO INCÓGNITA
b) Una potencia se indica con "**"
c) Una raíz se indica dentro de "raiz()"

-------------------------------------------------------------------------

Menú de opciones
    1. Conocer tipos de funciones
    2. Calcular qué tipo de función es
    3. Salir
    
>>> """))

    if opcion == 1:
        print("Tipos de funciones")
    elif opcion == 2:
        exp_alto = exponente()
        if exp_alto == 0:
            print("Es un monomio")
            print("Es una función lineal")
        elif exp_alto >= 2:
            print("Es un polinomio")
            if exp_alto == 2:
                print("Es una función cuadrática")
            elif exp_alto == 3:
                print("Es una función cúbica")
            elif exp_alto >= 4:
                print("Es una función de " + str(exp_alto) + " grado")
    elif opcion == 3:
        break
    else:
        print("Por favor, ingrese alguna de las opciones especificadas.")

    input("Presione ENTER para continuar...")
    