
def eqn(a,b,c):
    global det
    det = b**2 - 4*a*c
    if det == 0 or det > 0:
        x1 = float((-b + (det)**0.5)/2*a)
        x2 = float((-b - (det)**0.5)/2*a)
        return x1, x2
        
    elif det < 0:
        return "No real solutions"
l = True
while l == True:
    a = int(input("Enter the co-efficient of x\N{SUPERSCRIPT TWO}: "))
    b = int(input("Enter the co-efficient of x: "))
    c = int(input("Enter the constant term: "))
    print(eqn(a,b,c))
    l = input("Do you want to run the program again? (y/n): ")
    if l == "y":
        l = bool(1)
    else:
        l = bool(0)
    
    


