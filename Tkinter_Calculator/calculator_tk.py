from tkinter import *
window = Tk()
window.geometry("400x400")

#Entry Box
e=Entry(window, width=40, borderwidth=5)
e.place(x=0, y=0)


#BUTTONS
def click(num):
    result = e.get()
    e.delete(0, END)
    e.insert(0, str(result) + str(num))
b=Button(window, text="1", width=6, command=lambda: click(1))
b.place(x=10, y=60)

b=Button(window, text="2", width=6 , command=lambda: click(2))
b.place(x=70, y=60)

b=Button(window, text="3", width=6, command=lambda: click(3))
b.place(x=130, y=60)

b=Button(window, text="4", width=6, command=lambda: click(4))
b.place(x=10, y=120)

b=Button(window, text="5", width=6, command=lambda: click(5))
b.place(x=70, y=120)

b=Button(window, text="6", width=6, command=lambda: click(6))
b.place(x=130, y=120)

b=Button(window, text="7", width=6, command=lambda: click(7))
b.place(x=10, y=180)

b=Button(window, text="8", width=6, command=lambda: click(8))
b.place(x=70, y=180)

b=Button(window, text="9", width=6, command=lambda: click(9))
b.place(x=130, y=180)

b=Button(window, text="0", width=6, command=lambda: click(0))
b.place(x=70, y=240)

#OPERATORS
def add():
    n1=e.get()
    global math
    math="addition"
    global i
    i=int(n1)
    e.delete(0, END)

b=Button(window, text="+", width=6, command=add)
b.place(x=190, y=60)

def subtract():
    n1=e.get()
    global math
    math="subtraction"
    global i
    i=int(n1)
    e.delete(0, END)

b=Button(window, text="-", width=6, command=subtract)
b.place(x=190, y=120)

def multiply():
    n1=e.get()
    global math
    math="multiplication"
    global i
    i=int(n1)
    e.delete(0, END)

b=Button(window, text="*", width=6, command=multiply)
b.place(x=190, y=180)

def divide():
    n1=e.get()
    global math
    math="division"
    global i
    i=int(n1)
    e.delete(0, END)

b=Button(window, text="/", width=6, command=divide)
b.place(x=190, y=240)

def equals():
    n2=e.get()
    e.delete(0, END)
    if math=="addition":
        e.insert(0, i + int(n2))
    elif math=="subtraction":
        e.insert(0, i - int(n2))
    elif math=="multiplication":
        e.insert(0, i * int(n2))
    elif math=="division":
        e.insert(0, i / int(n2))


b=Button(window, text="=", width=6, command=equals)
b.place(x=130, y=240)
b=Button(window, text="C", width=6, command=lambda: e.delete(0, END))
b.place(x=10, y=240)
window.mainloop()