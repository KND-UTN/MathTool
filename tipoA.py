from sympy import *


def euler():
    x = Symbol('x')
    y = Symbol('y')
    ec = eval(input('Ingrese la ecuacion de la derivada: '))
    pasos = int(input('Ingrese la cantidad de pasos a realizar: '))
    xinicial = float(input('Ingrese el valor en X inicial: '))
    yinicial = float(input('Ingrese el valor en Y inicial: '))
    xfinal = float(input('Ingrese el valor en X final: '))
    h = (xfinal - xinicial) / pasos

    matriz_solucion = []
    c1 = xinicial
    c2 = yinicial
    for a in range(pasos + 1):
        c3 = ec.subs(x, c1).subs(y, c2)
        c4 = c1 + h
        c5 = c2 + h * (c3)

        if a == pasos:
            c3 = ''
            c4 = ''
            c5 = ''

        fila_temporal = [c1, c2, c3, c4, c5]
        matriz_solucion.append(fila_temporal)
        c1 = c4
        c2 = c5

    return matriz_solucion


def euler_mejorado():
    x = Symbol('x')
    y = Symbol('y')
    ec = eval(input('Ingrese la ecuacion de la derivada: '))
    pasos = int(input('Ingrese la cantidad de pasos a realizar: '))
    xinicial = float(input('Ingrese el valor en X inicial: '))
    yinicial = float(input('Ingrese el valor en Y inicial: '))
    xfinal = float(input('Ingrese el valor en X final: '))
    h = (xfinal - xinicial) / pasos

    matriz_solucion = []
    c1 = xinicial
    c2 = yinicial
    for a in range(pasos + 1):
        c3 = ec.subs(x, c1).subs(y, c2)
        c4 = c1 + h
        c5 = c2 + h * (c3)
        c6 = ec.subs(x, c4).subs(y, c5)
        c7 = c2 + (h / 2) * ( c3 + c6 )

        if a == pasos:
            c3 = ''
            c4 = ''
            c5 = ''
            c6 = ''
            c7 = ''

        fila_temporal = [c1, c2, c3, c4, c5, c6, c7]
        matriz_solucion.append(fila_temporal)
        c1 = c4
        c2 = c7

    return matriz_solucion


def runge_kutta():
    x = Symbol('x')
    y = Symbol('y')
    ec = eval(input('Ingrese la ecuacion de la derivada: '))
    pasos = int(input('Ingrese la cantidad de pasos a realizar: '))
    xinicial = float(input('Ingrese el valor en X inicial: '))
    yinicial = float(input('Ingrese el valor en Y inicial: '))
    xfinal = float(input('Ingrese el valor en X final: '))
    h = (xfinal - xinicial) / pasos

    matriz_solucion = []
    c1 = xinicial
    c2 = yinicial
    for a in range(pasos + 1):
        c3 = ec.subs(x, c1).subs(y, c2)
        c4 = c1 + (h/2)
        c5 = c2 + ((h/2) * c3)
        c6 = ec.subs(x, c4).subs(y, c5)
        c7 = c1 + (h/2)
        c8 = c2 + ((h/2) * c6)
        c9 = ec.subs(x, c7).subs(y, c8)
        c10 = c1 + h
        c11 = c2 + (h * c9)
        c12 = ec.subs(x, c10).subs(y, c11)
        c13 = c2 + ((h / 6) * (c3 + (2*c6) + (2*c9) + c12))

        if a == pasos:
            c3 = ''
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

        fila_temporal = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13]
        matriz_solucion.append(fila_temporal)
        c1 = c10
        c2 = c13

    return matriz_solucion