l = True
while l == True: 
    n = int(input("Enter number of rows: "))
    i = int(1)
    while n != 0:
        print("* "*i, "\n")
        i += 2
        n -= 1
    l = input("Do you want to run the program again? (y/n): ")
    if l == "y":
        l = bool(1)
    else:
        l = bool(0)