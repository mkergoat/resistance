from collections import OrderedDict

import numpy as np

from holtrop_mennen import CF_ITTC57, Re

form_factors = OrderedDict()
form_factors["rudder_behind_skeg"] = [1.5, 2.0]
form_factors["rudder_behind_stern"] = [1.3, 1.5]
form_factors["twin_screw_balance_rudders"] = [2.8]
form_factors["shaft_brackets"] = [3.0]
form_factors["skeg"] = [1.5, 2.0]
form_factors["strut_bossings"] = [3.0]
form_factors["hull bossings"] = [2.0]
form_factors["shafts"] = [2.0, 4.0]
form_factors["stabilizer_fins"] = [2.8]
form_factors["dome"] = [2.7]
form_factors["bilge_keels"] = [1.4]

stern_coefficients = {'normal': 0, 'u_shape': -10, 'v_shape': 10}


class Part:
    def __init__(self):
        self._name = 'part'
        self._L = None
        self.weight = 0.0

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name


class Hull(Part):
    def __init__(self):
        Part.__init__(self)
        self._stern_shape = 'normal'
        self._Loa = 0.0
        self._Boa = 0.0
        self._D = 0.0
        self._Cm = 0
        self._Cb = 0
        self._Abt = 0
        self._Cwp = 0

    def computeWettedArea(self, Lwl, T, B):
        return Lwl * (2 * T + B) * np.sqrt(self._Cm) * (
                0.453 + 0.4425 * self._Cb - 0.20862 * self._Cm - 0.003467 * B / T + 0.3696 * self._Cwp) + 2.38 * self._Abt / self._Cb


class Appendage(Part):
    def __init__(self, name):
        Part.__init__(self)
        self.S = 0.0
        self.set_name(name)
        self._form_factor = form_factors[self.get_name()]

    def get_form_factor(self):
        return self._form_factor
