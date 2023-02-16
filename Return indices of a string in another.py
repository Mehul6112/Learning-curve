l = True
while l == True:
    str1 = str(input("Enter a string: "))
    str2 = str(input("Enter another string: "))
    #str1 = "One piece wa jitsu zai sura!"
    #str2 = "a"
    indices = []
    index = -1
    while True:
        index = str1.find(str2, index + 1)
        if index == -1:
            break
        indices.append(index)
    if indices == []:
        print(-1)
    else:
        print(indices)
    l = input("Do you want to run the program again? (y/n): ")
    if l == "y":
        l = bool(1)
    else:
        l = bool(0)