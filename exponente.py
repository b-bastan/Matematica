import math, re

# ACLARAR QUE SOLO EXISTE X COMO INCÓGNITA
# NO PUEDEN INGRESARSE EXPONENTES MAYORES A 9999
# Potencia = **; raiz = //
# Tipos de potencia
# f(x) = x**5 + (2**2)**3
# f(x) = x**2569 + **8 - **9999

def exponente(funcion):
    pass



while True:
    x = "x"
    numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    list_exponente = []
    funcion = input("Ingrese una función: ")
    inicio = int(funcion.find("**"))
    while inicio != -1:
        num = 2
        for i in funcion[inicio+3: ]:
            num += 1
            if i not in str(numeros):
                break
        if num == 2:
            num = 6
        exponente = funcion[inicio+2: inicio+num]
        list_exponente.append(int(exponente))
        funcion = funcion[inicio+num: ]
        inicio = int(funcion.find("**"))
    exp_alto = max(list_exponente)
    print("El exponente más alto es: ", exp_alto)

    if exp_alto == 0:
        print("No es una función :p") 
    elif exp_alto == 1:
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
    