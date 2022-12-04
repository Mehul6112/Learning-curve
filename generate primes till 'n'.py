l = True
while l == True:
    n = int(input("Generate prime till the number: "))
    for i in range(2, n + 1):
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            print(i)
    l = input("Do you want to run the program again? (y/n): ")
    if l == "y":
        l = bool(1)
    else:
        l = bool(0)