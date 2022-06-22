################
# Julian Fontana - @Julian03-lab
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que retorne una tuple con factores primos de un numero entero positivo.
"""
def es_primo(numero:int):
    """
    Recibe como atributo un entero. Retorna True si el numero es primo y False si no es primo.
    """
    count = 2
    cantidad_restos = 0

    while count < numero:
        resto = numero%count
        if resto == 0:
            cantidad_restos +=1
        count += 1
    return(cantidad_restos==0)


def factores_primos(numero):
    numeros_primos = []
    for i in range(1,numero+1):
        if es_primo(i):
            numeros_primos.append(i)
    return(numeros_primos)


    
def principal():  # pragma: no cover
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    print(factores_primos(40))

if __name__ == "__main__":  # pragma: no cover
    principal()

