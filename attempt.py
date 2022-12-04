import copy
import math

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
        print("Machine code Generated: ")
        print(f"First Byte:{self.code}{self.d}{self.w}", end=' ')
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
        return self.AH + self.AL
    
    def __setax__(self, list1):
        if len(list1) <= 4:
            for i in range(len(self.ax)-1, len(self.ax) - len(list1) - 1, -1):
                self.ax[i] = list1[i-(len(self.ax) - len(list1))]
        else:
            print("Wrong setter to register")

        self.AL = self.ax[2:4]
        self.AH = self.ax[0:2]

    bx = ['0'] * 4
    def __getbx__(self):
        return self.BH + self.BL
    
    def __setbx__(self, list1):
        if len(list1) <= 4:
            for i in range(len(self.bx)-1, len(self.bx) - len(list1) - 1, -1):
                self.bx[i] = list1[i-(len(self.bx) - len(list1))]
        else:
            print("Wrong setter to register")

        self.BL = self.bx[2:4]
        self.BH = self.bx[0:2]
    
    cx = ['0'] * 4
    def __getcx__(self):
        return self.CH + self.CL
    
    def __setcx__(self, list1):
        if len(list1) <= 4:
            for i in range(len(self.cx)-1, len(self.cx) - len(list1) - 1, -1):
                self.cx[i] = list1[i-(len(self.cx) - len(list1))]
        else:
            print("Wrong setter to register")

        self.CL = self.cx[2:4]
        self.CH = self.cx[0:2]
    
    dx = ['0'] * 4
    def __getdx__(self):
        return self.DH + self.DL
    
    def __setdx__(self, list1):
        if len(list1) <= 4:
            for i in range(len(self.dx)-1, len(self.dx) - len(list1) - 1, -1):
                self.dx[i] = list1[i-(len(self.dx) - len(list1))]
        else:
            print("Wrong setter to register")

        self.DL = self.dx[2:4]
        self.DH = self.dx[0:2]

    sp = ['0'] * 4
    def __getsp__(self):
        return self.sp
    def __setsp__(self, list1):
        if len(list1) <= 4:
            for i in range(len(self.sp)-1, len(self.sp) - len(list1) - 1, -1):
                self.sp[i] = list1[i-(len(self.sp) - len(list1))]
        else:
            print("Wrong setter to register")

    bp = ['0'] * 4
    def __getbp__(self):
        return self.bp
    def __setbp__(self, list1):
        if len(list1) <= 4:
            for i in range(len(self.bp)-1, len(self.bp) - len(list1) - 1, -1):
                self.bp[i] = list1[i-(len(self.bp) - len(list1))]
        else:
            print("Wrong setter to register")

    si = ['0'] * 4
    def __getsi__(self):
        return self.si
    def __setsi__(self, list1):
        if len(list1) <= 4:
            for i in range(len(self.si)-1, len(self.si) - len(list1) - 1, -1):
                self.si[i] = list1[i-(len(self.si) - len(list1))]
        else:
            print("Wrong setter to register")
    
    di = ['0'] * 4
    def __getdi__(self):
        return self.di
    def __setdi__(self, list1):
        if len(list1) <= 4:
            for i in range(len(self.di)-1, len(self.di) - len(list1) - 1, -1):
                self.di[i] = list1[i-(len(self.di) - len(list1))]
        else:
            print("Wrong setter to register")
    
    al = ax[2:4]
    def __getal__(self):
        return self.al
    def __setal__(self, list1):
        if len(list1) <= 4:
            for i in range(len(self.al)-1, len(self.al) - len(list1) - 1, -1):
                self.al[i] = list1[i-(len(self.al) - len(list1))]
        else:
            print("Wrong setter to register")

    bl = bx[2:4]
    def __getbl__(self):
        return self.bl
    def __setbl__(self, list1):
        if len(list1) <= 4:
            for i in range(len(self.bl)-1, len(self.bl) - len(list1) - 1, -1):
                self.bl[i] = list1[i-(len(self.bl) - len(list1))]
        else:
            print("Wrong setter to register")

    cl = cx[2:4]
    def __getcl__(self):
        return self.cl
    def __setcl__(self, list1):
        if len(list1) <= 4:
            for i in range(len(self.cl)-1, len(self.cl) - len(list1) - 1, -1):
                self.cl[i] = list1[i-(len(self.cl) - len(list1))]
        else:
            print("Wrong setter to register")

    dl = dx[2:4]
    def __getdl__(self):
        return self.dl
    def __setdl__(self, list1):
        if len(list1) <= 4:
            for i in range(len(self.dl)-1, len(self.dl) - len(list1) - 1, -1):
                self.dl[i] = list1[i-(len(self.dl) - len(list1))]
        else:
            print("Wrong setter to register")

    ah = ax[0:2]
    def __getah__(self):
        return self.ah
    def __setah__(self, list1):
        if len(list1) <= 4:
            for i in range(len(self.ah)-1, len(self.ah) - len(list1) - 1, -1):
                self.ah[i] = list1[i-(len(self.ah) - len(list1))]
        else:
            print("Wrong setter to register")
    
    bh = bx[0:2]
    def __getbh__(self):
        return self.bh
    def __setbh__(self, list1):
        if len(list1) <= 4:
            for i in range(len(self.bh)-1, len(self.bh) - len(list1) - 1, -1):
                self.bh[i] = list1[i-(len(self.bh) - len(list1))]
        else:
            print("Wrong setter to register")

    ch = cx[0:2]
    def __getch__(self):
        return self.ch
    def __setch__(self, list1):
        if len(list1) <= 4:
            for i in range(len(self.ch)-1, len(self.ch) - len(list1) - 1, -1):
                self.ch[i] = list1[i-(len(self.ch) - len(list1))]
        else:
            print("Wrong setter to register")
    
    dh = dx[0:2]
    def __getdh__(self):
        return self.dh
    def __setdh__(self, list1):
        if len(list1) <= 4:
            for i in range(len(self.dh)-1, len(self.dh) - len(list1) - 1, -1):
                self.dh[i] = list1[i-(len(self.dh) - len(list1))]
        else:
            print("Wrong setter to register")

    #made registers into properties for easy access

    AX = property(fget=__getax__, fset=__setax__, fdel=None, doc=None)
    CX = property(fget=__getcx__, fset=__setcx__, fdel=None, doc=None)
    DX = property(fget=__getdx__, fset=__setdx__, fdel=None, doc=None)
    BX = property(fget=__getbx__, fset=__setbx__, fdel=None, doc=None)

    SP = property(fget=__getsp__, fset=__setsp__, fdel=None, doc=None)
    BP = property(fget=__getbp__, fset=__setbp__, fdel=None, doc=None)
    SI = property(fget=__getsi__, fset=__setsi__, fdel=None, doc=None)
    DI = property(fget=__getdi__, fset=__setdi__, fdel=None, doc=None)

    AL = property(fget=__getal__, fset=__setal__, fdel=None, doc=None)
    CL = property(fget=__getcl__, fset=__setcl__, fdel=None, doc=None)
    DL = property(fget=__getdl__, fset=__setdl__, fdel=None, doc=None)
    BL = property(fget=__getbl__, fset=__setbl__, fdel=None, doc=None)

    AH = property(fget=__getah__, fset=__setah__, fdel=None, doc=None)
    CH = property(fget=__getch__, fset=__setch__, fdel=None, doc=None)
    DH = property(fget=__getdh__, fset=__setdh__, fdel=None, doc=None)
    BH = property(fget=__getbh__, fset=__setbh__, fdel=None, doc=None)

    #registers AX,BX,CX,DX,SP,BP,SI,DI 
    fullregisters = {'ax':[AX,'000'], 'bx':[BX,'011'], 'cx':[CX,'001'], 'dx':[DX,'010'],
                    'sp':[SP,'100'], 'bp':[BP,'101'], 'si':[SI,'110'], 'di':[DI,'111']}
    #lower and upper variants of registers AX,BX,CX,DX
    halfregisters = {'al':[AL,'000'], 'bl':[BL,'011'], 'cl':[CL,'001'], 'dl':[DL,'010'],
                     'ah':[AH,'100'], 'bh':[BH,'101'], 'ch':[CH,'110'], 'dh':[DH,'111']}
                    
    memory = {'0':'1234', '1':'0000', '2':'0002', '3':'0000', '4':'0000', '5':'0000', '6':'0000',
              '7':'0000', '8':'0000', '9':'0000', 'A':'0000', 'B':'0000', 'C':'0000', 'D':'0000',
              'E':'0000', 'F':'0000'}

    def prevComplement(self,n, b) :
        maxNum, digits, num = 0, 0, n
        while n > 1:
            digits += 1
            n = n // 10
        maxDigit = b - 1
        while digits :
            maxNum = maxNum * 10 + maxDigit
            digits -= 1
        return maxNum - num

    def complement(self,n, b) :
        return self.prevComplement(n, b) + 1


    #method for the processor to take instruction input from the user
    def procinput(self):
        while True:
            inp1 = input("Enter the instruction: ").lower()
            if inp1 == 'exit':
                break
            elif inp1 in self.opcodes.keys():
                if inp1 == "mov":
                    mode = input("Choose an addressing mode:\n\
1: Register to Register\n\
2: Immediate to Register\n\
3: Memory to Register\n\
4: Register to Memory\n")
                    inp2 = input("Enter the first operand: ").lower()
                    inp3 = input("Enter the second operand: ").lower()

                    if mode == "1":
                        #16-bit reg-reg addressing (mov)
                        #AX,BX,CX,DX,SP,BP,SI,DI
                        if inp2 in self.fullregisters.keys() and inp3 in self.fullregisters.keys():
                            self.fullregisters[inp2][0].fset(self, self.fullregisters[inp3][0].fget(self))
                            x = MachineCode('100010', '1', '1', '11',
                                self.fullregisters[inp2][1], self.fullregisters[inp3][1])
                            x.display()
                       
                        #8-bit reg-reg addressing (mov)
                        #AH,AL,BH,BL,CH,CL,DH,DL
                        elif inp2 in self.halfregisters.keys() and inp3 in self.halfregisters.keys():
                            self.halfregisters[inp2][0].fset(self, self.halfregisters[inp3][0].fget(self))
                            x = MachineCode('100010', '1', '0', '11',
                                        self.halfregisters[inp2][1], self.halfregisters[inp3][1])
                            x.display()
                        else:
                            print("Invalid instruction operands")
                            print()

                    elif mode == '2':
                        #imm is only done for hex nums
                        #16-bit reg-imm addressing (mov)
                        if inp2 in self.fullregisters.keys() and inp3.isalnum():
                            #extracts the hex number
                            hexnum = copy.deepcopy(inp3)
                            hexnum = list(str(hex(int(hexnum, base = 16)))[2:])
                            #each case of the hex value moving into ax,bx,cx,dx
                            if len(hexnum) <= 4:
                                self.fullregisters[inp2][0].fset(self, hexnum)
                                #insert machine code
                            else:
                                print("Invalid sized value")
                                print()

                        #8-bit reg-imm addressing (mov)
                        elif inp2 in self.halfregisters.keys() and inp3.isalnum():
                            #extracts the hex number
                            hexnum = copy.deepcopy(inp3)
                            hexnum = list(str(hex(int(hexnum, base = 16)))[2:])
                            #each case of the hex value moving into lower and higher registers                        
                            if len(hexnum) <= 2:
                                self.halfregisters[inp2][0].fset(self,hexnum)
                                #insert machine code
                            else:
                                print("Invalid sized value")
                                print()
                        else:
                            print("Invalid instruction operands")
                            print()
                    elif mode == '3':
                        #16-bit reg-mem addressing (mov)
                        if inp2 in self.fullregisters.keys() and inp3[1] in self.memory.keys():
                            self.fullregisters[inp2][0].fset(self, list(self.memory[inp3[1]]))
                            #insert machine code
                        #8-bit reg-mem addressing (mov)
                        elif inp2 in self.halfregisters.keys() and inp3[1] in self.memory.keys():
                            self.halfregisters[inp2][0].fset(self, list(self.memory[inp3[1]]))
                            #insert machine code
                        
                        else:
                            print("Invalid instruction operands")
                            print()

                    elif mode == '4':
                        #16-bit mem-reg addressing (mov)
                        if inp2[1] in self.memory.keys() and inp3 in self.fullregisters.keys():
                            self.memory[inp2[1]] = ''.join(self.fullregisters[inp3][0].fget(self))
                            #insert machine code
                        
                        #8-bit mem-reg addressing (mov)
                        elif inp2[1] in self.memory.keys() and inp3 in self.halfregisters.keys():
                            self.memory[inp2[1]] = ''.join(self.halfregisters[inp3][0].fget(self))
                            #insert machine code
                       
                        else:
                            print("Invalid instruction operands")
                            print()
                    else:
                        print("Invalid mode input")
                        print()

                elif inp1 == "add":
                    mode = input("Choose an addressing mode:\n\
1: Register to Register\n\
2: Immediate to Register\n\
3: Memory to Register\n\
4: Register to Memory\n")
                    inp2 = input("Enter the first operand: ").lower()
                    inp3 = input("Enter the second operand: ").lower()
                    if mode == '1':
                        #16-bit reg-reg addressing (add)
                        if inp2 in self.fullregisters.keys() and inp3 in self.fullregisters.keys():
                            num2 = int(''.join(self.fullregisters[inp2][0].fget(self)), base=16)
                            num3 = int(''.join(self.fullregisters[inp3][0].fget(self)), base=16)
                            sum = list(hex(num2+num3)[2:])
                            if len(sum) > 4:
                                print("Value too big to fit into register")
                                print()
                            else:   
                                self.fullregisters[inp2][0].fset(self, sum)
                            #insert machine code
                        
                        #8-bit reg-reg addressing (add)
                        elif inp2 in self.halfregisters.keys() and inp3 in self.halfregisters.keys():
                            hexnum2 = int(''.join(self.halfregisters[inp2][0].fget(self)), base=16)
                            hexnum3 = int(''.join(self.halfregisters[inp3][0].fget(self)), base=16)
                            sum = list(hex(hexnum2+hexnum3)[2:])
                            if len(sum) > 2:
                                print("Value too big to fit into register")
                                print()
                            else:   
                                self.halfregisters[inp2][0].fset(self, sum)
                            #insert machine code
                        else:
                            print("Invalid instruction operands")
                            print()
                    
                    elif mode == "2":
                        #16-bit reg-reg addressing (add)
                        if inp2 in self.fullregisters.keys() and inp3.isalnum():
                            #extracts the hex number
                            hexnum = copy.deepcopy(inp3)
                            hexnum = int(hexnum, base=16)
                            hexnum2 = int(''.join(self.fullregisters[inp2][0].fget(self)), base=16)
                            sum = list(hex(hexnum+hexnum2)[2:])
                            if len(sum) <= 4:
                                self.fullregisters[inp2][0].fset(self, sum)
                                #insert machine code
                            else:
                                print("Invalid sized value")
                                print()

                        #8-bit reg-reg addressing (add)
                        if inp2 in self.halfregisters.keys() and inp3.isalnum():
                            #extracts the hex number
                            hexnum = copy.deepcopy(inp3)
                            hexnum = int(hexnum, base=16)
                            hexnum2 = int(''.join(self.halfregisters[inp2][0].fget(self)), base=16)
                            sum = list(hex(hexnum+hexnum2)[2:])
                            if len(sum) <= 2:
                                self.halfregisters[inp2][0].fset(self, sum)
                                #insert machine code
                            else:
                                print("Invalid sized value")
                                print()
                        
                    elif mode == '3':
                        #16-bit reg-mem addressing (add)
                        if inp2 in self.fullregisters.keys() and inp3[1] in self.memory.keys():
                            hexnum2 = int(self.memory[inp3[1]], base=16)
                            hexnum = int(''.join(self.fullregisters[inp2][0].fget(self)), base=16)
                            sum = list(hex(hexnum+hexnum2)[2:])
                            if len(sum) > 4:
                                print("Value too big to be loaded into register")
                            else:
                                self.fullregisters[inp2][0].fset(self, sum)
                            #insert machine code
                        #8-bit reg-mem addressing (add)
                        elif inp2 in self.halfregisters.keys() and inp3[1] in self.memory.keys():
                            hexnum2 = int(self.memory[inp3[1]], base=16)
                            hexnum = int(''.join(self.halfregisters[inp2][0].fget(self)), base=16)
                            sum = list(hex(hexnum+hexnum2)[2:])
                            if len(sum) > 2:
                                print("Value too big to be loaded into register")
                                print()
                            else:
                                self.halfregisters[inp2][0].fset(self, sum)
                            #insert machine code
                        else:
                            print("Invalid instruction operands")
                            print()
                    
                    elif mode == "4":
                        #16-bit mem-reg addressing (add)
                        if inp2[1] in self.memory.keys() and inp3 in self.fullregisters.keys():
                            hexnum2 = int(self.memory[inp2[1]], base=16)
                            hexnum = int(''.join(self.fullregisters[inp3][0].fget(self)), base=16)
                            sum = hex(hexnum+hexnum2)[2:]
                            self.memory[inp2[1]] = sum
                            #insert machine code
                        #8-bit mem-reg addressing (add)
                        elif inp2[1] in self.memory.keys() and inp3 in self.halfregisters.keys():
                            hexnum2 = int(self.memory[inp2[1]], base=16)
                            hexnum = int(''.join(self.halfregisters[inp3][0].fget(self)), base=16)
                            sum = hex(hexnum+hexnum2)[2:]
                            self.memory[inp2[1]] = sum
                            #insert machine code
                        else:
                            print("Invalid instruction operands")
                            print()
                    else:
                        print("Invalid mode input")
                        print()
                elif inp1 == "sub":
                    mode = input("Choose an addressing mode:\n\
1: Register to Register\n\
2: Immediate to Register\n\
3: Memory to Register\n\
4: Register to Memory\n")
                    inp2 = input("Enter the first operand: ").lower()
                    inp3 = input("Enter the second operand: ").lower()
                    if mode == '1':
                        #16-bit reg-reg addressing (sub)
                        if inp2 in self.fullregisters.keys() and inp3 in self.fullregisters.keys():
                            num2 = int(''.join(self.fullregisters[inp2][0].fget(self)), base=16)
                            num3 = int(''.join(self.fullregisters[inp3][0].fget(self)), base=16)
                            diff = list(hex(num2-num3)[2:].rjust(4,'0'))
                            if len(diff) > 4:
                                print("Value too big to fit into register")
                                print()
                            else:   
                                self.fullregisters[inp2][0].fset(self, diff)
                            #insert machine code
                        
                        #8-bit reg-reg addressing (sub)
                        elif inp2 in self.halfregisters.keys() and inp3 in self.halfregisters.keys():
                            hexnum2 = int(''.join(self.halfregisters[inp2][0].fget(self)))
                            hexnum3 = int(''.join(self.halfregisters[inp3][0].fget(self)))
                            if hexnum2 < hexnum3:
                                diff = self.complement(hexnum3, 16)
                                diff += hexnum2
                                diff = str(diff)
                                diff = hex(int(diff,16))
                                print(diff)
                            else:
                                hexnum2 = int(''.join(self.halfregisters[inp2][0].fget(self)), base=16)
                                hexnum3 = int(''.join(self.halfregisters[inp3][0].fget(self)), base=16)
                                diff = list(hex(hexnum2-hexnum3)[2:].rjust(4,'0'))
                            if len(diff) > 2:
                                print("Value too big to fit into register")
                                print()
                            else:   
                                self.halfregisters[inp2][0].fset(self, diff)
                            #insert machine code
                        else:
                            print("Invalid instruction operands")
                            print()
                    
                    elif mode == "2":
                        #16-bit reg-imm addressing (sub)
                        if inp2 in self.fullregisters.keys() and inp3.isalnum():
                            #extracts the hex number
                            hexnum = copy.deepcopy(inp3)
                            hexnum = int(hexnum, base=16)
                            hexnum2 = int(''.join(self.fullregisters[inp2][0].fget(self)), base=16)
                            diff = list(hex(hexnum-hexnum2)[2:])
                            if len(diff) <= 4:
                                self.fullregisters[inp2][0].fset(self, diff)
                                #insert machine code
                            else:
                                print("Invalid sized value")
                                print()

                        #8-bit reg-imm addressing (sub)
                        if inp2 in self.halfregisters.keys() and inp3.isalnum():
                            #extracts the hex number
                            hexnum = copy.deepcopy(inp3)
                            hexnum = int(hexnum, base=16)
                            hexnum2 = int(''.join(self.halfregisters[inp2][0].fget(self)), base=16)
                            diff = list(hex(hexnum-hexnum2)[2:])
                            if len(diff) <= 2:
                                self.halfregisters[inp2][0].fset(self, diff)
                                #insert machine code
                            else:
                                print("Invalid sized value")
                                print()
                        
                    elif mode == '3':
                        #16-bit reg-mem addressing (sub)
                        if inp2 in self.fullregisters.keys() and inp3[1] in self.memory.keys():
                            hexnum2 = int(self.memory[inp3[1]], base=16)
                            hexnum = int(''.join(self.fullregisters[inp2][0].fget(self)), base=16)
                            diff = list(hex(hexnum-hexnum2)[2:])
                            if len(diff) > 4:
                                print("Value too big to be loaded into register")
                            else:
                                self.fullregisters[inp2][0].fset(self, diff)
                            #insert machine code
                        #8-bit reg-mem addressing (sub)
                        elif inp2 in self.halfregisters.keys() and inp3[1] in self.memory.keys():
                            hexnum2 = int(self.memory[inp3[1]], base=16)
                            hexnum = int(''.join(self.halfregisters[inp2][0].fget(self)), base=16)
                            diff = list(hex(hexnum-hexnum2)[2:])
                            if len(diff) > 2:
                                print("Value too big to be loaded into register")
                                print()
                            else:
                                self.halfregisters[inp2][0].fset(self, diff)
                            #insert machine code
                        else:
                            print("Invalid instruction operands")
                            print()
                    
                    elif mode == "4":
                        #16-bit mem-reg addressing (sub)
                        if inp2[1] in self.memory.keys() and inp3 in self.fullregisters.keys():
                            hexnum2 = int(self.memory[inp2[1]], base=16)
                            hexnum = int(''.join(self.fullregisters[inp3][0].fget(self)), base=16)
                            diff = hex(hexnum-hexnum2)[2:]
                            self.memory[inp2[1]] = diff
                            #insert machine code
                        #8-bit mem-reg addressing (sub)
                        elif inp2[1] in self.memory.keys() and inp3 in self.halfregisters.keys():
                            hexnum2 = int(self.memory[inp2[1]], base=16)
                            hexnum = int(''.join(self.halfregisters[inp3][0].fget(self)), base=16)
                            diff = hex(hexnum-hexnum2)[2:]
                            self.memory[inp2[1]] = diff
                            #insert machine code
                        else:
                            print("Invalid instruction operands")
                            print()
                    else:
                        print("Invalid mode input")
                        print()
                elif inp1 == 'mul':
                    mode = input("Choose an addressing mode:\n\
1: Register\n\
2: Immediate\n\
3: Memory\n\
")
                    inp2 = input("Enter the first operand: ").lower()
                    # inp3 = input("Enter the second operand: ").lower()
                    if mode == 1:
                        # register to register multiplication, 16 bit
                        if inp2 in self.fullregisters.keys():
                            num2 = int(''.join(self.fullregisters[inp2][0].fget(self)), base=16)
                            num3 = int(''.join(self.fullregisters['ax'][0].fget(self)), base=16)
                            prod = list(hex(num2*num3)[2:].rjust(4,'0'))
                            if len(prod) > 4:
                                print("Value too big to fit into register")
                                print()
                            else:   
                                self.fullregisters[inp2][0].fset(self, prod)
                        # register to register multiplication, 8 bit
                        elif inp2 in self.halfregisters.keys():
                            num2 = int(''.join(self.halfregisters[inp2][0].fget(self)))
                            num3 = int(''.join(self.halfregisters['al'][0].fget(self)))
                            prod = list(hex(num2*num3)[2:].rjust(4,'0'))
                            if len(prod) > 2:
                                print("Value too big to fit into register")
                                print()
                            else:   
                                self.halfregisters['al'][0].fset(self, prod)
                            #insert machine code
                        else:
                            print("Invalid instruction operands")
                            print()
                    
                    elif mode == "2":
                        #16 bit immediate multiplication
                        if inp2.isalnum():
                            #extracts the hex number
                            hexnum = copy.deepcopy(inp3)
                            num = int(hexnum, base=16)
                            num2 = int(''.join(self.fullregisters['ax'][0].fget(self)), base=16)
                            prod = list(hex(num*num2)[2:])
                            if len(prod) <= 4:
                                self.fullregisters['ax'][0].fset(self, prod)
                                #insert machine code
                            else:
                                print("Invalid sized value")
                                print()

                        #8 bit immediate multiplication
                        if inp3.isalnum():
                            #extracts the hex number
                            hexnum = copy.deepcopy(inp3)
                            num = int(hexnum, base=16)
                            num2 = int(''.join(self.halfregisters['al'][0].fget(self)), base=16)
                            prod = list(hex(num*num2)[2:])
                            if len(prod) <= 2:
                                self.halfregisters['al'][0].fset(self, prod)
                                #insert machine code
                            else:
                                print("Invalid sized value")
                                print()
                        
                    elif mode == '3':
                        #16 bit memory multiplication
                        if inp3[1] in self.memory.keys():
                            num2 = int(self.memory[inp3[1]], base=16)
                            num = int(''.join(self.fullregisters['ax'][0].fget(self)), base=16)
                            prod = list(hex(num*num2)[2:])
                            if len(prod) > 4:
                                print("Value too big to be loaded into register")
                            else:
                                self.fullregisters['ax'][0].fset(self, prod)
                            #insert machine code
                        #8 bit memory muliplication
                        elif inp2 in self.halfregisters.keys() and inp3[1] in self.memory.keys():
                            num2 = int(self.memory[inp3[1]], base=16)
                            num = int(''.join(self.halfregisters['al'][0].fget(self)), base=16)
                            prod = list(hex(num*num2)[2:])
                            if len(prod) > 2:
                                print("Value too big to be loaded into register")
                                print()
                            else:
                                self.halfregisters['al'][0].fset(self, prod)
                            #insert machine code
                        else:
                            print("Invalid instruction operands")
                            print()
                    else:
                        print("Invalid mode input")
                        print()

                elif inp1 == "div":
                    mode = input("Choose an addressing mode:\n\
1: Register to Register\n\
2: Immediate to Register\n\
3: Register to Memory\n")
                    inp2 = input("Enter the first operand: ").lower()
                    if mode == '1':
                        #16 register division
                        if inp2 in self.fullregisters.keys():
                            num2 = int(''.join(self.fullregisters[inp2][0].fget(self)), base=16)
                            num3 = int(''.join(self.fullregisters['ax'][0].fget(self)), base=16)
                            div = list(hex(num2//num3)[2:].rjust(4,'0'))
                            rem = list(hex(num2%num3)[2:].rjust(4,'0'))
                            if len(div) > 4:
                                print("Value too big to fit into register")
                                print()
                            else:   
                                self.fullregisters['ax'][0].fset(self, div)
                                self.fullregisters['dx'][0].fset(self, rem)
                            #insert machine code
                        
                        #8 bit register division
                        elif inp2 in self.halfregisters.keys():
                            num2 = int(''.join(self.halfregisters[inp2][0].fget(self)))
                            num3 = int(''.join(self.halfregisters['al'][0].fget(self)))    
                            div = list(hex(num2//num3)[2:].rjust(4,'0'))
                            rem = list(hex(num2%num3)[2:].rjust(4,'0'))
                            if len(div) > 2:
                                print("Value too big to fit into register")
                                print()
                            else:   
                                self.halfregisters['al'][0].fset(self, div)
                                self.halfregisters['dl'][0].fset(self, rem)
                            #insert machine code
                        else:
                            print("Invalid instruction operands")
                            print()
                    
                    elif mode == "2":
                        #16 bit immediate div
                        if inp2.isalnum():
                            #extracts the hex number
                            hexnum = copy.deepcopy(inp3)
                            num = int(hexnum, base=16)
                            num2 = int(''.join(self.fullregisters['ax'][0].fget(self)), base=16)
                            div = list(hex(num//num2)[2:])
                            rem = list(hex(num%num2)[2:])
                            if len(div) <= 4:
                                self.fullregisters['ax'][0].fset(self, div)
                                self.fullregisters['dx'][0].fset(self, rem)
                                #insert machine code
                            else:
                                print("Invalid sized value")
                                print()

                        #8 bit immediate div
                        if inp3.isalnum():
                            #extracts the hex number
                            hexnum = copy.deepcopy(inp3)
                            num = int(hexnum, base=16)
                            num2 = int(''.join(self.halfregisters['al'][0].fget(self)), base=16)
                            div = list(hex(num//num2)[2:])
                            rem = list(hex(num%num2)[2:])
                            if len(div) <= 2:
                                self.halfregisters['ax'][0].fset(self, div)
                                self.halfregisters['dx'][0].fset(self, rem)
                                #insert machine code
                            else:
                                print("Invalid sized value")
                                print()
                        
                    elif mode == '3':
                        #16 bit memory division
                        if inp3[1] in self.memory.keys():
                            num2 = int(self.memory[inp3[1]], base=16)
                            num = int(''.join(self.fullregisters['ax'][0].fget(self)), base=16)
                            div = list(hex(num//num2)[2:])
                            rem = list(hex(num%num2)[2:])
                            if len(div) > 4:
                                print("Value too big to be loaded into register")
                            else:
                                self.fullregisters['ax'][0].fset(self, div)
                                self.fullregisters['ax'][0].fset(self, rem)
                            #insert machine code
                        #8-bit memory division
                        elif inp3[1] in self.memory.keys():
                            num2 = int(self.memory[inp3[1]], base=16)
                            num = int(''.join(self.halfregisters['al'][0].fget(self)), base=16)
                            div = list(hex(hexnum//hexnum2)[2:])
                            rem = list(hex(hexnum%hexnum2)[2:])
                            if len(div) > 2:
                                print("Value too big to be loaded into register")
                                print()
                            else:
                                self.halfregisters['al'][0].fset(self, div)
                                self.halfregisters['dl'][0].fset(self, rem)
                            #insert machine code
                        else:
                            print("Invalid instruction operands")
                            print()
                    else:
                        print("Invalid mode input")
                        print()

                elif inp1 == 'or':
                    mode = input("Choose an addressing mode:\n\
1: Register to Register\n\
2: Register to Immediate\n\
4: Register to Memory\n\
3: Memory to Register\n")
                    inp2 = input("Enter the first operand: ").lower()
                    inp2 = input("Enter the first operand: ").lower()

                    if mode == "1":
                         #16-bit reg-reg addressing (or)
                        if inp2 in self.fullregisters.keys() and inp3 in self.fullregisters.keys():
                            num2 = self.fullregisters[inp2][0].fget(self)
                            num3 = self.fullregisters[inp3][0].fget(self)
                            result = []
                            for i,j in zip(num2, num3):                   
                                if i=='1' or j=='1':
                                    result.append('1')
                                else:
                                    result.append('0')
                            self.fullregisters[inp2][0].fset(self, result)
                            #insert machine code
                        
                        #8-bit reg-reg addressing (or)
                        elif inp2 in self.halfregisters.keys() and inp3 in self.halfregisters.keys():
                            num2 = self.halfregisters[inp2][0]
                            num3 = self.halfregisters[inp3][0]
                            result = []
                            for i,j in zip(num2, num3):                   
                                if i=='1' or j=='1':
                                    result.append('1')
                                else:
                                    result.append('0')
                            self.halfregisters[inp2][0].fset(self, result)
                            #insert machine code
                        else:
                            print("Invalid instruction operands")
                            print()
                    
                    elif mode == "2":
                        #16-bit reg-reg addressing (or)
                        if inp2 in self.fullregisters.keys() and inp3.isalnum():
                            #extracts the hex number
                            num = copy.deepcopy(inp3)
                            num2 = self.fullregisters[inp2][0].fget(self)
                            result = []
                            for i,j in zip(num, num2):                   
                                if i=='1' or j=='1':
                                    result.append('1')
                                else:
                                    result.append('0')
                            self.fullregisters[inp2][0].fset(self, result)
                            #insert machine code

                        #8-bit reg-reg addressing (or)
                        if inp2 in self.halfregisters.keys() and inp3.isalnum():
                            #extracts the hex number
                            num = copy.deepcopy(inp3)
                            num2 = self.halfregisters[inp2][0].fget(self)
                            result = []
                            for i,j in zip(num, num2):                   
                                if i=='1' or j=='1':
                                    result.append('1')
                                else:
                                    result.append('0')
                            self.halfregisters[inp2][0].fset(self, result)
                            #insert machine code
                        
                    elif mode == '3':
                        #16-bit reg-mem addressing (or)
                        if inp2 in self.fullregisters.keys() and inp3[1] in self.memory.keys():
                            num2 = self.memory[inp3[1]]
                            num = self.fullregisters[inp2][0].fget(self)
                            result = []
                            for i,j in zip(num, num2):                   
                                if i=='1' or j=='1':
                                    result.append('1')
                                else:
                                    result.append('0')
                            self.fullregisters[inp2][0].fset(self, result)

                        #8-bit reg-mem addressing (or)
                        elif inp2 in self.halfregisters.keys() and inp3[1] in self.memory.keys():
                            hexnum2 = int(self.memory[inp3[1]], base=16)
                            hexnum = int(''.join(self.halfregisters[inp2][0].fget(self)), base=16)
                            result = []
                            for i,j in zip(num, num2):                   
                                if i=='1' or j=='1':
                                    result.append('1')
                                else:
                                    result.append('0')
                            self.halfregisters[inp2][0].fset(self, result)
                        else:
                            print("Invalid instruction operands")
                            print()
                    
                    elif mode == "4":
                        #16-bit mem-reg addressing (or)
                        if inp2[1] in self.memory.keys() and inp3 in self.fullregisters.keys():
                            num = self.memory[inp2[1]]
                            num2 = self.fullregisters[inp3][0].fget(self)
                            result = []
                            for i,j in zip(num, num2):                   
                                if i=='1' or j=='1':
                                    result.append('1')
                                else:
                                    result.append('0')
                            self.memory[inp2[1]] = result
                        #8-bit mem-reg addressing (or)
                        elif inp2[1] in self.memory.keys() and inp3 in self.halfregisters.keys():
                            num2 = self.memory[inp2[1]]
                            num = self.halfregisters[inp3][0].fget(self)
                            result = []
                            for i,j in zip(num, num2):                   
                                if i=='1' or j=='1':
                                    result.append('1')
                                else:
                                    result.append('0')
                            sum = hex(num+num2)[2:]
                            self.memory[inp2[1]] = result
                            #insert machine code
                        else:
                            print("Invalid instruction operands")
                            print()
                    else:
                        print("Invalid mode input")
                        print()
                elif inp1 == 'and':
                    mode = input("Choose an addressing mode:\n\
1: Register to Register\n\
2: Register to Immediate\n\
4: Register to Memory\n\
3: Memory to Register\n")
                    inp2 = input("Enter the first operand: ").lower()
                    inp2 = input("Enter the first operand: ").lower()

                    if mode == "1":
                         #16-bit reg-reg addressing (and)
                        if inp2 in self.fullregisters.keys() and inp3 in self.fullregisters.keys():
                            num2 = self.fullregisters[inp2][0].fget(self)
                            num3 = self.fullregisters[inp3][0].fget(self)
                            result = []
                            for i,j in zip(num2, num3):                   
                                if i=='1' and j=='1':
                                    result.append('1')
                                else:
                                    result.append('0')
                            self.fullregisters[inp2][0].fset(self, result)
                            #insert machine code
                        
                        #8-bit reg-reg addressing (and)
                        elif inp2 in self.halfregisters.keys() and inp3 in self.halfregisters.keys():
                            num2 = self.halfregisters[inp2][0]
                            num3 = self.halfregisters[inp3][0]
                            result = []
                            for i,j in zip(num2, num3):                   
                                if i=='1' and j=='1':
                                    result.append('1')
                                else:
                                    result.append('0')
                            self.halfregisters[inp2][0].fset(self, result)
                            #insert machine code
                        else:
                            print("Invalid instruction operands")
                            print()
                    
                    elif mode == "2":
                        #16-bit reg-reg addressing (and)
                        if inp2 in self.fullregisters.keys() and inp3.isalnum():
                            #extracts the hex number
                            num = copy.deepcopy(inp3)
                            num2 = self.fullregisters[inp2][0].fget(self)
                            result = []
                            for i,j in zip(num, num2):                   
                                if i=='1' and j=='1':
                                    result.append('1')
                                else:
                                    result.append('0')
                            self.fullregisters[inp2][0].fset(self, result)
                            #insert machine code

                        #8-bit reg-reg addressing (and)
                        if inp2 in self.halfregisters.keys() and inp3.isalnum():
                            #extracts the hex number
                            num = copy.deepcopy(inp3)
                            num2 = self.halfregisters[inp2][0].fget(self)
                            result = []
                            for i,j in zip(num, num2):                   
                                if i=='1' and j=='1':
                                    result.append('1')
                                else:
                                    result.append('0')
                            self.halfregisters[inp2][0].fset(self, result)
                            #insert machine code
                        
                    elif mode == '3':
                        #16-bit reg-mem addressing (and)
                        if inp2 in self.fullregisters.keys() and inp3[1] in self.memory.keys():
                            num2 = self.memory[inp3[1]]
                            num = self.fullregisters[inp2][0].fget(self)
                            result = []
                            for i,j in zip(num, num2):                   
                                if i=='1' and j=='1':
                                    result.append('1')
                                else:
                                    result.append('0')
                            self.fullregisters[inp2][0].fset(self, result)

                        #8-bit reg-mem addressing (and)
                        elif inp2 in self.halfregisters.keys() and inp3[1] in self.memory.keys():
                            hexnum2 = int(self.memory[inp3[1]], base=16)
                            hexnum = int(''.join(self.halfregisters[inp2][0].fget(self)), base=16)
                            result = []
                            for i,j in zip(num, num2):                   
                                if i=='1' and j=='1':
                                    result.append('1')
                                else:
                                    result.append('0')
                            self.halfregisters[inp2][0].fset(self, result)
                        else:
                            print("Invalid instruction operands")
                            print()
                    
                    elif mode == "4":
                        #16-bit mem-reg addressing (and)
                        if inp2[1] in self.memory.keys() and inp3 in self.fullregisters.keys():
                            num = self.memory[inp2[1]]
                            num2 = self.fullregisters[inp3][0].fget(self)
                            result = []
                            for i,j in zip(num, num2):                   
                                if i=='1' and j=='1':
                                    result.append('1')
                                else:
                                    result.append('0')
                            self.memory[inp2[1]] = result
                        #8-bit mem-reg addressing (and)
                        elif inp2[1] in self.memory.keys() and inp3 in self.halfregisters.keys():
                            num2 = self.memory[inp2[1]]
                            num = self.halfregisters[inp3][0].fget(self)
                            result = []
                            for i,j in zip(num, num2):                   
                                if i=='1' and j=='1':
                                    result.append('1')
                                else:
                                    result.append('0')
                            sum = hex(num+num2)[2:]
                            self.memory[inp2[1]] = result
                            #insert machine code
                        else:
                            print("Invalid instruction operands")
                            print()
                    else:
                        print("Invalid mode input")
                        print()  

                elif inp1 == 'not':
                    inp2 = input("Enter the first operand: ").lower()
                    if inp2 in self.fullregisters.keys():
                        num2 = self.fullregisters[inp2][0].fget(self)
                        result = []
                        for i in num2:                   
                            if i=='1':
                                result.append('0')
                            else:
                                result.append('1')
                        self.fullregisters[inp2][0].fset(self, result)
                        #insert machine code
                    
                    #8-bit reg-reg addressing (and)
                    elif inp2 in self.halfregisters.keys():
                        num2 = self.halfregisters[inp2][0]
                        result = []
                        for i in num2:                   
                            if i=='1':
                                result.append('0')
                            else:
                                result.append('1')
                        self.halfregisters[inp2][0].fset(self, result)
                        #insert machine code
                    else:
                        print("Invalid instruction operands")
                        print()

                


proc = Processor()
proc.AX = ['1','2','3','4']
proc.BX = ['1','2','3','5']
proc.procinput()
print(proc.memory['0'])
print(proc.AX)
print(proc.AH)
print(proc.AL)

