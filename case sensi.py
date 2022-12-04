l = True
while l == True: 
    char = str(input("Enter a character: "))
    if len(char) != 1 or char.isdigit():
        print("Enter a single Letter, bakayaro!")
    elif char.isupper():
        print(char,"is uppercase.")
    else:
        print(char,"is lowercase.")
    l = input("Do you want to run the program again? (y/n): ")
    if l == "y":
        l = bool(1)
    else:
        l = bool(0)
        