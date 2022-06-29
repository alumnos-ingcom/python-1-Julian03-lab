################
# Julian Fontana - @Julian03-lab
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que indique con True si un número entero es multiplo de otro, utilizando sumas y restas.
"""



def es_multiplo(numero:int, multiplo:int):
    """
    Recibe dos numeros enteros. Retorna True si el segundo es multiplo del primero, en caso de que no lo sea retorna False.
    """
    print(multiplo % numero, multiplo // numero)
    while multiplo > 0:
        multiplo -= numero
    return (multiplo == 0)
 

def principal():  # pragma: no cover
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """


if __name__ == "__main__":  # pragma: no cover
    principal()

