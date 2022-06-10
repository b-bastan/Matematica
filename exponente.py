import os, re

# ACLARAR QUE SOLO EXISTE X COMO INCÓGNITA
# NO PUEDEN INGRESARSE EXPONENTES MAYORES A 9999
# Potencia = **; raiz = //
# f(x) = x**5 + (2**2)**3
# f(x) = x**2569 + **8 - **9999
# f(x) = 5**6 x  * 9


while True:
    os.system("cls")
    numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    list_exponente = []

    while True:
        funcion = str(input("Ingrese una función: "))
        try:
            int(funcion.index("x"))
            break
        except ValueError:
            print("Por favor, ingrese correctamente la incógnita")

    funcion = funcion.replace(" ", "")
    inicio = int(funcion.find("x**"))

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
    
    print("El exponente más alto es: ", exp_alto)

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

    input("Presione ENTER para continuar...")
    