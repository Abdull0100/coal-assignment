class Register:

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self) -> str:
        return f"{self.name} = {self.value}"
    
    opcodes = {"mov": [100010, #100010dw oorrrmmm disp (reg,reg/mem,reg/reg,mem)
                       1100011,#1100011w oo000mmm disp data (mem,imm)
                       1011,   #1011wrrr data (reg,imm)
                       101000],#101000dw disp (mem,acc/acc,mem) 
                              
                              
                              
               "add": [000000, #000000dw oorrrmmm disp (reg,reg/reg,mem/mem,reg)
                       100000],#100000sw oo000mmm disp data (reg,imm/mem,imm/acc,imm) 
                                
               "dec": [1111111, #1111111w oo001mmm disp (reg8, mem)
                        01001], #01001rrr (reg16)
                               
               "inc": 1111111, #1111111w oo000mmm disp (reg8,mem,reg16)
               "neg": 1111011, #1111011w oo011mmm disp (reg, mem)
               "sub": [000101, #000101dw oorrrmmm disp (reg,reg/mem,reg/reg,mem)
                       100000, #100000sw oo101mmm disp data (reg,imm/mem,imm)
                       0010110]#0010110w data (acc,imm)
                
              }

def validater(instruction):
    global opCodes
    global registers

    reg_names = [reg.name for reg in registers]
    
    if instruction[0] not in opCodes:
        pass
    if instruction[0] in opCodes:
        if instruction[1] in reg_names:
            if instruction[2] in reg_names:
                print("Valid")