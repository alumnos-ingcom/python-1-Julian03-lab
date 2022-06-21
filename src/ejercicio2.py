################
# Julian Fontana - @Julian03-lab
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que reciba un número e indique si el mismo es positivo, negativo o cero utilizando sumas y restas.
"""

def signo(numero):
    '''
    Recibe un numero y retorna informacion acerca de si el numero es positivo, negativo o cero.
    '''
    valor_original = 0
    valor_comparativo = valor_original - numero
    if valor_comparativo > valor_original:
        signo = "-"
    elif valor_comparativo - valor_original:
        signo = "+"
    else:
        signo = 0
    
    return(signo)
    

def principal():  # pragma: no cover
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    signo()

if __name__ == "__main__":  # pragma: no cover
    principal()

