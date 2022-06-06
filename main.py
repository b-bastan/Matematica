import math, re

# ACLARAR QUE SOLO EXISTE X COMO INCÓGNITA
# Potencia = **; raiz = //
# Tipos de potencia

funcion = input("Ingrese una función: ")

inicio = int(funcion.find("**"))

res = print("Exponente: ", funcion[inicio: inicio+3])



new_funcion = funcion[inicio+3: ]

print("Nueva funcion: ", new_funcion)

new_inicio = int(new_funcion.find("**"))

res2 = print("Exponente: ", new_funcion[new_inicio: new_inicio+3])

res2 = new_funcion[new_inicio: new_inicio+3]

exponente = re.findall('[0-9]+', res2)

print("Solo exponente: ", exponente)