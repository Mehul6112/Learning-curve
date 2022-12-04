l = True
while l == True: 
    n = int(input("Enter the number of primes you want: "))
    i = int(2)
    while n != 0:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)
            n -= 1
        i += 1
    l = input("Do you want to run the program again? (y/n): ")
    if l == "y":
        l = bool(1)
    else:
        l = bool(0)
    
