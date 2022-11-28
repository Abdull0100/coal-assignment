from tkinter import *

window = Tk()
window.config(background="black")
window.geometry("500x500")

title = Frame(window)
title.pack(side=TOP)

heading = Label(title,text="Intel 8086",bg="black",fg="#00ff00")
heading.pack(side=TOP)

# instruction_input = Entry(window,bg="black",fg="#00ff00")
# instruction_input.pack()

instruction = Frame(window)
instruction.place(x=180,y=0)


options = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]


clicked = StringVar()

clicked.set("Monday")


opcode = OptionMenu(window,clicked,*options)
opcode.pack(side=LEFT,anchor="c")

opcode2 = OptionMenu(window,clicked,*options)
opcode2.pack(side=LEFT,anchor="c")

opcode3 = OptionMenu(window,clicked,*options)
opcode3.pack(side=LEFT,anchor="c")

window.mainloop()