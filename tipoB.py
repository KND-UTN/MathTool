from sympy import *


def euler():
    pass


def euler_mejorado():
    x = Symbol('x')
    y = Symbol('y')
    z = Symbol('z')
    ecy = eval(input('Ingrese la ecuacion derivada de y: '))
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
        c4 = ecy.subs(x, c1).subs(y, c2).subs(z, c3)
        c5 = ecz.subs(x, c1).subs(y, c2).subs(z, c3)
        c6 = c1 + h
        c7 = c2 + (h * c4)
        c8 = c3 + (h * c5)
        c9 = ecy.subs(x, c6).subs(y, c7).subs(z, c8)
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

    return matriz_solucion


def runge_kutta():
    pass
