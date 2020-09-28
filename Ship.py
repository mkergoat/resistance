class Ship:
    def __init__(self):
        self._Lwl = None
        self._T = None
        self._LCB = None
        self._Cp = None
        self._B = None
        self._disp = None
        self.parts = OrderedDict()

    def set__Lwl(self, Lwl):
        self._Lwl = Lwl
        
    def set__T(self, T):
        self._T = T
    
    def set__LCB(self, LCB):
        self._LCB = LCB
    
    def set__Cp(self, Cp = None):
        self._Cp = Cp
 
    def set__B(self, B):
        self._B = B

    def set__disp(self, nabla):
        self._disp = nabla
