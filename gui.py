from tkinter import *

class Register:
    
    def __init__(self, name, value) -> None:
        self.name = name
        self.value = value

    def __str__(self) -> str:
        return f"{self.name} = {self.value}"


# creation and initialization of the general purpose registers
general_purpose_registers = ["ax", "bx", "cx", "dx", "sp", "bp", "si", "di"]
for i in range(len(general_purpose_registers)):
    general_purpose_registers[i] = Register(general_purpose_registers[i], 0)

print(general_purpose_registers)

opcodes = {
    "mov": {
            "mov1": '100010',  # 100010dw oorrrmmm disp (reg,reg/mem,reg/reg,mem)
            "mov2": '1100011',  # 1100011w oo000mmm disp data (mem,imm)
            "mov3": '1011',  # 1011wrrr data (reg,imm)
            "mov4": '101000' # 101000dw disp (mem,acc/acc,mem)
            },  



    "add": {
            "add1" : '000000',  # 000000dw oorrrmmm disp (reg,reg/reg,mem/mem,reg)
            "add2" : '100000' # 100000sw oo000mmm disp data (reg,imm/mem,imm/acc,imm)
            },  

    "dec": {
            "dec1" : '1111111',  # 1111111w oo001mmm disp (reg8, mem)
            "dec2" : '01001'   # 01001rrr (reg16)
            },

    "inc": '1111111',  # 1111111w oo000mmm disp (reg8,mem,reg16)

    "neg": '1111011',  # 1111011w oo011mmm disp (reg, mem)

    "sub": {
            "sub1" : '000101',  # 000101dw oorrrmmm disp (reg,reg/mem,reg/reg,mem)
            "sub2" : '100000',  # 100000sw oo101mmm disp data (reg,imm/mem,imm)
            "sub3" : '0010110'  # 0010110w data (acc,imm)
            },

    "cmp": {
            "cmp1" : '001110',  # 001110dw oorrrmmm disp (reg,reg/mem,reg/reg,mem)
            "cmp2" : '100000', # 100000sw oo111mmm disp data (reg,imm/mem,imm)
            "cmp3" : '0001111' 
            }      

}


def add_title(master):
    title = Label(master, text="Intel 8080 Emulator", relief=RAISED)
    title.place(anchor="center", relx=0.5, y=10)


def register_ui(master):
    register_title_frame = Frame(master, bg="pink", width=300, height=607,
                                 relief=RAISED, highlightbackground="black", highlightthickness=1)
    register_title_frame.place(anchor=W, x=8, y=400)

    register_title = Label(register_title_frame,
                           text="Registers", bg="purple", width=39, height=2)
    register_title.place(anchor=W, x=0, y=20)

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
            register_title_frame, text=HighOrderRegister[i], width=5, height=4, bg="yellow")
        HighOrderRegister[i].place(anchor=W, x=0, y=75 + i * 70)

        variable_names_list_upper[i] = Label(register_title_frame, text=high_order_register_values[i],
                                             width=11, height=4, bg="white", highlightbackground="black", highlightthickness=1, relief=RAISED)
        variable_names_list_upper[i].place(anchor=W, x=50, y=75 + i * 70)

        LowOrderRegister[i] = Label(
            register_title_frame, text=LowOrderRegister[i], width=5, height=4, bg="yellow")
        LowOrderRegister[i].place(anchor=W, x=150, y=75 + i * 70)

        variable_names_list_lower[i] = Label(register_title_frame, text=low_order_register_values[i],
                                             width=11, height=4, bg="white", highlightbackground="black", highlightthickness=1, relief=RAISED)
        variable_names_list_lower[i].place(anchor=W, x=202, y=75 + i * 70)

    for i in range(len(remaining_registers)):
        remaining_registers[i] = Label(
            register_title_frame, text=remaining_registers[i], width=5, height=4, bg="orange")
        remaining_registers[i].place(anchor=W, x=0, y=358 + i * 70)

        variable_names_remaining[i] = Label(register_title_frame, text=remaining_registers_values[i],
                                            width=30, height=4, bg="white", highlightbackground="black", highlightthickness=1, relief=RAISED)
        variable_names_remaining[i].place(anchor=W, x=50, y=358 + i * 70)

def submit():
    print("submit")



def instruction_ui(master):
    global opcodes
    global general_purpose_registers

    instruction_frame = Frame(master, bg="pink", width=400, height=270,
                              relief=RAISED, highlightbackground="black", highlightthickness=1)
    instruction_frame.place(anchor=W, x=340, y=230)

    instruction_title = Label(
        instruction_frame, text="Instruction", bg="purple", width=50, height=2)
    instruction_title.place(anchor=W, x=0, y=20)

    opcode_options = [opcodes for opcodes in opcodes.keys()]
    
    opChoice = StringVar()
    destinatinChoice = StringVar()
    sourceChoice = StringVar()

    opChoice.set("OpCode")
    destinatinChoice.set("Destination")
    sourceChoice.set("Source")
    
    opCodeOption_menu = OptionMenu(instruction_frame, opChoice, *opcode_options)
    opCodeOption_menu.place(anchor=W, x=0, y=75)
    opCodeOption_menu.config(width=10, height=2, bg="white", highlightbackground="black", highlightthickness=1, relief=RAISED)

    destination_options = []
    source_options = []
    for i in range(len(general_purpose_registers)):
        destination_options.append(general_purpose_registers[i].name)

    destination_options.append("memory")
    source_options = destination_options.copy()
    source_options.append("immediate")

    destinationOption_menu = OptionMenu(instruction_frame, destinatinChoice, *destination_options)
    destinationOption_menu.place(anchor=W, x=150, y=75)
    destinationOption_menu.config(width=10, height=2, bg="white", highlightbackground="black", highlightthickness=1, relief=RAISED)

    sourceOption_menu = OptionMenu(instruction_frame, sourceChoice, *source_options)
    sourceOption_menu.place(anchor=W, x=300, y=75)
    sourceOption_menu.config(width=10, height=2, bg="white", highlightbackground="black", highlightthickness=1, relief=RAISED)

    submit_button = Button(instruction_frame, text="Submit", width=10, height=2, bg="white", highlightbackground="black", highlightthickness=1, relief=RAISED, command=submit)
    submit_button.place(anchor=W, x=0, y=150)




root = Tk()
root.geometry("900x900")


add_title(root)
register_ui(root)
instruction_ui(root)
# window.config(background="black")
# window.geometry("500x500")

# title = Frame(window)
# title.pack(side=TOP)

# heading = Label(title,text="Intel 8086",bg="black",fg="#00ff00")
# heading.pack(side=TOP)

# # instruction_input = Entry(window,bg="black",fg="#00ff00")
# # instruction_input.pack()

# instruction = Frame(window)
# instruction.place(x=180,y=0)


# options = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]


# clicked = StringVar()

# clicked.set("Monday")


# opcode = OptionMenu(window,clicked,*options)
# opcode.pack(side=LEFT,anchor="c")

# opcode2 = OptionMenu(window,clicked,*options)
# opcode2.pack(side=LEFT,anchor="c")

# opcode3 = OptionMenu(window,clicked,*options)
# opcode3.pack(side=LEFT,anchor="c")

root.mainloop()
