################
# Julian Fontana - @Julian03-lab
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir un programa que permita transformar un número solicitado expresado en grados, minutos y segundos a segundos a segundos. Y otra que haga el cambio en el sentido contrario, devolviendo una tuple.
"""
def sexadecimal_a_decimal(horas,minutos,segundos):
    """
    Recibe como atributos enteros que representan las horas,minutos y segundos. Retorna un entero que representa la conversion de estas a segundos.
    """

    horas = (horas*60)*60
    minutos = minutos * 60
    conversion = horas + minutos + segundos

    return (conversion)

def decimal_a_sexadecimal(numero):
    """
    Recibe como atributo un entero que representa los segundos. Retorna una tupla con la conversion de los segundos a horas, minutos y segundos.
    """
    horas = int((numero/60)/60)
    segundos = numero - ((horas*60)*60)
    minutos = int(segundos/60)

    segundos  -= (minutos*60)
    return(horas,minutos,segundos)

def principal():  # pragma: no cover
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """

if __name__ == "__main__":  # pragma: no cover
    principal()
