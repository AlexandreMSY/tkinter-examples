from tkinter import *
from tkinter import filedialog

def fileTest():
    filePath = filedialog.askopenfilename()
    print(filePath)

    file = open(filePath, "r")
    print(file.read())

window = Tk()

button = Button(text="Click Here", command=fileTest)
button.pack()

window.mainloop()
