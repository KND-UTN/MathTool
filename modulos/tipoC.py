from sympy import *
import numpy as np
import pandas as pd


def euler():
    x = Symbol('x')
    y = Symbol('y')
    z = Symbol('z')
    ecz = eval(input('Ingrese la ecuacion derivada de z: '))
    pasos = int(input('Ingrese la cantidad de pasos a realizar: '))
    xinicial = float(input('Ingrese el valor en X inicial: '))
    yinicial = float(input('Ingrese el valor en Y inicial: '))
    zinicial = float(input('Ingrese el valor en Z inicial: '))
    xfinal = float(input('Ingrese el valor en X final: '))
    h = (xfinal - xinicial) / pasos

    matriz_solucion = []
    c1 = xinicial
    c2 = yinicial
    c3 = zinicial

    for a in range(pasos + 1):
        c4 = c3
        c5 = ecz.subs(x, c1).subs(y, c2).subs(z, c3)
        c6 = c1 + h
        c7 = c2 + (h * c4)
        c8 = c3 + (h * c5)

        if a == pasos:
            c4 = ''
            c5 = ''
            c6 = ''
            c7 = ''
            c8 = ''

        fila_temporal = [c1, c2, c3, c4, c5, c6, c7, c8]
        matriz_solucion.append(fila_temporal)
        c1 = c6
        c2 = c7
        c3 = c8

    m = np.array(matriz_solucion).transpose()
    matriz_solucion = pd.DataFrame({'xm': m[0], 'ym': m[1], 'zm': m[2], 'f(xm, ym, zm)': m[3], 'g(xm, ym, zm)': m[4],
                                    'x(m+1)': m[5], 'y(m+1)': m[6], 'z(m+1)': m[7]})
    return matriz_solucion


def euler_mejorado():
    x = Symbol('x')
    y = Symbol('y')
    z = Symbol('z')
    ecz = eval(input('Ingrese la ecuacion derivada de z: '))
    pasos = int(input('Ingrese la cantidad de pasos a realizar: '))
    xinicial = float(input('Ingrese el valor en X inicial: '))
    yinicial = float(input('Ingrese el valor en Y inicial: '))
    zinicial = float(input('Ingrese el valor en Z inicial: '))
    xfinal = float(input('Ingrese el valor en X final: '))
    h = (xfinal - xinicial) / pasos

    matriz_solucion = []
    c1 = xinicial
    c2 = yinicial
    c3 = zinicial

    for a in range(pasos + 1):
        c4 = c3
        c5 = ecz.subs(x, c1).subs(y, c2).subs(z, c3)
        c6 = c1 + h
        c7 = c2 + (h * c4)
        c8 = c3 + (h * c5)
        c9 = c8
        c10 = ecz.subs(x, c6).subs(y, c7).subs(z, c8)
        c11 = c2 + ((h / 2) * (c4 + c9))
        c12 = c3 + ((h / 2) * (c5 + c10))

        if a == pasos:
            c4 = ''
            c5 = ''
            c6 = ''
            c7 = ''
            c8 = ''
            c9 = ''
            c10 = ''
            c11 = ''
            c12 = ''

        fila_temporal = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12]
        matriz_solucion.append(fila_temporal)
        c1 = c6
        c2 = c11
        c3 = c12

    m = np.array(matriz_solucion).transpose()
    matriz_solucion = pd.DataFrame({'xm': m[0], 'ym': m[1], 'zm': m[2], 'f(xm, ym, zm)': m[3], 'g(xm, ym, zm)': m[4],
                                    'x(m+1) *1': m[5], 'ym + h * f(xm, ym, zm) *2': m[6], 'zm + h * g(xm, ym, zm) *3': m[7],
                                    'f(1, 2, 3)': m[8], 'g(1, 2, 3)': m[9], 'y(m+1)': m[10], 'z(m+1)': m[11]})
    return matriz_solucion

def runge_kutta():
    x = Symbol('x')
    y = Symbol('y')
    z = Symbol('z')
    ecz = eval(input('Ingrese la ecuacion derivada de z: '))
    pasos = int(input('Ingrese la cantidad de pasos a realizar: '))
    xinicial = float(input('Ingrese el valor en X inicial: '))
    yinicial = float(input('Ingrese el valor en Y inicial: '))
    zinicial = float(input('Ingrese el valor en Z inicial: '))
    xfinal = float(input('Ingrese el valor en X final: '))
    h = (xfinal - xinicial) / pasos

    matriz_solucion = []
    c1 = xinicial
    c2 = yinicial
    c3 = zinicial

    for a in range(pasos + 1):
        c4 = c3
        c5 = ecz.subs(x, c1).subs(y, c2).subs(z, c3)
        c6 = c1 + (h / 2)
        c7 = c2 + ((h / 2) * c4)
        c8 = c3 + ((h / 2) * c5)
        c9 = c8
        c10 = ecz.subs(x, c6).subs(y, c7).subs(z, c8)
        c11 = c6
        c12 = c2 + ((h / 2) * c9)
        c13 = c3 + ((h / 2) * c10)
        c14 = c13
        c15 = ecz.subs(x, c11).subs(y, c12).subs(z, c13)
        c16 = c1 + h
        c17 = c2 + (h * c14)
        c18 = c3 + (h * c15)
        c19 = c18
        c20 = ecz.subs(x, c16).subs(y, c17).subs(z, c18)
        c21 = c2 + ((h / 6) * (c4 + 2 * c9 + 2 * c14 + c19))
        c22 = c3 + ((h / 6) * (c5 + 2 * c10 + 2 * c15 + c20))

        if a == pasos:
            c4 = ''
            c5 = ''
            c6 = ''
            c7 = ''
            c8 = ''
            c9 = ''
            c10 = ''
            c11 = ''
            c12 = ''
            c13 = ''
            c14 = ''
            c15 = ''
            c16 = ''
            c17 = ''
            c18 = ''
            c19 = ''
            c20 = ''
            c21 = ''
            c22 = ''

        fila_temporal = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20, c21, c22]
        matriz_solucion.append(fila_temporal)
        c1 = c16
        c2 = c21
        c3 = c22

    m = np.array(matriz_solucion).transpose()
    matriz_solucion = pd.DataFrame({'xm': m[0], 'ym': m[1], 'zm': m[2], 'k1': m[3],
                                    'l1': m[4], 'xm + (h/2)': m[5], 'ym + k1 * (h/2)': m[6], 'zm + l1 * (h/2)': m[7],
                                    'k2': m[8], 'l2': m[9], 'xm+(h/2)': m[10], 'ym + k2 * (h/2)': m[11],
                                    'zm + l2 * (h/2)': m[12], 'k3': m[13], 'l3': m[14], 'x(m+1)': m[15],
                                    'ym + h * k3': m[16], 'zm + h*l3': m[17], 'k4': m[18], 'l4': m[19],
                                    'y(m+1)': m[20], 'z(m+1)': m[21]})
    return matriz_solucion











