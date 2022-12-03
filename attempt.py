#class GeneralRegister():
#    def __init__(self, name, value, regcode): #value should be taken as string
#        self.name = name
#        self.value = value
#        self.regcode = regcode
#    
#    def getvalue(self): #getter function for contents (string)
#        return self.value
#    
#    def getregcode(self): #getter function for register code (string)
#        return self.code
#
#    def __str__(self) -> str: #prints out name and value
#        return f"{self.name} = {self.value}"
#
#class LowerRegister(GeneralRegister):
#    def __init__(self, name, value, regcode):
#        super().__init__(name, value, regcode)
#        #self.name = name
#        #self.value = value
#        #self.regcode = regcode
#
#class HigherRegister(GeneralRegister):
#    def __init__(self, name, value, regcode):
#        super().__init__(name, value, regcode)
#        #self.name = name
#        #self.value = value
#        #self.regcode = regcode
#
#class DividableRegister(GeneralRegister):
#    #constructor for dividable 16-bit registers (ax,bx,cx,dx)
#    def __init__(self, name, value, regcode):
#        super().__init__(name, value, regcode)
#        self.lower = LowerRegister(self.name[0]+'L', self.value[2:4], self.regcode)
#        self.higher = HigherRegister(self.name[0]+'H', self.value[0:2], '1' + self.regcode[1:3])
#        #self.value = self.higher.value + self.lower.value
#    
#    #sets the values of lower and higher after operations on 16-bit register
#    def update(self):
#        self.value = self.higher.value + self.lower.value
#        self.lower = LowerRegister(self.name[0]+'L', self.value[2:4], self.regcode)
#        self.higher = HigherRegister(self.name[0]+'H', self.value[0:2], self.regcode)
#
#    #getter function for lower 8-bits of register as string
#    def getlowerstr(self):
#        return ''.join(self.lower)
#    
#    #getter function for higher 8-bits of register as string
#    def gethigherstr(self):
#        return ''.join(self.higher)
#

class MachineCode():
	#codes is for opcodes, dw and mode are self explanatory
    #all arguments are strings, easier to manipulate
    def __init__(self, code, d, w, mode, rrr, mmm):
        self.code = code
        self.d = d
        self.w = w
        self.mode = mode
        self.rrr = rrr
        self.mmm = mmm

    def display(self):
        print(f"First Byte:{self.code}{self.d}{self.w}")
        print(f"Second Byte:{self.mode}{self.rrr}{self.mmm}")
        print(f"Opcode:{self.code}")
        print(f"D:{self.d}")
        print(f"W:{self.w}")
        print(f"MOD:{self.mode}")
        print(f"REG:{self.rrr}")
        print(f"R/M:{self.mmm}")

class Processor():
    opcodes =       {"mov": ['100010', #100010dw oorrrmmm disp (reg,reg/mem,reg/reg,mem)
                       '1100011',#1100011w oo000mmm disp data (mem,imm)
                       '1011'],   #1011wrrr data (reg,imm) 
                              
                              
                              
               "add": ['000000', #000000dw oorrrmmm disp (reg,reg/reg,mem/mem,reg)
                       '100000'],#100000sw oo000mmm disp data (reg,imm/mem,imm/acc,imm) 
                                
               "dec": ['1111111', #1111111w oo001mmm disp (reg8, mem)
                        '01001'], #01001rrr (reg16)
                               
               "inc": '1111111', #1111111w oo000mmm disp (reg8,mem,reg16)
               "neg": '1111011', #1111011w oo011mmm disp (reg, mem)
               "sub": ['000101', #000101dw oorrrmmm disp (reg,reg/mem,reg/reg,mem)
                       '100000'], #100000sw oo101mmm disp data (reg,imm/mem,imm),
               "cmp": ['001110', #001110dw oorrrmmm disp (reg,reg/mem,reg/reg,mem)
                       '100000'] #100000sw oo111mmm disp data (reg,imm/mem,imm)     
              }
    ax = ['0'] * 4
    def __getax__(self):
        return self.AH[0] + self.AL[0]
    
    def __setax__(self, list1):
        self.ax = list1
        self.AL[0] = self.ax[0][2:4]
        self.AH[0] = self.ax[0][0:2]

    bx = ['0'] * 4
    def __getbx__(self):
        return self.BH[0] + self.BL[0]
    
    def __setbx__(self, list1):
        self.bx = list1
        self.BL[0] = self.bx[0][2:4]
        self.BH[0] = self.bx[0][0:2]
    
    cx = ['0'] * 4
    def __getcx__(self):
        return self.CH[0] + self.CL[0]
    
    def __setcx__(self, list1):
        self.cx = list1
        self.CL[0] = self.cx[0][2:4]
        self.CH[0] = self.cx[0][0:2]
    
    dx = ['0'] * 4
    def __getdx__(self):
        return self.DH[0] + self.DL[0]
    
    def __setdx__(self, list1):
        self.dx = list1
        self.DL[0] = self.dx[0][2:4]
        self.DH[0] = self.dx[0][0:2]

        
    AX = property(fget=__getax__, fset=__setax__, fdel=None, doc=None)
    CX = property(fget=__getcx__, fset=__setcx__, fdel=None, doc=None)
    DX = property(fget=__getdx__, fset=__setdx__, fdel=None, doc=None)
    BX = property(fget=__getbx__, fset=__setbx__, fdel=None, doc=None)
    SP = [['0'] * 4, '100']
    BP = [['0'] * 4, '101']
    SI = [['0'] * 4, '110']
    DI = [['0'] * 4, '111']

    AL = [ax[0][2:4], '000']
    CL = [cx[0][2:4], '001']
    DL = [dx[0][2:4], '010']
    BL = [bx[0][2:4], '011']

    AH = [ax[0][0:2], '100']
    CH = [cx[0][0:2], '101']
    DH = [dx[0][0:2], '110']
    BH = [bx[0][0:2], '111']


    fullregisters = {'ax':[AX,'000'], 'bx':[BX,'011'], 'cx':[CX,'001'], 'dx':[DX,'010'], 'sp':[SP,'100'], 'bp':[BP,'101'], 'si':[SI,'110'], 'di':[DI,'111']} #16-bit registers   
    halfregisters = {'al':[AL,'000'], 'bl':[BL,'011'], 'cl':[CL,'001'], 'dl':[DL,'010'], 'ah':[AH,'100'], 'bh':[BH,'101'], 'ch':[CH,'110'], 'dh':[DH,'111']} #8-bit registers

    def procinput(self):
        inp1 = input("Enter the instruction: ").lower()
        if inp1 in self.opcodes.keys():
            inp2 = input("Enter the first operand: ").lower()
            inp3 = input("Enter the second operand: ").lower()
            if inp1 == "mov":
                #16-bit reg addressing
                if inp2 in self.fullregisters and inp3 in self.fullregisters:
                    self.fullregisters[inp2][0].fset(self, self.fullregisters[inp3][0].fget(self))
                    x = MachineCode('100010', '1', '1', '11',self.fullregisters[inp2][1], self.fullregisters[inp3][1])
                    x.display()
               
                #8-bit reg addressing
                if inp2 in self.halfregisters and inp3 in self.halfregisters:
                    self.halfregisters[inp2][0][0][::] = self.halfregisters[inp3][0][0][::]
                    x = MachineCode('100010', '1', '0', '11',self.halfregisters[inp2][1], self.halfregisters[inp3][1])
                    x.display()

proc = Processor()
proc.AX = ['1','2','3','4']
proc.BX = ['5','6','7','8']
proc.procinput()

print(proc.AH)
print(proc.BH)
print(proc.AX)
print(proc.BX)




