f = open("tracesGPS1.csv", "r")

a = 0
n = 0

lats = []
lons = []

for l in f.readlines():
    #print(l)
    L = l.split(";")
    print(L)
    lats.append(L[0])
    lons.append(L[1])

    n = n + 1

print(lats)
print(lons)
# print("Average : ", a/n)

# distance speed time for first five
