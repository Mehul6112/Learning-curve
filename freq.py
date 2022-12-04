my_string = str(input("Enter a string: "))
  
freq = {}
  
for i in my_string:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
  
print ("Count of all characters in", my_string, "is :","\n " +  str(freq))