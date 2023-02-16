def checking_name(name):
    if any(char.isdigit() or not char.isalpha() for char in name):
        raise ValueError("Invalid name. Please enter only alphabets.")
    else:
        print("Valid name entered.")
        
l = True
while l == True:
      
    try:
        name = input("Enter your name: ")
        checking_name(name)
    except ValueError as ve:
        print(ve)

    l = input("Do you want to run the program again? (y/n): ")
    if l == "y":
        l = bool(1)
    else:
        l = bool(0)