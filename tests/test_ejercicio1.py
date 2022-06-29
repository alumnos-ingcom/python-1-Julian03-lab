from ejercicios.ejercicio1 import convertir_a_farenheit
################
# Nombre - @usuario_github
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Describir aquí que es lo que se esta probando.
Tengan en cuenta que el archivo tiene que llamarse igual
que el archivo a probar agregando antes `test_`
"""
import pytest
from ejercicios.ejercicio1 import *


def test_convertir_a_farenheit():
    """
       Una breve descripción del caso de prueba aplicado a la función
    """
    assert convertir_a_farenheit(0) == 32
