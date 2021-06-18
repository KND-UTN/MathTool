__author__ = 'Leila Spini, Ignacio Pieve, Sofia Cibello, Juan Pablo Donalisio'
__version__ = 0.1

from sympy import *
import numpy as np
import pandas as pd
from math import e


def derivada(x):
    return diff(x)


def menu():
    print('Aproximador de raices')
    x = Symbol('x')
    ec = eval(input('Ingrese la ecuacion: ').replace('^', '**'))
    decx = 10 ** (-int(input('Cuantos decimales desea en x (dx)?: ')))
    decy = 10 ** (-int(input('Cuantos decimales desea en y (dy)?: ')))

    raices = preguntarRaices()
    matrix = generador_matriz(raices, ec, decx, decy)
    codigoEnLatex = formateadorMatriz(matrix, raices, ec)
    print(codigoEnLatex)


def preguntarRaices():
    cant = int(input('Cuantas raices desea calcular?: '))
    lista = []
    for a  in range(cant):
        lista.append(float(input('Ingrese la raiz n' + str(a) + ': ')))
    return lista


def generador_matriz(roots, ec, decx, decy):
    x = Symbol('x')

    matrizGrande = []

    for a in roots:
        matriz = []
        c1 = float(a)
        c2 = float(ec.subs(x, c1))
        c3 = float(ec.diff(x).subs(x, c1))
        c4 = float(c1 - (c2/c3))
        c5 = float(c4 - c1)
        c6 = float(ec.subs(x, c4))
        tempRow = [c1, c2, c3, c4, c5, c6]
        matriz.append(tempRow)
        ultimo = c4

        while (abs(float(c4 - c1)) >= decx) or (abs(float(ec.subs(x, c4))) >= decy):
            c1 = float(ultimo)
            c2 = float(ec.subs(x, c1))
            c3 = float(ec.diff(x).subs(x, c1))
            c4 = float(c1 - (c2 / c3))
            c5 = float(c4 - c1)
            c6 = float(ec.subs(x, c4))
            tempRow = [c1, c2, c3, c4, c5, c6]
            matriz.append(tempRow)
            ultimo = c4

        matrizGrande.append(matriz)

    return matrizGrande


def formateadorMatriz(matriz, raices, ec):
    x = Symbol('x')
    mensaje = "\nEcuacion: " + str(ec).replace("**", '^') + '\nDerivada: ' + str(ec.diff(x)).replace("**", '^') + '\n\n'
    soluciones = []

    for a in range(len(matriz)):
        mensaje += '-' * 75 + '\n\n' + 'Aproximando a raiz: ' + str(raices[a]) + '\n\n'

        t1 = np.array(matriz[a]).transpose()
        temporal2 = pd.DataFrame({"xi": t1[0], "f(xi)": t1[1], "f'(xi)": t1[2], "xi + 1": t1[3]})
        mensaje += str(temporal2)
        mensaje += '\n\n' + 'Solucion: ' + str(matriz[a][-1][3]) + '\n\n'
        soluciones.append(str(matriz[a][-1][3]))

    mensaje += '-' * 75 + '\n\n' + 'Soluciones: ' '\n\n'
    c = 0
    for solucion in soluciones:
        mensaje += "Solución " + str(c) + ': ' + str(solucion) + '\n'
        c += 1

    return mensaje






if __name__ == "__main__":
    menu()
