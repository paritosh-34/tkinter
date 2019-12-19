from tkinter import *

# ------------------------


def run():
    f = open("test.csv", "a")

    n = e1.get()
    s = e2.get()
    m1 = float(e3.get())
    m2 = float(e4.get())
    m3 = float(e5.get())

    f.write(n + "," + s + "," + str(m1) + "," + str(m2) + "," + str(m3) + ",\n")

    f.close()

# --------------------


window = Tk()
window.title("Double")

l1 = Label(window, text="Name : ", fg="blue")
l1.grid(row=0, column=0)
e1 = Entry(window, fg="blue", cursor="heart")
e1.grid(row=0, column=1)

l2 = Label(window, text="Sir Name : ", fg="blue")
l2.grid(row=1, column=0)
e2 = Entry(window, fg="blue", cursor="heart")
e2.grid(row=1, column=1)

l3 = Label(window, text="Marks 1 : ", fg="blue")
l3.grid(row=2, column=0)
e3 = Entry(window, fg="blue", cursor="heart")
e3.grid(row=2, column=1)

l4 = Label(window, text="Marks 2 : ", fg="blue")
l4.grid(row=3, column=0)
e4 = Entry(window, fg="blue", cursor="heart")
e4.grid(row=3, column=1)

l5 = Label(window, text="Marks 3 : ", fg="blue")
l5.grid(row=4, column=0)
e5 = Entry(window, fg="blue", cursor="heart")
e5.grid(row=4, column=1)


b1 = Button(window, text="Submit", command=run)
b1.grid(row=8, column=1)

b2 = Button(window, text="Quit", command=quit)
b2.grid(row=8, column=0)

window.mainloop()



