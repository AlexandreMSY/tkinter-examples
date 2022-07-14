from tkinter import *

def printChosenNum():
    if scaleChosenNum.get() >= 5:
        print("nice")

    else:
        print("not nice")

window = Tk()

scaleChosenNum = IntVar()

scaleButton = Scale(
    window,
    from_ = 0,
    to = 100,
    orient= HORIZONTAL,
    troughcolor= "lightblue",
    variable = scaleChosenNum,
)

button = Button(
    window,
    text="Click",
    command = printChosenNum,
)

scaleButton.pack()
button.pack()



window.mainloop()