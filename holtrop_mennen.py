import numpy as np
from collections import OrderedDict

## HOLTROP - MENNEN SHIP RESISTANCE EVALUATION


class Ship:
    def __init__(self):
        self._Lwl = None
        self._T = None
        self._LCB = None
        self._Cp = None

def LRoL():
    return 1 - Cp + 0.06 * Cp * LCB * (4 * Cp - 1)

def hull_form_factor()
    """
    Computes the hull form factor
    """
    return c13 * (0.93 + c12 * (B / LR)**0.92497 * (0.95 - Cp)**(-0.521448) * (1 - Cp + 0.0225 * LCB)**(0.6906))

def Re()
    return rho * V * L / mu

def CF_ITTC57()
    return 0.075/(np.log(Re()) - 2)^2

def RF():
    return 0.5 * rho * V**2 * S * CF



RT = RF * (1+k1) + RAPP + RW + RB + RTR + RA
