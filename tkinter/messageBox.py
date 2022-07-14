from tkinter import *
from tkinter import messagebox


def submit():
    wordInput = userInput.get().lower()

    if wordInput >= "a" and wordInput <= "z":
        print(userInput.get())
    
    else:
        messagebox.showwarning(
            title = "error!",
            message= "error!",
        )

window = Tk()

userInput = Entry(
    window,
    
)
userInput.pack()

submitButton = Button(
    window,
    text = "submit",
    command= submit,
)

submitButton.pack()

window.mainloop()
