l = True
while l == True:
    is_prime = bool(1)
    n = int(input("Enter a number: "))
    if n == 1 or n == 0:
        print(n, "is neither prime nor composite.")
    elif n>1:
        i = int(2)
        while i < n/2:
            if n % i == 0:
                is_prime = bool(0)
                break
            else:
                i += 1
        if is_prime:
            print(n, "is a prime number.")
        else:
            print(n, "is not a prime number.")
        l = input("Do you want to run the program again? (y/n): ")
        if l == "y":
            l = bool(1)
        else:
            l = bool(0)