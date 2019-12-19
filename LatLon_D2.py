from tkinter import *
from math import sin, cos, sqrt, atan2, radians

# --------------------------------


def calculate():
    lat1 = float(e1.get())
    lon1 = float(e2.get())
    lat2 = float(e3.get())
    lon2 = float(e4.get())
    d = EquiRectDistDeg(lat1, lon1, lat2, lon2)

    v.set(str(d) + " m")


def EquiRectDistDeg(lat1, lon1, lat2, lon2):
    return EquiRectDist(radians(lat1), radians(lon1), radians(lat2), radians(lon2))


def EquiRectDist(lat1, lon1, lat2, lon2):
    R = 6371*(10**3)

    x = (lon2 - lon1) * cos(lat1+lat2)/2
    y = lat2 - lat1

    d = sqrt(pow(x, 2) + pow(y, 2)) * R
    return d

# --------------------------------


window = Tk()
window.title("Second_Degree")


l1 = Label(window, text="lat1 : ", fg="blue")
l1.grid(row=0, column=0)
e1 = Entry(window, fg="blue", cursor="heart")
e1.grid(row=0, column=1)

l2 = Label(window, text="lon1 : ", fg="blue")
l2.grid(row=1, column=0)
e2 = Entry(window, fg="blue", cursor="heart")
e2.grid(row=1, column=1)

l5 = Label(window, text="", fg="blue")
l5.grid(row=2, column=0)
l6 = Label(window, text="", fg="blue")
l6.grid(row=2, column=1)

l3 = Label(window, text="lat2 : ", fg="blue")
l3.grid(row=3, column=0)
e3 = Entry(window, fg="blue", cursor="heart")
e3.grid(row=3, column=1)

l4 = Label(window, text="lon2 : ", fg="blue")
l4.grid(row=4, column=0)
e4 = Entry(window, fg="blue", cursor="heart")
e4.grid(row=4, column=1)

b1 = Button(window, text="Calculate", command=calculate, fg="blue")
b1.grid(row=5, column=2)

b2 = Button(window, text="Quit", command=quit, fg="blue")
b2.grid(row=5, column=0)

l7 = Label(window, text="", fg="blue")
l7.grid(row=6, column=0)
l8 = Label(window, text="", fg="blue")
l8.grid(row=6, column=1)

l9 = Label(window, text="Ans : ", fg="blue")
l9.grid(row=7, column=0)

v = StringVar()
l10 = Label(window, textvariable=v, fg="blue")
l10.grid(row=7, column=1)

window.mainloop()