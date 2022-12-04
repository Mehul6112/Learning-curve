def num_2_word(char):
    if char == '0':
        print("Zero")
    elif char == '1':
        print("One")
    elif char == '2':
        print("Two")
    elif char == '3':
        print("Three")
    elif char == '4':
        print("Four")
    elif char == '5':
        print("Five")
    elif char == '6':
        print("Six")
    elif char == '7':
        print("Seven")
    elif char == '8':
        print("Eight")
    else:
        print("Nine")
l = True
while l == True: 
    char = input("Enter a character: ")
    if len(char) != 1 or char.isalpha():
        print("Enter a single number, bakayaro!")
    else:
        print(num_2_word(char), "\n")
    l = input("Do you want to run the program again? (y/n): ")
    if l == "y":
        l = bool(1)
    else:
        l = bool(0)