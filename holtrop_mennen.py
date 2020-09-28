# -*- coding: utf-8 -*-

import numpy as np
from collections import OrderedDict

## HOLTROP - MENNEN SHIP RESISTANCE EVALUATION

def LCB_from_amidshipsoL(LCB, L):
    """
    Longitudinal center of buoyancy position measured from amidships as a 
    percentage of waterline length L
    """
    return (LCB - 0.5*L)/L

def LRoL(Cp, LCB, L):
    """
    Parameter used by the Holtrop approximation
    Cp : prismatic coefficient
    LCB: longitudinal position of the center of buoyancy
    """
    return 1 - Cp + 0.06 * Cp * LCB_from_amidshipsoL(LCB, L) * (4 * Cp - 1)

def hull_form_factor(T, L, B, LCB, Cp, C_stern):
    """
    Computes the hull form factor
    B: ship max width
    LCB: longitudinal position of center of buoyancy
    Cp: Prismatic coefficient
    T: average moulded draft
    """
    LCB_midoL = LCB_from_amidshipsoL(LCB,L)
    LR = L * LRoL(Cp, LCB_midoL)
    if T/L > 0.05:
        c12 = (T/L)**0.2228446
    elif T/L < 0.02:
        c12 = 0.479948
    else:
        c12 = 48.20 * ((T / L) - 0.02) ** 2.078 + 0.479948
    c13 = 1 + 0.003 * C_stern
    
    return c13 * (0.93 + c12 * (B / LR) ** 0.92497 * (0.95 - Cp)**(-0.521448) * (1 - Cp + 0.0225 * LCB_midoL)**(0.6906))

def Re(V,L,rho,mu):
    """
    Computes the Reynolds number for the flow
    around the ship or element
    V: reference velocity
    L: reference length
    rho: fluid density
    """
    return rho * V * L / mu

def CF_ITTC57(Re):
    """
    Skin friction coefficient computed
    using ITTC 57 Friction Line Formula
    """
    return 0.075/(np.log(Re()) - 2)^2

def makeDimensionnal(rho, V, S, C):
    """
    Transforms a non-dimensionnal coefficient into a dimensionnal one
    """
    return 0.5 * rho * V**2 * S * C



#RT = RF * (1+k1) + RAPP + RW + RB + RTR + RA
