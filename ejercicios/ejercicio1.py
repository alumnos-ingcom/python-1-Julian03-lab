################
# Julian Fontana - @Julian03-lab
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Se quiere transformar temperaturas en grados fahrenheit a grados centígrados y viceversa.

Escribir las funciones para convertir la temperatura en grados centigrados en fahrenheit como un número decimal, utilice esta formula para calcular los grados centígrados y retorne el resultado obtenido. Y viceversa.
"""


def convertir_a_farenheit(centigrados):
    '''
    Toma como argumento un número que representa los grados Celsius (°C) y lo retorna en grados Fahrenheit (°F).
    '''
    farenheit = (centigrados * 1.8) + 32
    return(farenheit)
    

def convertir_a_centigrados(farenheit):
    '''
    Toma como argumento un número que representa los grados Fahrenheit (°F) y lo retorna en grados Celsius (°C).
    '''
    centigrados = (farenheit-32)/1.8
    return(centigrados)

def principal():  # pragma: no cover
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    convertir_a_centigrados()
    convertir_a_farenheit()
if __name__ == "__main__":  # pragma: no cover
    principal()

