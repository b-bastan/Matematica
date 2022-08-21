import os # Sirve para poder limpiar la consola

#################################-- VARIABLES GLOBALES --#################################

value = False # Variable auxiliar que sirve para indicar si la función que ingresó el usuario se debe o no volver a analizar
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] # Lista de números

#################################-- FUNCIONES --#################################

def ingresarFuncion():

    # Esta función quita todos los espacios dentro la función ingresada por el usuario, además que coloca en minúscula la x en caso de que se encuentre en mayúscula y corrobora que exista aunque sea una x en la función, ya que caso contrario no se puede analizar como tal

    global value, funcion # global permite que el valor de estas variables sea accedido desde cualquier lugar del programa

    if value: # Si value es igual a True...
        return funcion # Devuelve la función
    else:
        value = True 
        while True: # Es un bucle infinito que se ejecuta indefinidamente hasta el final o cuando el programa se detenga a la fuerza
            funcion = str(input("Ingrese una función: f(x) = ")) # Convierte en string (o cadena de caracteres) la función que ingresará el usuario a través del input

            try: # Intenta ejecutar algo, en caso de que tire error, proseguirá con el except ValueError
                funcion = funcion.lower() # Convierte cualquier caracter de la función que esté en mayúscula a minúscula
                int(funcion.index("x")) # Busca una x en la función: si no la encuentra, lanza el error ValueError
                funcion = funcion.replace(" ", "") # Quita los espacios de la función 
                break
            except ValueError:
                print("Por favor, ingrese correctamente la incógnita")
        return funcion


def exponente():

    # Esta función se encarga de buscar cuál es el exponente al que está elevado x, ya que se supone (por el código while de abajo, si es necesario ir a revisar ese código antes para comprender mejor) que es una función polinómica. 

    list_exponente = [] # Dentro de esta lista iremos guardando todos los exponentes que encontremos dentro de la función (donde x está elevado a algún numero), y al final se decide cuál es el exponente más alto para determinar qué tipo de grado tiene la función
    funcion = ingresarFuncion() # Llama a la función ingresarFuncion() para que devuelva la función ingresada por el usuario que será almacenada en la variable funcion
    
    inicio = int(funcion.find("x**")) # Busca si existe x** en la función: en caso de que no la encuentre, devuelve un -1
    fraccion()

    # Mientras que inicio sea distinto a -1, es decir que haya encontrado x**, va a ejecutar este bucle
    while inicio != -1:
        num = 2 # Variable auxiliar
        for i in funcion[inicio+3: ]: # Bucle que se ejecuta desde inicio+3:, ya que x** tiene tres caracteres, y empieza a buscar una x
            if i not in str(numeros): # En caso de que no encuentre un número luego de x** porque encuentra un + por ejemplo, rompe el bucle
                break
            num += 1
        if num == 3: # Es solo para evitar algunos errores en el código, en definitiva es una variable auxiliar
            num = 4
        exponente = int(funcion[inicio+3: inicio+num]) # Utilizando la variable auxiliar, podemos determinar desde donde empieza hasta donde termina el exponente, por ejemplo x**23, sabemos que el exponente es 23
        list_exponente.append(exponente) # Se añade el exponente a la lista list_exponente
        funcion = funcion[inicio+num: ] # Esto sirve para poder volver a buscar dentro de la lista a partir del último lugar donde se buscó, para que así no vuelva a buscar el primer x** que encuentre en la función
        inicio = int(funcion.find("x**")) # Busca nuevamente si existe x** en la función
    try: # Cuando rompe el bucle while, intenta encontrar el máximo número de exponente, en caso que no lo encuentre coloca que el expo_alto = 0, no porque matemáticamente lo sea, sino para luego indicar en el while de más abajo qué texto debe imprimir, es decir que imprimiría "Es una función lineal"
        exp_alto = max(list_exponente)
    except ValueError:
        exp_alto = 0
    
    return exp_alto # Devuelve el expo_alto


def raiz():

    # Función que se encarga de ver si la función ingresada por el usuario contiene una raíz, y en caso de ser así si es o no una función irracional

    funcion = ingresarFuncion() # Llama a la función ingresarFuncion() para que devuelva la función ingresada por el usuario que será almacenada en la variable funcion

    find_raiz = int(funcion.find("raiz(")) # Busca si existe raiz( en la función: en caso de que no la encuentre, devuelve un -1

    # Condicional que se ejecuta solo en caso de que find_raiz devuelva un valor distinto a -1
    if find_raiz != -1:
        for i in funcion[find_raiz+5: ]: # Bucle que se ejecuta desde find_raiz+5, ya que raiz( tiene cinco caracteres, y empieza a buscar una x dentro de esa raiz
            if i != ")": # Si la raiz no está cerrada se ejecuta lo siguiente
                if i == "x": # Si encuentra una x dentro de la raiz, devuelve True
                    return True
            else:
                break # Si la raiz está cerrada, se rompe el bucle for
    

