from tkinter import *
from math import radians, degrees, sin, cos, asin, acos, sqrt
from PIL import ImageTk, Image


def calculate():
    x1 = float(e1.get())
    x2 = float(e2.get())
    x3 = float(e3.get())
    x4 = float(e4.get())
    x1, x2, x3, x4 = map(radians, [x1, x2, x3, x4])

    v.set(str(
        6371000 * (
            acos(sin(x2) * sin(x4) + cos(x2) * cos(x4) * cos(x1 - x3)))))


window = Tk()
window.title("Distance")

l1 = Label(window, text="LONGITUDE 1:")
l1.grid(row=0, column=0)
e1 = Entry(window, bg="yellow")
e1.grid(row=0, column=1)

l2 = Label(window, text="LATITUDE 1:")
l2.grid(row=1, column=0)
e2 = Entry(window, bg="yellow")
e2.grid(row=1, column=1)

l3 = Label(window, text="LONGITUDE 2:")
l3.grid(row=2, column=0)
e3 = Entry(window, bg="yellow")
e3.grid(row=2, column=1)

l4 = Label(window, text="LATITUDE 2:")
l4.grid(row=3, column=0)
e4 = Entry(window, bg="yellow")
e4.grid(row=3, column=1)

b1 = Button(window, text="Quit", fg="blue", command=quit)
b1.grid(row=4, column=0)

b2 = Button(window, text="Calculate", fg="blue", command=calculate)
b2.grid(row=4, column=2)

v = StringVar()

l5 = Label(window, textvariable=v, bg="yellow")
l5.grid(row=5, column=1)

l6 = Label(window, text="DISTANCE IN M:")
l6.grid(row=5, column=0)

img = ImageTk.PhotoImage(Image.open('download.png'))
l6 = Label(window, image=img)
l6.grid(row=6, column=1)

window.mainloop()