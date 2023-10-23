import math
print("This code solves for side C of a right triangle using the Pythagorean Theorem. ")
#ask input for a & b values
a = float(input("What is the length of the first side (Side A)?: "))
b = float(input("What is the length of the first side (Side B)?: "))

#figure out value of C
c = math.sqrt(a**2+b**2)
#output value of C
print("The length of C is " + str(c))
