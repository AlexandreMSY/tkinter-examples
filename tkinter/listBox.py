from tkinter import * 
import os

def submit():
    itemList = []

    os.system("cls")

    for index in textBox.curselection():
        itemList.insert(index, textBox.get(index))
    
    print(itemList)
    
def insert():
    textBox.insert(textBox.size(), textToAdd.get())

    textBox.config(height=textBox.size())

def deleteStuff():
    for index in reversed(textBox.curselection()):
        textBox.delete(index)
    
    textBox.config(height = textBox.size())

window = Tk()

#listBox
textBox = Listbox(
    window,
    font = ("Arial", 15),
    width = "10",
    selectmode= MULTIPLE,
)

textBox.insert(1, "99")
textBox.insert(2, "98")
textBox.insert(3, "97")
textBox.insert(4, "96")

textBox.config(height= textBox.size())

submitButton = Button(
    window,
    text="Click Here",
    command = submit
)

insertButton = Button(
    window,
    text="Insert Item",
    command = insert
)

textToAdd = Entry(
    window,
)

deleteButton = Button(
    window,
    text = "Delete",
    command = deleteStuff
)

textBox.pack()
submitButton.pack()
insertButton.pack()
deleteButton.pack()
textToAdd.pack()

window.mainloop()
