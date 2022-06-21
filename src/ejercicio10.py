################
# Julian Fontana - @Julian03-lab
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que indique con True si una palabra o frase ingresada se trata de un palindromo. Palíndromo, es si se lee igual de derecha a izquierda que de izquierda a derecha.
"""

def es_palindromo(texto):
    """
    Recibe como atributo un string. Retorna True si el string es palindromo, de caso contrario retorna False.
    """
    texto = texto.lower()
    texto = texto.replace(" ", "")
    texto = list(texto)
    texto_reversa = texto[::-1]
    return (texto == texto_reversa)


def principal():  # pragma: no cover
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """

if __name__ == "__main__":  # pragma: no cover
    principal()

