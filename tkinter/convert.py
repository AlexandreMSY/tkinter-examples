from tkinter import *
from tkinter.font import BOLD
from funcao import Binary
from funcao import DecimalToBinary

#function that prints the result

def printResult():
    parameter = int(userInput.get())
    printThis = 0
    
    if option.get() == 1:
        printThis = str(DecimalToBinary(parameter))

        result.config(
            text = printThis
        )
    else:
        printThis = str(Binary(parameter))

        result.config(
            text = printThis
        )


#window 

window = Tk()
window.title("Conversor")

option = IntVar()

window.geometry("350x100")

userInput = Entry(
    window,
    font = ("arial", 15, BOLD)
)

userInput.pack()

click = Button (
    window,
    text="Result",
    bg= "yellow",
    relief=SOLID,
    command = printResult,
).pack()

result = Label(
    window,
    font = ("arial", 15)
)

result.pack()

optionChk = Checkbutton(
    window,
    text="Decimal to Binary",
    variable = option,
    onvalue= 1,
    offvalue= 0,
)

optionChk.pack()

window.mainloop()
