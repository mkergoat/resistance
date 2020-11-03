from string import Template

ctr_file_template = Template(""""
;========================
; SHIP DATA
;========================
Lwl    = ; ship length at waterline
LOA    = ; ship overall length
Bwl    = ; ship beam at waterline
BOA    =
Ta     =
Tf     =
LCB    =
Cp     =
Cm     =
Cb     =

;=======
; PARTS
;=======
;-----------
; Bilge keels
; ----------
S = ;

;-----------
; Rudder
; ----------
type = ; 
S = ;

;-----------
; Skeg
; ----------
S = ;

""")


def read_ctr_file(ctr_file):
    f = open(ctr_file, 'r')