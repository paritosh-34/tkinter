r = "y"
while r == "y":
    x = int(input("Enter no : "))
    while 1 > x or x > 10:
        # i = 1
        print("---------------------")
        print("\tTable of", x, ":-")
        print("---------------------")
        # while i < 11:
        #     print(i, "*", x, "=", x*i)
        #     i += 1

        for i in range(0,11):
            print(i, "*", x, "=", x*i)

        r = input("Continue (y/n) ? ")

print("......END......")