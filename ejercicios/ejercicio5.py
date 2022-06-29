################
# Julian Fontana - @Julian03-lab
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que mediante restas sucesivas, obtenga el valor del cociente y resto de dos números enteros.
"""

def division_lenta(dividendo, divisor):
    """
    Recibe como atributos dos numeros enteros que representan el dividendo y el divisor. Retorna mediante restas sucesivas el cociente y el resto.
    """

    cociente = 0
    while dividendo > divisor:
        dividendo -= divisor
        cociente += 1
    return(cociente,dividendo)


def principal():  # pragma: no cover
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """

if __name__ == "__main__":  # pragma: no cover
    principal()