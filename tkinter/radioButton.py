from tkinter import *
from tkinter.font import BOLD

window = Tk()

options = ["Windows", "Linux", "macOS"]
x = IntVar()
print(x)

for i in range(len(options)):
    buttons = Radiobutton(
        window,
        text = options[i],
        font = ("arial", 20, BOLD),
        variable = x,
        value = i,
        
    )

    buttons.pack()

window.mainloop()
