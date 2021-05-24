__author__ = 'Leila Spini, Ignacio Pieve, Sofia Cibello, Juan Pablo Donalisio'
__version__ = 2.0

import pandas as pd
import numpy as np
from sympy import *


def menu():
    vals = pedir_valores()
    funcs = pedir_funciones()
    constructor(vals, funcs)


def pedir_valores():
    cant = int(input('Cuantos valores desea ingresar?: '))
    valoresy = []
    valoresx = []
    for a in range(cant):
        valoresy.append(float(input('Ingrese el valor ' + str(a) + ' en y: ')))
        valoresx.append(float(input('Ingrese el valor ' + str(a) + ' en x: ')))
    m = pd.DataFrame({"Y": valoresy, "X": valoresx})
    return m


def pedir_funciones():
    cant = int(input('Cuantas funciones desea ingresar?: '))
    funciones = []
    x = Symbol('x')
    y = Symbol('y')
    c = Symbol('c')
    for a in range(cant):
        f = eval(input('Ingrese la funcion ' + str(a) + ': '))
        funciones.append(f)
    return funciones


def constructor(valores, ecuaciones):
    x = Symbol('x')
    y = Symbol('y')
    c = Symbol('c')
    ecuaciones_resueltas = []
    matrices_sin_datos = []
    matrices_con_datos = []
    soluciones = []
    terminos = []
    desviaciones = []
    for a in range(len(ecuaciones)):
        argumentos = (ecuaciones[a]).args
        cant_filas = len(argumentos)
        matriz = [[0 for x in range(cant_filas+1)] for y in range(cant_filas)]
        matriz2 = [[0 for x in range(cant_filas + 1)] for y in range(cant_filas)]
        for i in range(cant_filas):
            terminos.append('C' + str(i + 1))
            for j in range(cant_filas+1):
                if j == cant_filas:
                    matriz[i][j] = ((argumentos[i] / c) * y)
                else:
                    matriz[i][j] = ((argumentos[i] / c) * (argumentos[j] / c))

                total_esta_celda = 0
                for k in range(len(valores["X"])):
                    total_esta_celda += matriz[i][j].subs(x, valores['X'][k]).subs(y, valores['Y'][k])
                matriz2[i][j] = total_esta_celda

        matrices_sin_datos.append(matriz)
        matrices_con_datos.append(matriz2)

        solucionar = Matrix(matriz2)
        solucion = solve_linear_system_LU(solucionar, terminos)
        soluciones.append(solucion)
        terminos = []
        ecuacion_resuelta = []
        cont = 0
        for i in range(len(argumentos)):
            if c in argumentos[i].free_symbols:
                ecuacion_resuelta.append(argumentos[i].subs(c, solucion['C' + str(cont+1)]))
                cont += 1
            else:
                ecuacion_resuelta.append(argumentos[i])
        unida = 0
        for i in range(len(ecuacion_resuelta)):
            unida += ecuacion_resuelta[i]
        ecuaciones_resueltas.append(unida)

        desviacion = 0
        for k in range(len(valores["X"])):
            t1 = ecuaciones_resueltas[a].subs(x, valores['X'][k]).subs(y, valores['Y'][k])
            t2 = valores['Y'][k] - t1
            desviacion += t2 ** 2
        desviaciones.append(desviacion)

    mostrador(ecuaciones, matrices_sin_datos, matrices_con_datos, soluciones, ecuaciones_resueltas, valores, desviaciones)


def mostrador(ecs, matricessd, matricescd, soluciones, ecsresueltas, datos, desv):
    print('-' * 75)
    print('Datos:')
    print(datos)
    print('')
    print('Ecuaciones planteadas:')
    for a in ecs:
        print('F(x) = ' + str(a))

    c = 0
    for a in ecs:
        print('\n' + '-' * 75)
        c += 1
        print('Ecuacion ' + str(c) + ': ' + str(a))
        print('\nMatriz con datos (Sin resolver):')
        temp = Matrix(matricessd[c-1])
        temp = np.array(temp.transpose())
        msr = {}
        for b in range(len(matricessd[c-1][0])):
            if b == len(matricessd[c-1][0]) - 1:
                msr['Y'] = temp[b]
            else:
                msr['C' + str(b + 1)] = temp[b]
        temp = pd.DataFrame(msr)
        print(temp)

        print('\nMatriz con datos (Resuelta):')
        temp = Matrix(matricescd[c-1])
        temp = np.array(temp.transpose())
        msr = {}
        for b in range(len(matricescd[c-1][0])):
            if b == len(matricescd[c-1][0]) - 1:
                msr['Y'] = temp[b]
            else:
                msr['C' + str(b + 1)] = temp[b]
        temp = pd.DataFrame(msr)
        print(temp)

        print('\nConjunto de soluciones: ')
        for i in soluciones[c-1]:
            print(str(i) + ': ' + str(soluciones[c-1][i]))
        print('\nEcuacion final: ' + str(ecsresueltas[c-1]))
        print('Desviacion: ' + str(desv[c-1]))


if __name__ == "__main__":
    menu()
