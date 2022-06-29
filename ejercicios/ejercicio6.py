################
# Julian Fontana - @Julian03-lab
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que a partir de tres variables de tipo entero retorne una tupla con dichos valores ordenados de menor a mayor. Y Viceversa
"""

def ordenar_mayor_a_menor(uno:int,dos:int,tres:int):
    """
    Toma como parametros tres numeros enteros y retorna una tupla con los valores ordenados de mayor a menor.
    """
    aux = None
    orden = [uno,dos,tres]
    count = 0
    while count < 2:
        if orden[count] >= orden[1]:
            orden[0] = orden[0]
        else:
            aux = orden[count]
            orden[count] = orden[1]
            orden[1] = aux
        if orden[count] >= orden[2]:
                pass
        else:
            aux = orden[count]
            orden[count] = orden[2]
            orden[2] = aux
        count += 1
    orden = tuple(orden)
    return(orden)
        
def ordenar_menor_a_mayor(uno,dos,tres):
    """
    Toma como parametros tres numeros enteros y retorna una tupla con los valores ordenados de menor a mayor.
    """
    aux = None
    orden = [uno,dos,tres]
    count = 0
    while count < 2:
        if orden[count] <= orden[1]:
            orden[0] = orden[0]
        else:
            aux = orden[count]
            orden[count] = orden[1]
            orden[1] = aux
        if orden[count] <= orden[2]:
                pass
        else:
            aux = orden[count]
            orden[count] = orden[2]
            orden[2] = aux
        count += 1
    orden = tuple(orden)
    return(orden)



def principal():  # pragma: no cover
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """

if __name__ == "__main__":  # pragma: no cover
    principal()

#3,2,1
#3,1,2
# 2,3,1
# 2,1,3
# 1,2,3
# 1,3,2