def fraccion():

    # Función que se encarga de ver si la función ingresada por el usuario contiene una división, y en caso de ser así si es o no una función racional

    funcion = ingresarFuncion() # Llama a la función ingresarFuncion() para que devuelva la función ingresada por el usuario que será almacenada en la variable funcion

    find_fraccion = int(funcion.find("/(")) # Busca si existe /( en la función: en caso de que no lo encuentre, devuelve un -1

    # Condicional que se ejecuta en caso de que find_fraccion devuelva un valor distinto a -1. Cabe destacar que este if find_fraccion != -1 tiene como función encontrar funciones racionales tales como f(x) = 1/(x+3)
    if find_fraccion != -1:
        for i in funcion[find_fraccion+2: ]: # Bucle que se ejecuta desde find_fraccion+2, ya que /( tiene dos caracteres, y empieza a buscar una x dentro de esa división
            if i != ")": # Si la división no está cerrada se ejecuta lo siguiente
                if i == "x": # Si encuentra una x dentro de la división, devuelve True
                    return True
            else:
                break # Si la raiz está cerrada, se rompe el bucle for  
    # En caso de que find_fraccion devuelva -1, se ejecuta otro código que a diferencia del if find_fraccion != -1, se encarga de encontrar funciones racionales tales como f(x) = 1/x
    else:
        find_fraccion = int(funcion.find("/")) # Busca si existe / en la función
        # Condicional que se ejecuta solo en caso de que find_fraccion devuelva un valor distinto a -1
        if find_fraccion != -1: 
            for i in funcion[find_fraccion+1: ]: # Bucle que se ejecuta desde find_fraccion+1, ya que / tiene un caracter, y empieza a buscar una x dentro de esa división
                if i not in str(numeros):
                    if i == "x":
                        return True
                else:
                    break
                

def error(valor):

    # Esta función se encarga de validar que la opción ingresada por el usuario no sea cualquier tipo de datos (letras, símbolos, etc.), solo números

    while True: # Bucle que se repetirá hasta que el usuario ingrese correctamente la opción
        try:
            opcion = int(input(valor))
            return opcion
        except ValueError:
            print("Ingrese la opción correctamente")
            input("Presione ENTER para continuar...")
            


#################################-- MAIN --#################################


while True: # Bucle repetirá el programa constantemente
    os.system("cls") # Limpia la consola cuando comienza el bucle

    cadena = "¡Bienvenido a Pipo's Functions!"

    print(cadena.center(70, " ")) # Estético, solo centra el texto

    print("""
ANTES DE USAR EL PROGRAMA, ES NECESARIO TENER EN CUENTA QUE...
a) Utilizaremos x como incógnita
b) Una potencia se indica con "**"
c) Una raíz se indica dentro de "raiz()"

-------------------------------------------------------------------------

Menú de opciones
    1. Conocer tipos de funciones
    2. Analizar qué tipo de función es
    3. Salir

""")
    opcion = error(">>> ") # Mandamos la opción escogida a esta función

    # Condicional que mostrará en pantalla qué tipo de función es la ingresada por el usuario, haciendo uso de las funciones anteriormente creadas
    if opcion == 1:
        print("Tipos de funciones")
    elif opcion == 2:
        if raiz(): # Si la función raiz() devuelve True...
            print("Es una función irracional")
        else:
            if fraccion(): # Si la función fraccion() devuelve True...
                print("Es una función racional")
            else: # Si no es una fracción, entonces es una función polinómica
                print("Es una función polinómica")
                exp_alto = exponente() # Llamamos a la función exponente()
                if exp_alto == 0: # Dependiendo del valor retornado, se ejecutará lo siguiente
                    print("Es una función lineal")
                elif exp_alto >= 2:
                    if exp_alto == 2:
                        print("Es una función cuadrática")
                    elif exp_alto == 3:
                        print("Es una función cúbica")
                    elif exp_alto >= 4: # Si el exponente es mayor a 4, directamente colocamos el número del exponente y le añadimos la palabra grando a la derecha
                        print("Es una función de " + str(exp_alto) + " grado")
        value = False
    elif opcion == 3:
        break
    else:
        print("Ingrese alguna de las opciones especificadas.")
    input("Presione ENTER para continuar...")