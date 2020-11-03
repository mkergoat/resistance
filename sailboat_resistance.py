# sailboat resistance via approximations
# ref: cours de conception de voiliers ENSTA Bretagne

import numpy as np
import matplotlib.pyplot as plt

# ship data
Lwl = 8 # roughly, m
Bwl = 2.5 # roughly, m
Tc = 1 #roughly, m
k = 0.05 # en premiere approximations, -

# Flow and environnement data
g = 9.81 #kg.m.s^-2
rho = 1025 #kg m^-3
nu = 1e-6 # USI
Vs = np.array([0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.25, 4.5, 4.75, 5, 5.5, 6]) * 0.5144 #m.s^-1
Re = Vs * Lwl / nu # -
Fn = Vs / pow(g * Lwl, 0.5) # - 

# RT list according to value of delta
nablas = rho * np.array([1, 1.5, 2, 2.5, 3]) / 1000 #kg
RT = []
Rw = []

# Approximation of wetted surface
Sw = 1.41 * Lwl * pow(pow(Bwl, 2) / 4 + pow(Tc, 2), 0.5) # m^2

# Viscous resistance
Cf = 0.075 / pow((np.log(Re) - 2), 2)
Rf = .5 * rho * Sw * pow(Vs, 2) * Cf
Rv = (1 + k) * Rf

# Wavemaking resistance
for i, nabla in enumerate(nablas):
    Rwi = rho * g * nabla * (0.02 * pow(Fn, 2) + 27 / ( pow(0.314 * Lwl / pow(nabla, 1/3), 9) + pow(Fn, -8)))
    Rw.append(Rwi)
    # Total resistance by Froude hypothesis
    RT.append(Rv + Rwi)

fig, ax = plt.subplots(1,1)
for i, nabla in enumerate(nablas):
    ax.plot(Vs / 0.5144, RT[i] / g, label = r"$\Delta = $ {} t".format(1000 * nabla / 1025))
ax.set_xlabel(r'$V$ [nd]')
ax.set_ylabel(r'$R_T$ [kg]')
ax.legend()
plt.savefig('resistance.svg', format='svg')
