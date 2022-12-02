class GeneralRegister():
    def __init__(self, name, value, regcode): #value should be taken as string
        self.name = name
        self.value = value
        self.regcode = regcode
    
    def getvalue(self): #getter function for contents (string)
        return self.value
    
    def getregcode(self): #getter function for register code (string)
        return self.code

    def __str__(self) -> str: #prints out name and value
        return f"{self.name} = {self.value}"

class LowerRegister(GeneralRegister):
    def __init__(self, name, value, regcode):
        super().__init__(name, value, regcode)
        #self.name = name
        #self.value = value
        #self.regcode = regcode

class HigherRegister(GeneralRegister):
    def __init__(self, name, value, regcode):
        super().__init__(name, value, regcode)
        #self.name = name
        #self.value = value
        #self.regcode = regcode

class DividableRegister(GeneralRegister):
    #constructor for dividable 16-bit registers (ax,bx,cx,dx)
    def __init__(self, name, value, regcode):
        super().__init__(name, value, regcode)
        self.lower = LowerRegister(self.name[0]+'L', self.value[2:4], self.regcode)
        self.higher = HigherRegister(self.name[0]+'H', self.value[0:2], '1' + self.regcode[1:3])
        #self.value = self.higher.value + self.lower.value
    
    #sets the values of lower and higher after operations on 16-bit register
    def update(self):
        self.value = self.higher.value + self.lower.value
        self.lower = LowerRegister(self.name[0]+'L', self.value[2:4], self.regcode)
        self.higher = HigherRegister(self.name[0]+'H', self.value[0:2], self.regcode)

    #getter function for lower 8-bits of register as string
    def getlowerstr(self):
        return ''.join(self.lower)
    
    #getter function for higher 8-bits of register as string
    def gethigherstr(self):
        return ''.join(self.higher)




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

AX = DividableRegister("AX", '1234', '000')
CX = DividableRegister("CX", '0000', '001')
DX = DividableRegister("DX", '0000', '010')
BX = DividableRegister("BX", '5678', '011')
SP = GeneralRegister("SP", '0000', '100')
BP = GeneralRegister("BP", '0000', '101')
SI = GeneralRegister("SI", '0000', '110')
DI = GeneralRegister("DI", '0000', '111')

AL = AX.lower
CL = CX.lower
DL = LowerRegister("DL", '00', '010')
BL = LowerRegister("BL", '00', '011')

AH = HigherRegister("AH", '00', '100')
CH = HigherRegister("CH", '00', '101')
DH = HigherRegister("DH", '00', '110')
BH = HigherRegister("BH", '00', '111')


fullregisters = {'ax':AX, 'bx':BX, 'cx':CX, 'dx':DX, 'sp':SP, 'bp':BP, 'si':SI, 'di':DI} #16-bit registers
lowerregisters = {'al':AL, 'bl':BL, 'cl':CL, 'dl':DL} #lower 8-bit registers
higherregisters = {'ah':AH, 'bh':BH, 'ch':CH, 'dh':DH} #higher 8-bit registers
halfregisters = {'al':AL, 'bl':BL, 'cl':CL, 'dl':DL, 'ah':AH, 'bh':BH, 'ch':CH, 'dh':DH}

inp1 = input("Enter the instruction: ").lower()
inp2 = input("Enter the first operand: ").lower()
inp3 = input("Enter the second operand: ").lower()

if inp1 in opcodes.keys():
    if inp1 == "mov":
        #16-bit reg addressing
        if inp2 in fullregisters and inp3 in fullregisters:
            fullregisters[inp2].value = fullregisters[inp3].value

            x = MachineCode('100010', '1', '1', '11',fullregisters[inp2].regcode, fullregisters[inp3].regcode)
            #x.display()
        
        #8-bit reg addressing
        #if inp2 in halfregisters and inp3 in halfregisters:
        #    halfregisters[inp2].value = halfregisters[inp3].value

print(AX.value)
print(AL.value)
AL.value = '12'
AX.update()

print(AX.value)
