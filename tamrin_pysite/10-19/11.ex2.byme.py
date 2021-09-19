import math
a=int(input("num: "))
if sum([ True if a%factor == 0 else False for factor in ( [2] + list(range(3,int(math.sqrt(a)),2) )) ]): 
  print("Number is composite")
else: 
  print("Number is prime")