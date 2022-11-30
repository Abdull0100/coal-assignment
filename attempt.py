class GeneralRegister():
    def __init__(self, name, value): #value should be taken as string
        self.name = name
        self.value = value
        self.contents = [x for x in self.value] #divides value and stores it into contents

    def __str__(self) -> str:
        return f"{self.name} = {self.value}"
    
class LowerRegister(GeneralRegister):
    def __init__(self, name, value):
        super().__init__(name, value)
        self.lower = self.contents[2:4]
        self.valstr = ''.join(self.lower)

    def __str__(self) -> str:
        return f"{self.name} = {self.valstr}"

class HigherRegister(GeneralRegister):
    def __init__(self, name, value):
        super().__init__(name, value)
        self.higher = self.contents[0:2]
        self.valstr = ''.join(self.higher)

    def __str__(self) -> str:
        return f"{self.name} = {self.valstr}"

class MachineCode():
	#codes is for opcodes, dw and mode are self explanatory
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
                       '1011',   #1011wrrr data (reg,imm)
                       '101000'],#101000dw disp (mem,acc/acc,mem) 
                              
                              
                              
               "add": ['000000', #000000dw oorrrmmm disp (reg,reg/reg,mem/mem,reg)
                       '100000'],#100000sw oo000mmm disp data (reg,imm/mem,imm/acc,imm) 
                                
               "dec": ['1111111', #1111111w oo001mmm disp (reg8, mem)
                        '01001'], #01001rrr (reg16)
                               
               "inc": '1111111', #1111111w oo000mmm disp (reg8,mem,reg16)
               "neg": '1111011', #1111011w oo011mmm disp (reg, mem)
               "sub": ['000101', #000101dw oorrrmmm disp (reg,reg/mem,reg/reg,mem)
                       '100000', #100000sw oo101mmm disp data (reg,imm/mem,imm)
                       '0010110'],#0010110w data (acc,imm)
               "cmp": ['001110', #001110dw oorrrmmm disp (reg,reg/mem,reg/reg,mem)
                       '100000', #100000sw oo111mmm disp data (reg,imm/mem,imm)
                       '0001111']#0001111w data (acc,imm)      
              }

inp1 = input("Enter the instruction: ")
inp2 = input("Enter the first register: ")
inp3 = input("Enter the second register: ")

if inp1.lower() in opcodes.keys():
	if inp2.lower() == "ax" and inp3.lower() = "bx":