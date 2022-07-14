from tkinter import *

options = ["Homework", "Discovery", "Human After All"]

def display_option_chosen():
    userOption = " "

    if optionChosen.get() == 0:
        userOption = "Homework"
    
    elif optionChosen.get() == 1:
        userOption = "Discovery"
    
    else:
        userOption = "Human After All"
    
    displayOption.config(
        text= userOption
    )

window = Tk()
window.geometry("420x420")

optionChosen = IntVar()

header = Label(
    window,
    text = "Options",
    font = ("arial", 10)
)

header.pack()

for option in range(len(options)):
    radioButtons = Radiobutton(
        window,
        text = options[option],
        font = ("arial", 10),
        variable = optionChosen,
        value = option
        
    )

    radioButtons.pack()

finishButton = Button(
    window,
    text= "Click",
    font = ("arial", 10),
    relief= SOLID,
    command = display_option_chosen
)

finishButton.pack()

displayOption = Label(
    window,
)

displayOption.pack()

window.mainloop()
