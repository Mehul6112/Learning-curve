l = True
while l == True: 
    n = int(input("Enter number of rows: "))
    while n != 0:
        print("* "*(2*n - 1))
        n -= 1
    l = input("Do you want to run the program again? (y/n): ")
    if l == "y":
        l = bool(1)
    else:
        l = bool(0)