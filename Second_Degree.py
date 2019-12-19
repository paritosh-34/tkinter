from tkinter import *


# -------------------------

def calculate():
    a = float(e1.get())
    b = float(e2.get())
    c = float(e3.get())

    d = b**2 - 4*a*c
    v.set(str(d))
    if d > 0:
        V.set("2 solutions")
        x1 = ((-b) - (d)**(0.5))/2
        x2 = ((-b) + (d) ** (0.5)) / 2
        v1.set(str(x1))
        v2.set(str(x2))
    elif d == 0:
        V.set("One solution")
    else:
        V.set("No solution")


# -------------------------

window = Tk()
window.title("Second_Degree")

l1 = Label(window, text="a : ", fg="blue")
l1.grid(row=0, column=0)
e1 = Entry(window, fg="blue", cursor="heart")
e1.grid(row=0, column=1)

l2 = Label(window, text="b : ", fg="blue")
l2.grid(row=1, column=0)
e2 = Entry(window, fg="blue", cursor="heart")
e2.grid(row=1, column=1)

l3 = Label(window, text="c : ", fg="blue")
l3.grid(row=2, column=0)
e3 = Entry(window, fg="blue", cursor="heart")
e3.grid(row=2, column=1)

b1 = Button(window, text="Calculate", command=calculate)
b1.grid(row=3, column=2)

b2 = Button(window, text="Quit", command=quit)
b2.grid(row=3, column=0)

v = StringVar()
l4 = Label(window, textvariable=v, fg="blue")
l4.grid(row=4, column=1)

V = StringVar()
l5 = Label(window, textvariable=V, fg="blue")
l5.grid(row=5, column=1)

v1 = StringVar()
l6 = Label(window, textvariable=v1, fg="blue")
l6.grid(row=6, column=1)

v2 = StringVar()
l7 = Label(window, textvariable=v2, fg="blue")
l7.grid(row=6, column=1)

window.mainloop()
