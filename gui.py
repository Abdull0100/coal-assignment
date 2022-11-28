from tkinter import *

def add_title(master):
    title = Label(master, text="Intel 8080 Emulator",relief=RAISED)
    title.place(anchor="center", relx=0.5, y=10)





def register_ui(master):
    register_title_frame = Frame(master,bg="pink",width=300,height=607, relief=RAISED, highlightbackground="black", highlightthickness=1)
    register_title_frame.place(anchor=W, x=8, y=400)

    register_title = Label(register_title_frame, text="Registers",bg="purple", width=39, height=2)
    register_title.place(anchor=W, x=0, y=20)

    # place values of registers here in form of a list
    high_order_register_values = [0,0,0,0]
    low_order_register_values = [0,0,0,0]
    variable_names_list_upper = ["B","C","D","E"]
    variable_names_list_lower = ["H","L","M","A"]
    # names of general purpose registers goes here

    HighOrderRegister = ["AH", "BH", "CH", "DH"]
    LowOrderRegister = ["AL", "BL", "CL", "DL"]

    remaining_registers = ["BP", "SP", "SI", "DI"]
    variable_names_remaining = ["BP", "SP", "SI", "DI"] #to be used as labels
    remaining_registers_values = [0,0,0,0]


    for i in range(len(HighOrderRegister)):
        HighOrderRegister[i] = Label(register_title_frame, text=HighOrderRegister[i], width=5, height=4, bg="yellow")
        HighOrderRegister[i].place(anchor=W, x=0, y=75 + i * 70)

        variable_names_list_upper[i] = Label(register_title_frame, text=high_order_register_values[i], width=11, height=4, bg="white", highlightbackground="black", highlightthickness=1)
        variable_names_list_upper[i].place(anchor=W, x=50, y=75 + i * 70)

        LowOrderRegister[i] = Label(register_title_frame, text=LowOrderRegister[i], width=5, height=4, bg="yellow")
        LowOrderRegister[i].place(anchor=W, x=150, y=75 + i * 70)

        variable_names_list_lower[i] = Label(register_title_frame, text=low_order_register_values[i], width=11, height=4, bg="white", highlightbackground="black", highlightthickness=1)
        variable_names_list_lower[i].place(anchor=W, x=200, y=75 + i * 70)
    
    for i in range(len(remaining_registers)):
        remaining_registers[i] = Label(register_title_frame, text=remaining_registers[i], width=5, height=4, bg="orange")
        remaining_registers[i].place(anchor=W, x=0, y=358 + i * 70)

        variable_names_remaining[i] = Label(register_title_frame, text=remaining_registers_values[i], width=30, height=4, bg="white", highlightbackground="black", highlightthickness=1, relief=RAISED)
        variable_names_remaining[i].place(anchor=W, x=50, y=358 + i * 70)
    

    





root = Tk()
root.geometry("900x900")




add_title(root)
register_ui(root)

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