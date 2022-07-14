from tkinter import *

def seeText():
    print(text.get(1.0,END))
    text.delete(1.0,END)


window = Tk()

window.geometry("300x280")

text = Text(width= 20, height= 10, font=("Arial", 15), background="#939393")
text.pack()

button = Button(text="submit", command=seeText
)

button.pack()

window.mainloop()
