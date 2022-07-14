from tkinter import *
from tkinter import colorchooser

def colour():
    color = colorchooser.askcolor()
    hexColor = color[1]
    
    window.config(
        background=hexColor
    )

window = Tk()
window.geometry("200x200")

button = Button(
    text="Color Chooser",
    command= colour,
)

button.pack()

window.mainloop()
