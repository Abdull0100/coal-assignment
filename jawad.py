class ALU:
    def __init__(self) -> None:
        pass

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b

    def inc(self, a):
        return a + 1

    def dec(self, a):
        return a - 1

class OpCodes:
    def dumpregs(self):
        global registers
        for register in registers:
            print(register)


class Register:
    
    def __init__(self, name, value) -> None:
        self.name = name
        self.value = value

    def __str__(self) -> str:
        return f"{self.name} = {self.value}"

    def __repr__(self) -> str:
        return f"{self.name} = {self.value}"

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
    


def call_dumpregs():
    global registers
    for register in registers:
        print(register)


def instructionParser(instruction):
    tokens = instruction.split(" ")
    if(len(tokens) == 3):
        tokens[1] = tokens[1].replace(",", "")
    validater(tokens)

def execute(instruction):
    instructionParser(instruction)
    global registers
    global opCodes
    global alu

    tokens = instruction.split(" ")
    if(len(tokens) == 3):
        tokens[1] = tokens[1].replace(",", "")

    if tokens[0] == "add":
        reg1 = [reg for reg in registers if reg.name == tokens[1]][0]
        reg2 = [reg for reg in registers if reg.name == tokens[2]][0]
        reg1.value = alu.add(reg1.value, reg2.value)

    elif tokens[0] == "sub":
        reg1 = [reg for reg in registers if reg.name == tokens[1]][0]
        reg2 = [reg for reg in registers if reg.name == tokens[2]][0]
        reg1.value = alu.sub(reg1.value, reg2.value)

    elif tokens[0] == "mul":
        reg1 = [reg for reg in registers if reg.name == tokens[1]][0]
        reg2 = [reg for reg in registers if reg.name == tokens[2]][0]
        reg1.value = alu.mul(reg1.value, reg2.value)

    elif tokens[0] == "div":
        reg1 = [reg for reg in registers if reg.name == tokens[1]][0]
        reg2 = [reg for reg in registers if reg.name == tokens[2]][0]
        reg1.value = alu.div(reg1.value, reg2.value)

    elif tokens[0] == "inc":
        reg1 = [reg for reg in registers if reg.name == tokens[1]][0]
        reg1.value = alu.inc(reg1.value)

    elif tokens[0] == "dec":
        reg1 = [reg for reg in registers if reg.name == tokens[1]][0]
        reg1.value = alu.dec(reg1.value)

    elif tokens[0] == "dumpregs":
        call_dumpregs()

    else:
        print("Invalid instruction")

ax = Register("ax", 0)
bx = Register("bx", 0)
cx = Register("cx", 0)
dx = Register("dx", 0)


registers = [ax, bx, cx, dx]
opCodes = ["add", "sub", "mul", "div", "inc", "dec","mov", "dumpregs"]
alu = ALU()
# print("Welcome to the Intel 8086 Simulator\n\n")
# print("Instructions:\n")
# print("Available registers: eax, ebx, ecx, edx\n")
# print("Available opcodes: add, sub, mul, div, inc, dec\n")
# print("Enter the instruction in the following format: opcode register1 register2\n")
print("Example: add eax, ebx\n")
while instruction != "exit":
    instruction = input("[Enter]");
    execute(instruction)


