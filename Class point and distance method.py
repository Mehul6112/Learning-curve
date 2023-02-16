import math

l = True
while l == True: 
    
    class Point:
        def __init__(one, x, y):
            one.x = x
            one.y = y

        def print_point(one):
            print("Point coordinates: ({}, {})".format(one.x, one.y))
        
        def distance(one, two):
            dx = one.x - two.x
            dy = one.y - two.y
            return math.sqrt(dx**2 + dy**2)

    # create two Point objects and print them

    print("For 1st set of co-ordinates: ")
    p1 = Point(int(input("Enter value at x-axis: ")), int(input("Enter value at y-axis: ")))

    print("For 2nd set of co-ordinates: ")
    p2 = Point(int(input("Enter value at x-axis: ")), int(input("Enter value at y-axis: ")))

    p1.print_point()
    p2.print_point()

    dist = p1.distance(p2)
    print("Distance between p1 and p2: {}".format(dist))
    
    l = input("Do you want to run the program again? (y/n): ")
    if l == "y":
        l = bool(1)
    else:
        l = bool(0)
