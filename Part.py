form_factors = OrderedDict()
form_factor["rudder_behind_skeg"] = [1.5,2.0]
form_factor["rudder_behind_stern"] = [1.3,1.5]
form_factor["twin_screw_balance_rudders"] = [2.8]
form_factor["shaft_brackets"] = [3.0]
form_factor["skeg"] = [1.5, 2.0]
form_factor["strut_bossings"] = [3.0]
form_factor["hull bossings"] = [2.0]
form_factor["shafts"] = [2.0, 4.0]
form_factor["stabilizer_fins"] = [2.8]
form_factor["dome"] = [2.7]
form_factor["bilge_keels"] = [1.4]

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
        self.CM = 0
        self.CB = 0
        self.ABT = 0
        self.C_WP
        
        
        
    def computeWettedArea(self):
        return 'to do'
        
class Appendage(Part):
	def __init__(self):
		Part.__init__(self)
		self.S = 0.0
        self._form_factor = form_factors[self.name]
     
	
	