# IMPLICIT TYPE CASTING (AUTOMATIC TYPE CONVERSION)
# x = 5      #int
# y = 2.5    #float

# result = x+y
# print(result)
# print(type(result)) sdsuiuyioyadiosufgyoiasdygouia

# EXPLICIT TYPE CASTING (MANUAL TYPE CONVERSION)
# int() - converts to integer
# float() - converts to float
# str() - converts to string
# BOOL() - converts to boolean

# INT
# x = "10"
# y = int(x)

# print(y)
# print(type(y))

# int(float("10.5"))  # ValueError: invalid literal for int() with base 10: '10.5'

# FLOAT
# x = "15"
# y = float(x)
# print(y)

# STR
# age = 40
# # print("I am " + str(age) + " years old.")
# print("I am " + "30")

# bool

# print(bool(1))
# 1 = true
# 0 = false
# "" = false
# " " = true
# "string"= true
# bool(None) = false
# x = 1
# print(bool(x))  # true

# # Empty or 0 = false
# # anything with value = true

price = input("Enter the price: ")
quantity = input("Enter the quantity: ")

if price.isdigit() and quantity.isdigit():
    price = float(price)
    quantity = int(quantity)
    total = float(price) * int(quantity)
    print(total)
else:
    print("Invalid input")



# # DRY - DON'T REPEAT YOURSELF
# # Always validate before casting

# value = "123"

# if value.isdigit():
#     value = int(value)
# else:
#     print("Invalid input")


# dsfasf
# adsfasdfasdf
# asdfasdf
# asdf