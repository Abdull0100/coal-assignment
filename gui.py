from tkinter import *


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

class Register:

    def __init__(self, name, value) -> None:
        self.name = name
        self.value = value

    def __str__(self) -> str:
        return f"{self.name} = {self.value}"


# creation and initialization of the general purpose registers
general_purpose_registers = ["ax", "bx", "cx", "dx", "sp", "bp", "si", "di"]
for i in range(len(general_purpose_registers)):
    general_purpose_registers[i] = Register(general_purpose_registers[i], 1)

# all the instructions
opcodes = {
    "mov": {
        "mov1": '100010',  # 100010dw oorrrmmm disp (reg,reg/mem,reg/reg,mem)
        "mov2": '1100011',  # 1100011w oo000mmm disp data (mem,imm)
        "mov3": '1011',  # 1011wrrr data (reg,imm)
        "mov4": '101000'  # 101000dw disp (mem,acc/acc,mem)
    },



    "add": {
        "add1": '000000',  # 000000dw oorrrmmm disp (reg,reg/reg,mem/mem,reg)
        # 100000sw oo000mmm disp data (reg,imm/mem,imm/acc,imm)
        "add2": '100000'
    },

    "dec": {
        "dec1": '1111111',  # 1111111w oo001mmm disp (reg8, mem)
        "dec2": '01001'   # 01001rrr (reg16)
    },

    "inc": '1111111',  # 1111111w oo000mmm disp (reg8,mem,reg16)

    "neg": '1111011',  # 1111011w oo011mmm disp (reg, mem)

    "sub": {
        "sub1": '000101',  # 000101dw oorrrmmm disp (reg,reg/mem,reg/reg,mem)
        "sub2": '100000',  # 100000sw oo101mmm disp data (reg,imm/mem,imm)
        "sub3": '0010110'  # 0010110w data (acc,imm)
    },

    "cmp": {
        "cmp1": '001110',  # 001110dw oorrrmmm disp (reg,reg/mem,reg/reg,mem)
        "cmp2": '100000',  # 100000sw oo111mmm disp data (reg,imm/mem,imm)
        "cmp3": '0001111'
    }

}


memory_locations = {
    "0000": "00",
    "0001": "00",
    "0002": "00",
    "0003": "00",
    "0004": "00",
    "0005": "00",
    "0006": "00",
    "0007": "00",
    "0008": "00",
    "0009": "00",
    "000A": "00",
    "000B": "00",
    "000C": "00",
    "000D": "00",
    "000E": "00",
    "000F": "00",
}


def add_title(master):
    title = Label(master, text="Intel 8080 Emulator",font=("calibri 12 bold"), relief=FLAT, bg="black", fg="#00ff00", height=9, width=300)
    title.place(anchor="center", relx=0.5, y=10)


def register_ui(master):
    register_title_frame = Frame(master, width=301, height=608,
                                 relief=FLAT, highlightbackground="black", highlightthickness=2, bg="black")
    register_title_frame.place(anchor=W, x=8, y=403)

    register_title = Label(register_title_frame,
                           text="Registers",font="calibri 10 bold",fg="#00ff00",width=32, height=2, bg="black",highlightbackground="#12123b",highlightthickness=3)
    register_title.place(anchor=W, x=0, y=15)

    # place values of registers here in form of a list
    high_order_register_values = [0, 0, 0, 0]
    low_order_register_values = [0, 0, 0, 0]
    variable_names_list_upper = ["B", "C", "D", "E"]
    variable_names_list_lower = ["H", "L", "M", "A"]
    # names of general purpose registers goes here

    HighOrderRegister = ["AH", "BH", "CH", "DH"]
    LowOrderRegister = ["AL", "BL", "CL", "DL"]

    remaining_registers = ["BP", "SP", "SI", "DI"]
    variable_names_remaining = ["BP", "SP", "SI", "DI"]  # to be used as labels
    remaining_registers_values = [0, 0, 0, 0]

    for i in range(len(HighOrderRegister)):
        HighOrderRegister[i] = Label(
            register_title_frame, text=HighOrderRegister[i],fg="#00ff00", width=5, height=4, bg="black")
        HighOrderRegister[i].place(anchor=W, x=0, y=75 + i * 70)

        variable_names_list_upper[i] = Label(register_title_frame, text=high_order_register_values[i],
                                             width=11, height=4,fg="#00ff00", bg="#12123b", highlightbackground="black", highlightthickness=1, relief=FLAT)
        variable_names_list_upper[i].place(anchor=W, x=50, y=75 + i * 70)

        LowOrderRegister[i] = Label(
            register_title_frame, text=LowOrderRegister[i],fg="#00ff00",width=5, height=4, bg="black")
        LowOrderRegister[i].place(anchor=W, x=150, y=75 + i * 70)

        variable_names_list_lower[i] = Label(register_title_frame, text=low_order_register_values[i],
                                             width=11, height=4, bg="#12123b",fg="#00ff00" ,highlightbackground="black", highlightthickness=1, relief=FLAT)
        variable_names_list_lower[i].place(anchor=W, x=202, y=75 + i * 70)

    for i in range(len(remaining_registers)):
        remaining_registers[i] = Label(
            register_title_frame, text=remaining_registers[i],fg="#00ff00", width=5, height=4, bg="black")
        remaining_registers[i].place(anchor=W, x=0, y=358 + i * 70)

        variable_names_remaining[i] = Label(register_title_frame, text=remaining_registers_values[i],fg="#00ff00",
                                            width=30, height=4, bg="#12123b", highlightbackground="black", highlightthickness=1, relief=FLAT)
        variable_names_remaining[i].place(anchor=W, x=50, y=358 + i * 70)


