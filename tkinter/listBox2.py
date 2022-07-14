from tkinter import *

def submit():
    print(tkList.get(tkList.curselection()))

def replaceButton():
    position = tkList.curselection()

    tkList.delete(tkList.curselection())
    tkList.insert(position, textBox.get())

    tkList.config(
        height = tkList.size()
    )

window = Tk()

tkList = Listbox(
    window,
    font = ("arial", 15),
    background= "lightblue",
    width = 10,
)

tkList.insert(0, "lol")
tkList.insert(1, "lmfao")
tkList.insert(2, "jajaja")

tkList.pack()

tkList.config(height=tkList.size())

submitButton = Button(
    window,
    text="Submit",
    command = submit
)

submitButton.pack()

replace = Button(
    window,
    text= "Replace",
    command = replaceButton
)

replace.pack()

textBox = Entry(
    window,
)

textBox.pack()

window.mainloop()
