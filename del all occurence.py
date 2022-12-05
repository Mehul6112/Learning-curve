str1 = str(input("Enter a sentence: "))
result = ""
ch_to_remove = str(input("input a char: "))

for ch in str1:
    occurred_flag = False
    if ch == ch_to_remove and occurred_flag == False:
        occurred_flag = True
        continue
    else:
        result += ch
print(result)