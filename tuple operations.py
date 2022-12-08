t1 = (1,2,5,9,2,4,6,8,10)
t2 = (11,13,15)
print(t1[0:5], "\n")
print(t1[5:], "\n")
even = ()
for i in t1:
  if i%2 == 0:
    even = even + (i,)
print(even)
print(t1+t2, "\n")
print("Minimum value is: ", min(t1+t2), "\n", "Maximum value is: ", max(t1+t2))
