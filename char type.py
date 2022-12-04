l = True
while l == True: 
    char = str(input("Enter a character: "))
    if len(char) != 1:
        print("Enter a single letter, bakayaro!")
    else:
        if ((char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z')):
            print(char,"is a letter.")
        elif (char >='0' and char <= '9'):
            print(char, "is a number.")
        else:
            print(char, "is a symbol.")
    l = input("Do you want to run the program again? (y/n): ")
    if l == "y":
        l = bool(1)
    else:
        l = bool(0)