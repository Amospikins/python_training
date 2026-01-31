# "" '' text data
# -4 -3 -2 -1
# name = "Amos"
# message = 'Hello, World!'
# strings are: enclosed in either double or single quotes, Immutable (cannot be changed directly), string is also a sequence of characters (can be indexed and sliced)

# multi-line strings

# text = """ Python is powerful.
# and easy safdsaf
# sfFAS
# sfASF
# fas
# A
# """
# print("""dwfasdfdasfdasffadsf
#       asdfdasf
#       adsfasdf
#       asd
#       f
#       asdf""")

# Indexing
# print(name[8])

# Slicing: extracting a part of the string
# string[start : stop : step]
# text = "PythonProgramming"

# print(text[0:6])
# print(text[0:])
# print(text[:6])
# print(text[::2])
# print(text[::-1])  # reverse the string

# Immutable
# name = "Emmanuel"
# name[0] = "F"

# concatentation: joining strings together with +

# String repetition (*)
# print("Ha" * 3)

# # String length
# text = "Hello"
# print(len(text))

# String Membership
# in, not in

# text ="Python Programming"
# print("Python" in text)
# print("java" not in text)

# Case conversion
# text = "hello world"
# print(text.upper())
# print(text.lower())
# print(text.capitalize())
# print(text.title())

# Remove spaces
# text = "   Hello World    "
# print(text.strip())
# print(text.lstrip())
# print(text.rstrip())

# replace text
# text = "Hello World"
# print(text.replace("World", "Python"))

# count occurrences
# text = "banana"
# print(text.count("a"))  

# finding text
# text = "Python Programming"
# print(text.find("Python")) 
# print(text.find("Java")) 


# Start & end with
# text = "Python Programming"
# print(text.startswith("hon"))
# print(text.endswith("ing"))

# Split string
# sentence = "python is fun"
# words = sentence.split()
# print(words)
# text = "apple banana cherry"
# print(text.split(" "))

# Joining strings
# words = ['Hello', 'world', 'from', 'Python']
# sentence = " ".join(words)
# print(sentence)


# String Formatting
name = "Alice"
age = 30

# print("My name is " + name + " and I am " + str(age) + " years old.") concatenation
# f-strings (best method) => templating or template literals => string interpolation
# print(f"My name is {name} and i am {age + 2} years old.")
# print("My name is {} and I am {} years old.".format(name, age + 2))

# escape characters
# \n  # new line
# \t  # tab space 
# \'  # single quote
# \"  # double quote
# \\  # backslash

# print("Hello,\tWorld!")

# checking string content
# text ="Emmanuel123"
# .isalpha()  # only letters
# .isdigit()  # only numbers
# .isalnum()  # letters and numbers
# .isspace()  # only spaces
# .islower()  # all lowercase
# .isupper()  # all uppercase
# print(text.isalnum())   