def instruction_ui(master):
    global opChoice
    global destinationChoice
    global sourceChoice
    global instruction_label

    instruction_frame = Frame(master, bg="black", width=426, height=270,
                              relief=RAISED, highlightbackground="black", highlightthickness=1)
    instruction_frame.place(anchor=W, x=340, y=234)

    instruction_title = Label(
        instruction_frame, text="Instruction",font="calibri 9 bold" ,bg="black",fg="#00ff00", width=52, height=2, highlightbackground="#12123b",highlightthickness=3)
    instruction_title.place(anchor=W, x=-1, y=20)

    opcode_options = [opcodes for opcodes in opcodes.keys()]

    opChoice = StringVar()
    destinationChoice = StringVar()
    sourceChoice = StringVar()

    opChoice.set("OpCode")
    destinationChoice.set("Destination")
    sourceChoice.set("Source")

    instruction_entry = OptionMenu(
        instruction_frame, opChoice, *opcode_options)
    instruction_entry.place(anchor=W, x=5, y=75)
    instruction_entry.config(width=10, height=2, bg="#12123b",fg="#00ff00",
                             highlightbackground="black", highlightthickness=1, relief=RAISED, activebackground="#12123b", activeforeground="#00ff00")

    destination_options = []
    source_options = []
    for i in range(len(general_purpose_registers)):
        destination_options.append(general_purpose_registers[i].name)

    destination_options.append("memory")
    source_options = destination_options.copy()
    source_options.append("immediate")

    destination_entry = OptionMenu(
        instruction_frame, destinationChoice, *destination_options)
    destination_entry.place(anchor=W, x=149, y=75)
    destination_entry.config(width=10, height=2, bg="#12123b",fg="#00ff00",
                             highlightbackground="black", highlightthickness=1, relief=RAISED ,activebackground="#12123b", activeforeground="#00ff00")

    source_entry = OptionMenu(instruction_frame, sourceChoice, *source_options)
    source_entry.place(anchor=W, x=295, y=75)
    source_entry.config(width=10, height=2, bg="#12123b",fg="#00ff00",
                        highlightbackground="black", highlightthickness=1, relief=RAISED, activebackground="#12123b", activeforeground="#00ff00")

    instruction_label = Label(
        instruction_frame, width=50, height=2, bg="black", fg="#00ff00", highlightbackground="#12123b", highlightthickness=3, relief=SOLID)
    instruction_label.place(anchor=W, x=5, y=150)

    submit_button = Button(instruction_frame, text="Submit", width=10, height=1, bg="#12123b",fg="#00ff00",
                           highlightbackground="black", highlightthickness=1, relief=RAISED, command=submit)
    submit_button.place(anchor=W, x=150, y=250)


def execute_instruction(opcode,destination,source):
    alu = ALU()
    source_value = 0
    destination_value = 0
    if opcode == "add":
        for i in range(len(general_purpose_registers)):
            if destination == general_purpose_registers[i].name:
                destination_value = general_purpose_registers[i].value
                break
        if source == "immediate":
            source_value = int(input("Enter immediate value: "))
        else:
            for i in range(len(general_purpose_registers)):
                if source == general_purpose_registers[i].name:
                    source_value = general_purpose_registers[i].value
                    break
        destination_value =  alu.add(destination_value, source_value)
        for i in range(len(general_purpose_registers)):
            if destination == general_purpose_registers[i].name:
                general_purpose_registers[i].value = destination_value
                break
        register_ui(root)




def submit():
    complete_instruction = ""
    if opChoice.get() != "OpCode":
        complete_instruction += opChoice.get()
        if destinationChoice.get() != "Destination":
            complete_instruction += " " + destinationChoice.get()
            if sourceChoice.get() != "Source":
                execute_instruction(opChoice.get(), destinationChoice.get(), sourceChoice.get())
                complete_instruction += ", " + sourceChoice.get()
                instruction_label.config(text=complete_instruction)
            else:
                instruction_label.config(text="Invalid Instruction")
        else:
            instruction_label.config(text="Invalid Instruction")
    else:
        instruction_label.config(text="Invalid Instruction")

def memory_ui(master):
    global memory_labels
    global memory_values
    global memory_title
    global memory_frame

    memory_frame = Frame(master, bg="black", width=400, height=600,
                         relief=RAISED, highlightbackground="black", highlightthickness=1)
    memory_frame.place(anchor=W, x=800, y=399)

    memory_title = Label(
        memory_frame, text="Memory",font="calibri 10 bold", bg="black",fg="#00ff00", width=50, height=2, highlightbackground="#12123b", highlightthickness=3)
    memory_title.place(anchor=W, x=-43, y=20)

    memory_labels = []
    memory_values = []

    for i in range(16):
        memory_labels.append(Label(
            memory_frame, text="0x00" + hex(i)[2:].upper(), width=10,font="calibri 10 bold",fg="#00ff00", height=2, bg="#12123b", highlightbackground="black", highlightthickness=1, relief=RAISED))
        memory_labels[i].place(anchor=W, x=5, y=75 + i * 30)

        memory_values.append(Label(
            memory_frame, text="0x" + hex(0)[2:].upper(), width=30, height=2, bg="#12123b",fg="#00ff00", highlightbackground="black", highlightthickness=1, relief=RAISED))
        memory_values[i].place(anchor=W, x=137, y=75 + i * 30)


global root
root = Tk()
root.geometry("1500x1000")
root.config(bg="#1e1e62")


add_title(root)
register_ui(root)
instruction_ui(root)
memory_ui(root)

root.mainloop()
