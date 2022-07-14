from tkinter import *
from tkinter import messagebox

def msgBox():
    answser = messagebox.askquestion(title="test", message="test")

    if answser == "yes":
        print("ok!")
    
    else:
        print("not ok!")

window = Tk()

button = Button(
    text="Click Here",
    command=msgBox,
)

button.pack()



window.mainloop()
