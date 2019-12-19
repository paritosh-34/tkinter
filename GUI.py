from tkinter import *


# -------------------------

def calculate():
    #print("Aie!")
    a = float(e1.get())
    #print(a*2)
    v.set(str(a*2))

# -------------------------

window = Tk()
window.title("Double")

l1 = Label(window, text="x :", fg="blue")
l1.grid(row=0, column=0)
e1 = Entry(window, fg="blue", cursor="heart")
e1.grid(row=0, column=1)

l2 = Label(window, text="       ", bg="pink")
l2.grid(row=1, column=0)

v = StringVar()
l3 = Label(window, textvariable=v, bg="pink")
l3.grid(row=1, column=1)

b1 = Button(window, text="Calculate", command=calculate)
b1.grid(row=2, column=1)

b2 = Button(window, text="Quit", command=quit)
b2.grid(row=2, column=0)

window.mainloop()
