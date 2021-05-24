__author__ = 'Leila Spini, Ignacio Pieve, Sofia Cibello, Juan Pablo Donalisio'
__version__ = 1.0

from sympy import *
import modulos.mensajes as msg
import modulos.tipoA as A
import modulos.tipoB as B
import modulos.tipoC as C
import os
import pandas as pd


def menu():
    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 1000)

    opc = msg.opciones_principales()
    os.system('cls')

    retorno = False
    if opc == 1:
        opc2 = msg.opciones_tipo_a()
        if opc2 == 1:
            retorno = A.euler()
        elif opc2 == 2:
            retorno = A.euler_mejorado()
        else:
            retorno = A.runge_kutta()

    elif opc == 2:
        opc2 = msg.opciones_tipo_b()
        if opc2 == 1:
            retorno = B.euler()
        elif opc2 == 2:
            retorno = B.euler_mejorado()
        else:
            retorno = B.runge_kutta()

    elif opc == 3:
        opc2 = msg.opciones_tipo_c()
        if opc2 == 1:
            retorno = C.euler()
        elif opc2 == 2:
            retorno = C.euler_mejorado()
        else:
            retorno = C.runge_kutta()

    print(retorno)


if __name__ == '__main__':
    menu()
