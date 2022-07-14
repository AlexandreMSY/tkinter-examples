from tkinter import * 

def testFunc():
    if test.get() == 1:
        print("wow")
    
    else:
        print("not wow")


window1 = Tk()

test = IntVar()

options = Checkbutton(
    text="1 or 0",
    variable= test,
    command = testFunc,
    onvalue= 1,
    offvalue= 0,

)

options.pack()




window1.mainloop()
