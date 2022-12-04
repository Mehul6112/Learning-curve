l = True
while l == True: 
    my_string = str(input("Enter a string: "))
  
    freq = {}
  
    for i in my_string:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
  
    print ("Count of all characters in", my_string, "is :","\n " +  str(freq))
    l = input("Do you want to run the program again? (y/n): ")
    if l == "y":
        l = bool(1)
    else:
        l = bool(0)