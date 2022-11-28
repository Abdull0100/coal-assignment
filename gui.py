from tkinter import *

def add_title(master):
    title = Label(master, text="Intel 8080 Emulator",relief=RAISED)
    title.place(anchor="center", relx=0.5, y=10)





def register_ui(master):
    register_title_frame = Frame(master,bg="pink",width=300,height=550, relief=RAISED, highlightbackground="black", highlightthickness=1)
    register_title_frame.place(anchor=W, x=8, y=400)

    register_title = Label(register_title_frame, text="Registers",bg="purple", width=10, height=2)
    register_title.place(anchor=W, x=0, y=20)





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