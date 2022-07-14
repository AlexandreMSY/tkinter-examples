from tkinter import *

window = Tk()

menubar = Menu(window)

filemenu = Menu(menubar,tearoff=0)
filemenu.add_command(label="text123")

menubar.add_cascade(label="TEST", menu=filemenu)

window.config(menu=menubar)

window.mainloop()