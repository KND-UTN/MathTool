from sympy import *
import numpy as np
import pandas as pd
import sympy


ln = sympy.log
log = sympy.log
sin = sympy.sin
cos = sympy.cos
e = np.exp(1)
w = Symbol('w')
x = Symbol('x')
y = Symbol('y')
z = Symbol('z')


def euler():
    ecw, pasos, xinicial, yinicial, zinicial, winicial, xfinal = mensaje_inicial()
    h = (xfinal - xinicial) / pasos

    matriz_solucion = []
    c1 = xinicial
    c2 = yinicial
    c3 = zinicial
    c4 = winicial

    for a in range(pasos + 1):
        c5 = c3
        c6 = c4
        c7 = ecw.subs(x, c1).subs(y, c2).subs(z, c3).subs(w, c4)

        c8 = c1 + h
        c9 = c2 + (h * c5)
        c10 = c3 + (h * c6)
        c11 = c4 + (h * c7)

        if a == pasos:
            c5 = ''
            c6 = ''
            c7 = ''
            c8 = ''
            c9 = ''
            c10 = ''
            c11 = ''

        fila_temporal = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11]
        matriz_solucion.append(fila_temporal)
        c1 = c8
        c2 = c9
        c3 = c10
        c4 = c11

    m = np.array(matriz_solucion).transpose()
    matriz_solucion = pd.DataFrame({'xm': m[0], 'ym': m[1], 'zm': m[2], 'wm': m[3], 'f(xm, ym, zm, wm)': m[4], 'g(xm, ym, zm, wm)': m[5], 'h(xm, ym, zm, wm)': m[6],
                                    'x(m+1)': m[7], 'y(m+1)': m[8], 'z(m+1)': m[9], 'w(m+1)': m[10]})
    return matriz_solucion


def euler_mejorado():
    raise Exception("Method not finished.")
    ecz, ecw, pasos, xinicial, yinicial, zinicial, winicial, xfinal = mensaje_inicial()
    h = (xfinal - xinicial) / pasos

    matriz_solucion = []
    c1 = xinicial
    c2 = yinicial
    c3 = zinicial
    c4 = winicial

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
    raise Exception("Method not finished.")
    ecw, pasos, xinicial, yinicial, zinicial, winicial, xfinal = mensaje_inicial()
    h = (xfinal - xinicial) / pasos

    matriz_solucion = []
    c1 = xinicial
    c2 = yinicial
    c3 = zinicial
    c4 = winicial

    for a in range(pasos + 1):
        # Primer parte
        c5 = c3
        c6 = c4
        c7 = ecw.subs(x, c1).subs(y, c2).subs(z, c3).subs(w, c4)

        # Segunda parte
        c8 = c1 + (h / 2)
        c9 = c2 + ((h / 2) * c5)
        c10 = c3 + ((h / 2) * c6)
        c11 = c4 + ((h / 2) * c7)
        c12 = c10
        c13 = c11
        c14 = ecw.subs(x, c8).subs(y, c9).subs(z, c10).subs(w, c11)

        # Tercera parte
        c15 = c14
        c16 = c2 + ((h / 2) * c12)
        c17 = c3 + ((h / 2) * c13)
        c18 = c4 + ((h / 2) * c14)
        c19 = c17
        c20 = c18
        c21 = ecw.subs(x, c15).subs(y, c16).subs(z, c17).subs(w, c18)

        # Cuarta parte
        c22 = c1 + h
        c23 = c2 + (h * c19)
        c24 = c3 + (h * c20)
        c25 = c4 + (h * c21)

        c26 = c24
        c27 = c25
        c28 = ecw.subs(x, c22).subs(y, c23).subs(z, c24).subs(w, c25)

        c29 = c2 + ((h / 6) * (c5 + 2 * c12 + 2 * c19 + c26))
        c30 = c3 + ((h / 6) * (c6 + 2 * c13 + 2 * c15 + c27))
        c31 = c4 + ((h / 6) * (c7 + 2 * c14 + 2 * c15 + c28))

        if a == pasos:
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
            c23 = ''
            c24 = ''
            c25 = ''
            c26 = ''
            c27 = ''
            c28 = ''
            c29 = ''
            c30 = ''
            c31 = ''

        fila_temporal = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20, c21, c22, c23, c24, c25, c26, c27, c28, c29, c30, c31]
        matriz_solucion.append(fila_temporal)
        c1 = c22
        c2 = c29
        c3 = c30
        c4 = c31

    m = np.array(matriz_solucion).transpose()
    matriz_solucion = pd.DataFrame({'xm': m[0], 'ym': m[1], 'zm': m[2], 'wm': m[3], 'k1': m[4],
                                    'l1': m[5], 'm1': m[6], 'xm + (h/2)': m[7], 'ym + k1 * (h/2)': m[8], 'zm + l1 * (h/2)': m[9], 'wm + m1 * (h/2)': m[10],
                                    'k2': m[11], 'l2': m[12], 'm2': m[13], 'xm+(h/2)': m[14], 'ym + k2 * (h/2)': m[15],
                                    'zm + l2 * (h/2)': m[16], 'wm + m2 * (h/2)': m[17], 'k3': m[18], 'l3': m[19], 'm3': m[20], 'x(m+1)': m[21],
                                    'ym + h * k3': m[22], 'zm + h*l3': m[23], 'wm + h*m3': m[24], 'k4': m[25], 'l4': m[26], 'm4': m[27],
                                    'y(m+1)': m[28], 'z(m+1)': m[29], 'w(m+1)': m[30]})
    return matriz_solucion


def mensaje_inicial():
    ecw = eval(input('Ingrese la ecuacion derivada tercera de Y: ').replace('^', '**'))
    pasos = int(input('Ingrese la cantidad de pasos a realizar: '))
    xinicial = float(input('Ingrese el valor en X inicial: '))
    yinicial = float(input('Ingrese el valor en Y inicial: '))
    zinicial = float(input('Ingrese el valor en Z inicial (derivada primera de Y): '))
    winicial = float(input('Ingrese el valor en w inicial (derivada segunda de Y): '))
    xfinal = float(input('Ingrese el valor en X final: '))
    return ecw, pasos, xinicial, yinicial, zinicial, winicial, xfinal


