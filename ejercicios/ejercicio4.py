################
# Julian Fontana - @Julian03-lab
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que haga la suma entre dos números enteros sin hacer la operación de manera directa. Esto quiere decir que para hacer la suma entre 4 y 3, las operaciones resultantes deberán ser 4+1+1+1.

La funcion debe ser capaz de sumar cualquier numero entero positivo y negativo.
"""

def suma_lenta(numero, otro_numero):
    """
    Recibe dos numeros enteros positivos o negativos y hace la suma entre ellos de forma lenta. Retorna la suma entre los dos numeros.
    """
    count = 0
    if otro_numero < 0:
        while otro_numero < count:
            numero -= 1
            count -= 1
    elif otro_numero > 0:
        while otro_numero > count:
            numero += 1
            count += 1
    return(numero)

def principal():  # pragma: no cover
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """

if __name__ == "__main__":  # pragma: no cover
    principal()
