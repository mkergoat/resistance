form_factors = OrderedDict()
form_factor["rudder_behind_skeg"] = [1.5,2.0]
form_factor["rudder_behind_stern"] = [1.3,1.5]
form_factor["twin_screw_balance_rudders"] = [2.8]
form_factor["shaft_brackets"] = [3.0]
form_factor["skeg"] = [1.5, 2.0]

class Part:
	def __init__(self):
		self._name = 'appendage'
        self._L = None
		self.weight = 0.0
		
	def set_name(self, name):
		self._name = name
		
class Hull(Part):
	def __init__(self):
		Part.__init__(self)
		self._stern_shape = 'normal'
		self.LOA = 0.0
		self.BOA = 0.0
		self.D = 0.0
	
class Appendage(Part):
	def __init__(self):
		Part.__init__(self)
		self.S = 0.0
        self._form_factor = form_factors[self.name]
     
	
	