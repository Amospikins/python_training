import math
# signs to do operations
# arithmetic operators
# +, -, *, /, %, **, //
# comparison operators
# ==, !=, >, <, >=, <=
# logical operators
# and, or, not
# % modulus operator gives the remainder of a division operation
# ** raise to power (Exponential operator)
# // floor division gives the integer part of the division

# == equal to
# != not equal to
# print(3/2)


# Almighty Formula
# x1=(-b + √(b²-4ac)) / 2a
# x2=(-b - √(b²-4ac)) / 2a

b = -5
a = 1
c = 4

twoA = 2 *a
bSquared =  b ** 2
fourAC = 4 * a *c

bSqMFAC = bSquared - fourAC
Sq_bSqMFAC = math.sqrt(bSqMFAC)
x1 = (-b + Sq_bSqMFAC)/twoA
x2 = (-b - Sq_bSqMFAC)/twoA
print(x1, x2)




