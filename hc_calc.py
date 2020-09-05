'''
	depth of closure h_c calculator

	based on Hallermeier 1978
'''


import matplotlib.pyplot as plt
import numpy as np

# assumed from example
r = 1000 #seawater mass density, can be 1030
rs = 2650 #sediment mass density

g = 9.81 # acc due to gravity
H0 = 0.5 # deep water wave height
T = 8 # wave period
L0 = g*T**2/(2*np.pi())

 

'''
    h.c Solver
'''

def dr_solve(h,T):
    g = 9.81
    tol=10**-6
    kh0 = 1.0
    g0 = kh0*np.tanh(kh0) - (2*np.pi/T)**2*h/g
    g0p = kh0*(1-np.tanh(kh0)**2) + np.tanh(kh0)

    i = 0

    while i<10000:
        kh1 = kh0 - g0/g0p
        g1 = kh1*np.tanh(kh1) - (2*np.pi/T)**2*h/g
        g1p = kh1*(1-np.tanh(kh1)**2) + np.tanh(kh1)

        i+=1

        if abs(kh0-kh1)>tol:
            kh0=kh1
            g0=g1
            g0p=g1p
        else :
            return 2*np.pi/(kh0/h)
        #    if i=10000:
        # in case of error : counter measure