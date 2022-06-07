from cgi import print_arguments
import math, re

# ACLARAR QUE SOLO EXISTE X COMO INCÓGNITA
# Potencia = **; raiz = //
# Tipos de potencia
# f(x) = x**5 + (2**2)**3
# f(x) = x**2569 + **8 - **9999

def exponente(funcion):
    pass

# NO PUEDEN INGRESARSE EXPONENTES MAYORES A 9999

while True:
    numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    list_exponente = []
    funcion = input("Ingrese una función: ")
    inicio = int(funcion.find("**"))
    while inicio != -1:
        print("Inicio: ", inicio)
        num = 2
        print("Número inicio: ", num)
        for i in funcion[inicio+3: ]:
            num += 1
            if i not in str(numeros) or i == " ":
                print("I que no esta entre los numeros: ", i)
                break
        print("Número fin: ", num)
        if num == 2:
            num += 4
        print("Numero: ", num)
        exponente = funcion[inicio+2: inicio+num]
        print(exponente)
        list_exponente.append(exponente)
        funcion = funcion[inicio+num: ]
        inicio = int(funcion.find("**"))
    print(list_exponente)
    exp_alto = max(list_exponente)
    print("El exponente más alto es: ", exp_alto)
    if exp_alto == 2:
        print("Es cuadrática") 

    
    



new_funcion = funcion[inicio+3: ]

print("Nueva funcion: ", new_funcion)

new_inicio = int(new_funcion.find("**"))

res2 = print("Exponente: ", new_funcion[new_inicio: new_inicio+3])

res2 = new_funcion[new_inicio: new_inicio+3]

exponente = re.findall('[0-9]+', res2)

print("Solo exponente: ", exponente)