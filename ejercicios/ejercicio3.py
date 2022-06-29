################
# Julian Fontana - @Julian03-lab
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que utilizando sumas y restas, reciba dos valores y retorne:

Retornar -1 si el primero es menor que el segundo
Retornar 0 si son iguales
Retornar 1 si el primero es mayor que el segundo
"""

def compara(numero, otro_numero):
    """
    Recibe dos valores numericos.
    Retorna -1 si el primero es menor que el segundo. Retorna 0 si son iguales. Retorna 1 si el primero es mayor que el segundo
    """
    nuevo_numero = numero - otro_numero
    if nuevo_numero > 0:
        nuevo_numero = 1
    elif nuevo_numero < 0:
        nuevo_numero = -1
    else:
        nuevo_numero = 0
    return(nuevo_numero)

def principal():  # pragma: no cover
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """

if __name__ == "__main__":  # pragma: no cover
    principal()

