from collections import OrderedDict

import numpy as np

from Part import Hull
from holtrop_mennen import CF_ITTC57, Re, makeDimensionnal


class Ship:
    def __init__(self):
        self._Lwl = None
        self._T = None
        self._LCB = None
        self._Cp = None
        self._B = None
        self._disp = None
        self.parts = OrderedDict()
        self.parts['hull'] = Hull()
        self.appendages = {k: v for k, v in self.parts.items() if k != 'Hull'}

    def set__Lwl(self, Lwl):
        self._Lwl = Lwl

    def set__T(self, T):
        self._T = T

    def set__LCB(self, LCB):
        self._LCB = LCB

    def set__Cp(self, Cp=None):
        self._Cp = Cp

    def set__B(self, B):
        self._B = B

    def set__disp(self, nabla):
        self._disp = nabla

    def compute_R_appendages(self, rho, V):
        S_all = np.sum([appendage.S for appname, appendage in self.appendages.items()])
        equiv_form_factor = np.sum(
            [appendage.S * appendage.get_form_factor() for appname, appendage in self.appendages.items()]) / S_all
        return makeDimensionnal(rho, V, S_all, CF_ITTC57(Re)) * equiv_form_factor
