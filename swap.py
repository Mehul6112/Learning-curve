l = True
while l == True: 
    str1 = input("Please Enter First String : ")
    str2 = input("Please Enter Second String : ")
    n = int(input("Enter no. of chars to swap : "))
    x=str1[0:n]
 
    str1=str1.replace(str1[0:n],str2[0:n])
 
    str2=str2.replace(str2[0:n],x)
 
    print("Your first string has become :- ",str1)
    print("Your second string has become :- ",str2)
    l = input("Do you want to run the program again? (y/n): ")
    if l == "y":
        l = bool(1)
    else:
        l = bool(0)