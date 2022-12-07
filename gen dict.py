a = int(input("number of terms: "))
y = {}
for i in range(1,a+1):
    x = {i:i**3}
    y.update(x)
    
print(y)