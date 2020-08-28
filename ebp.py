'''
    A collection of multiple calculation of related to Equilibrium Beach Profile (EBP) calculations

    ref: Coastal Processes with Engineering Applications - Dean and Dalrymple

    initial EBP, refer to page 171
    compare with results from amh-rlc hard drive - same timestep, whole profile, plot on same canvas
'''

import numpy as np

## Constants

# rho = 1000      # density of water
# g = 9.81
# f =             #

## Input parameters





## Solved wave parameters


# U_b = 3*sig*k*H**2 / (16*np.sinh(k*h))**2   # near-bottom velocity
# t_b = rho*f/8 * U_b * abs(U_b)      # mean shear stress




# EBP calc from AMH mathcad spreadsheet

# Determination of Ideal Slope for Beach Nourishment to have Type 4 Profile

H_0 = 1.2
T = 5.82
d = 1           # grain size in mm


def A(x):
    c = [-0.5604771955, 2.4081148505, -4.159592873, 3.774463172, -2.081258638, 0.7732330746, 0.0023618472]
    c = np.array(c)
    return c[0]*x**6 + c[1]*x**5 + c[2]*x**4 + c[3]*x**3 + c[4]*x**2 + c[5]*x + c[6]
# A = 0.067*w**0.44 where w is the fall velocity a f(d), d = sediment diameter

# w = sqrt(A**3 * g) / 7.5  # fall velocity


# Using the 1/3 power law disregarding effects of wave set-up

h_b = H_0*0.78  # breaking depth / depth to active zone

L = (h_b/A(d))**(3/2)       # width of active zone

y = np.arange(0,L,0.1)       # horizontal direction axis

h = -A(d)*y**(2/3)          # bed level from 0

import matplotlib.pyplot as plt

plt.plot(y,h)
plt.plot(y,np.zeros(len(h)),"r--")
plt.axes().set_aspect('equal')
xmin, xmax = [min(y), max(y)]
ymin, ymax = [min(h), max(h)+1]
plt.xlim(xmin, xmax)
plt.ylim(ymin, ymax)
plt.title("Profile")

plt.savefig("ebp.pdf")


# Calculate required slope for Advancing Type 4 profile

m_e = h_b/L         # effective / average slope of EBP
m_i = m_e*6/5       # required flatness of slope to achieve a type 4 profile

print(" ")
print("Effective / average slope of EBP: %20.3f" %m_e)
print("Required slope for a Type 4 - advancing profile: %.3f" %m_i)
