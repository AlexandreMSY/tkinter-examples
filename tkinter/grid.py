from tkinter import *

def textDisplay():
    print(entry1.get(), entry2.get())

window = Tk()

window.geometry("900x500")

frameTest = Frame(borderwidth=1 ,relief=SOLID,)

smallText = Label(frameTest, text="Testing: ", font=("Arial", 12))
smallText.grid(row=0, column=0)

entry1 = Entry(frameTest, width=45,)
entry1.grid(row=0, column=1)

smallText2 = Label(frameTest, text="Testing: ", font=("Arial", 12))
smallText2.grid(row=1, column=0)

entry2 = Entry(frameTest, width=45)
entry2.grid(row=1, column=1)

submit = Button(frameTest, text="Submit", command=textDisplay)
submit.grid(row=2,column=0)

frameTest.grid(row=0, column=0)

window.mainloop()
