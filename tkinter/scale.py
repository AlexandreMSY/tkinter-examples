from tkinter import *

def printVar():
    if x.get() >= 5:
        print("ok")
    
    else:
        print("not ok!")

window = Tk()

x = IntVar()

scaleSlider = Scale(
    window,
    from_ = 0,
    to = 10,
    orient= HORIZONTAL,
    showvalue= 1,
    variable= x,
    troughcolor= "#70afff",
)

scaleSlider.pack()

button = Button(
    window,
    text="test",
    command = printVar,
)

button.pack()

window.mainloop()
