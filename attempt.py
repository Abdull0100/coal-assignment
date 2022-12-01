class GeneralRegister():
    def __init__(self, name, value): #value should be taken as string
        self.name = name
        self.value = value
    
    def getvalue(self): #getter function for contents (list)
        return self.value

    def __str__(self) -> str: #prints out name and value
        return f"{self.name} = {self.value}"
    
class DividableRegister(GeneralRegister):
    #constructor for dividable 16-bit registers (ax,bx,cx,dx)
    def __init__(self, name, value):
        super().__init__(name, value)
        self.lower = self.value[2:4]
        self.higher = self.value[0:2]
    
    #sets the values of lower and higher after operations on 16-bit register
    def update(self):
        self.lower = self.value[2:4]
        self.higher = self.value[0:2]

    #getter function for lower 8-bits of register (list)
    def getlower(self):
        return self.lower
    
    #getter function for higher 8-bits of register (list)
    def gethigher(self):
        return self.higher

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
	#def __str__(self) -> str:
	#	return f"{self.code}{self.d}{self.w}{self.mode}{self.rrr}{self.mmm}"


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

AX = DividableRegister("AX", '1234')
BX = DividableRegister("BX", '5678')
CX = DividableRegister("CX", '0000')
DX = DividableRegister("DX", '0000')
SP = GeneralRegister("SP", '0000')
BP = GeneralRegister("BP", '0000')
SI = GeneralRegister("SI", '0000')
DI = GeneralRegister("DI", '0000')

fullregisters = {'ax':AX, 'bx':BX, 'cx':CX, 'dx':DX, 'sp':SP, 'bp':BP, 'si':SI, 'di':DI} #16-bit registers
lowerregisters = ['al', 'bl', 'cl', 'dl'] #lower 8-bit registers
higherregisters = ['ah', 'bh', 'ch', 'dh'] #higher 8-bit registers

inp1 = input("Enter the instruction: ")
inp2 = input("Enter the first operand: ")
inp3 = input("Enter the second operand: ")

if inp1.lower() in opcodes.keys():
    if inp1.lower() == "mov":
        #16-bit reg addressing
        if inp2.lower() in fullregisters and inp3.lower() in fullregisters:
            fullregisters[inp2.lower()].value = fullregisters[inp3.lower()].value
            fullregisters[inp2.lower()].update()
        
        #if inp2.lower() in lowerregisters or inp2.lower() in higherregisters

        
print(AX.__str__())
print(BX.__str__())
print(AX.gethigherstr())
