from newton import newton
import math

'''
Turn this into a function takes all wave parameters,
assumes g
then returns L
'''
g = 9.81

h = 10
T = 8

Lo = g*T**2/(2*math.pi)

f = lambda x: x*math.tanh(x) - (2*math.pi/T)**2 * h/g
Df =  lambda x: x/(math.cosh(x))**2 + math.tanh(x)
kh = newton(f,Df,Lo)

L = 2*math.pi/kh*h
print(L,Lo)
