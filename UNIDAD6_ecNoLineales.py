__author__ = 'Ignacio Pieve Roiger'
__version__ = 0.1

from sympy import *
import numpy as np
import pandas as pd


def menu():
    print('Aproximador de raices')

    x = Symbol('x')
    ec = eval(input('Ingrese la ecuacion: '))
    decx = 10 ** (-int(input('Cuantos decimales desea en x?: ')))
    decy = 10 ** (-int(input('Cuantos decimales desea en y?: ')))

    raices = preguntarRaices()
    matrix = generador_matriz(raices, ec, decx, decy)
    codigoEnLatex = formateadorMatriz(matrix, raices, ec, decx, decy)
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


def formateadorMatriz(matriz, raices, ec, decx, decy):
    x = Symbol('x')
    mensaje = "\nEcuacion: " + str(ec) + '\nDerivada: ' + str(ec.diff(x)) + '\n\n'

    for a in range(len(matriz)):
        mensaje += '-' * 75 + '\n\n' + 'Aproximando a raiz: ' + str(raices[a]) + '\n\n'

        t1 = np.array(matriz[a]).transpose()
        temporal2 = pd.DataFrame({"xi": t1[0], "f(xi)": t1[1], "f'(xi)": t1[2], "xi + 1": t1[3]})
        mensaje += str(temporal2)
        mensaje += '\n\n' + 'Solucion: ' + str(matriz[a][-1][3]) + '\n\n'

    return mensaje






if __name__ == "__main__":
    menu()