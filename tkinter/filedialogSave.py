from tkinter import *
from tkinter import filedialog
import os

def fileSelect(): 
    file = filedialog.askopenfile(filetypes=[("Python",".py")]) #open files
    userInput.insert(INSERT, file.read())

def save():
    fileSave = filedialog.asksaveasfile(defaultextension=".py",filetypes=[("Python",".py"),("All files", ".*")]) #saves file
    code = str(userInput.get(1.0,END))
    fileSave.write(code)                                                                                            
    fileSave.close()

def executeCode():
    exec(userInput.get(1.0,END))

def eraseTerminal():
    os.system("cls")

def delete():
    userInput.delete(1.0, END)

#window    

window = Tk()
window.title("Worst IDE Ever 2.0")
window.geometry("900x420")

userInput = Text(window, width=200)
userInput.pack(expand=TRUE, fill=BOTH)

frame = Frame()

openButton = Button(frame, text="Open PY", command=fileSelect, padx=5).grid(row=0, column=0,padx=5)

saveButton = Button(frame,text="Save", command=save, padx=5).grid(row=0, column=1, padx=5)

executeButton = Button(frame, text="Run", command=executeCode, padx=5).grid(row=0, column=2, padx=5)

clearTerminal = Button(frame, text="Clear Terminal", command=eraseTerminal, padx=5).grid(row=0, column=3, padx=5)

deleteEverything = Button(frame, text="Delete Everything", command=delete, padx=5).grid(row=0, column=4, padx=5)

frame.pack(expand=TRUE)

window.mainloop()
