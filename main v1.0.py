from tkinter import *
from tkinter import ttk
from math import radians, sin, atan2, cos, sqrt
import os

# --------------------


def calculate():
    fname = cb.get()
    dist, time_gap = file(fname)

    #dist *= 1000
    d.set(str(dist) + " m")
    h = int(time_gap // 3600)

    v = time_gap % 3600
    m = int(v // 60)
    ss = int(v % 60)

    st = (str(h) + "h " + str(m) + "m " + str(ss) + "s")
    t.set(st)
    s.set(str(dist/time_gap) + " m/s")

    f = open('test.csv', 'a')

    f.write(fname+" : ,"+str(dist)+"m"+","+st+","+str(dist/time_gap)+"m/s,\n")
    f.close()


def file(fname):
    f = open(fname, "r")

    lats = []
    lons = []
    tt1 = 0.0
    L = []
    n = 0
    for l in f.readlines():
        if fname == 'tracesGPS1.csv':
            L = l.split(";")

        else:
            L = l.split(",")

        if n:
            lats.append(L[0])
            lons.append(L[1])
        if n == 1:
            tt1 = L[4]
        n = n + 1

    tt2 = L[4]

    tt1 = tt1.rstrip()
    tt2 = tt2.rstrip()

    d = 0
    for i in range (0,lats.__len__()-1):
        d = d + toRadians(lats[i], lons[i], lats[i+1], lons[i+1])

    time_gap = float(tt2) * (10 ** (-3)) - float(tt1) * (10 ** (-3))

    return d, time_gap


def toRadians(la1, lo1, la2, lo2):
    return calculations(radians(float(la1)), radians(float(lo1)), radians(float(la2)), radians(float(lo2)))


def calculations(lat1, lon1, lat2, lon2):

    R = 6373.0

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c * 1000
    return distance

# --------------------


window = Tk()
window.title('GPS v1.0')

l1 = Label(window, text="FileName : ", fg="blue")
l1.grid(row=0, column=0)
# e1 = Entry(window)
# e1.grid(row=0, column=1)

f = os.path.abspath('.')
L = os.listdir(f)
Lcsv = []

for e in L:
    if '.csv' in e:
        Lcsv.append(e)

#files = ['tracesGPS1.csv', 'tracesGPS2.csv', 'tracesGPS3.csv']
#s1 = Spinbox(window, values=Lcsv)
#s1.grid(row=0, column=1)

cb = ttk.Combobox(window, values=Lcsv)
cb.grid(row=0, column=1)

l2 = Label(window, text="Distance : ", fg="blue")
l2.grid(row=1, column=0)

d = StringVar()
l5 = Label(window, textvariable=d)
l5.grid(row=1, column=1)

l3 = Label(window, text="Time : ", fg="blue")
l3.grid(row=2, column=0)

t = StringVar()
l6 = Label(window, textvariable=t)
l6.grid(row=2, column=1)

l4 = Label(window, text="Speed : ", fg="blue")
l4.grid(row=3, column=0)

s = StringVar()
l7 = Label(window, textvariable=s)
l7.grid(row=3, column=1)

b1 = Button(window, text="Calculate", bg="cyan", command=calculate)
b1.grid(row=4, column=2)

b2 = Button(window, text="Quit", bg="cyan", command=quit)
b2.grid(row=4, column=0)

window.mainloop()