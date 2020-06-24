from sympy import *

x = Symbol('x')
y = Symbol('y')
f1 = 5*x + 2*y


print(f1.subs(x, 2).subs(y, 1))