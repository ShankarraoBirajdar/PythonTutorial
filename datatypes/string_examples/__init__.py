# Python Strings
# In computer programming, a string is a sequence of characters.
# For example, "hello" is a string containing a sequence of characters 'h', 'e', 'l', 'l', and 'o'.
# We use single quotes or double quotes to represent a string in Python
# create string type variables
name = "Python"
print(name)
message = "I love Python."
print(message)

# Access String Characters in Python
# We can access the characters in a string in three ways
# 1)Indexing: One way is to treat strings as a list and use index values.
greet = 'hello'
# access 1st index element
print(greet[1]) # "e"

# 2)Negative Indexing: Similar to a list, Python allows negative indexing for its strings
greet = 'hello'
# access 4th last element
print(greet[-4]) # "e"
# 3)Slicing: Access a range of characters in a string by using the slicing operator colon :
greet = 'Hello'
# access character from 1st index to 3rd index
print(greet[1:4])  # "ell"
# Note: If we try to access an index out of the range or use numbers other than an integer, we will get errors.

# Python Strings are immutable
# In Python, strings are immutable. That means the characters of a string cannot be changed.
# message = 'Hola Amigos'
# message[0] = 'H'#TypeError: 'str' object does not support item assignment
# print(message)

# However, we can assign the variable name to a new string.
message = 'Hola Amigos'
# assign new string to message variable
message = 'Hello Friends'
print(message); # prints "Hello Friends"

# Python Multiline String
# We can also create a multiline string in Python.
# For this, we use triple double quotes """ or triple single quotes '''
# multiline string
message = """
Never gonna give you up
Never gonna let you down
"""
print(message)

# Python String Operations
# 1. Compare Two Strings
# We use the == operator to compare two strings.
# If two strings are equal, the operator returns True. Otherwise, it returns False.
str1 = "Hello, world!"
str2 = "I love Python."
str3 = "Hello, world!"
# compare str1 and str2
print(str1 == str2)
# compare str1 and str3
print(str1 == str3)

# 2. Join Two or More Strings
# In Python, we can join (concatenate) two or more strings using the + operator
greet = "Hello, "
name = "Jack"
# using + operator
result = greet + name
print(result)
# Output: Hello, Jack

# Iterate Through a Python String
greet = 'Hello'
# iterating through greet string
for letter in greet:
    print(letter)

# Python String Length
# In Python, we use the len() method to find the length of a string.
greet = 'Hello'
# count length of greet string
print(len(greet))
# Output: 5

# String Membership Test
# We can test if a substring exists within a string or not, using the keyword in
print('a' in 'program') # True
print('at' not in 'battle') #False

# Methods of Python String

# Python String upper()
message = 'python is fun'
# convert message to uppercase
print(message.upper())
# Output: PYTHON IS FUN

# Python String lower()
message = 'PYTHON IS FUN'
# convert message to lowercase
print(message.lower())
# Output: python is fun

# Python String partition()
# The partition() method takes a string parameter separator that separates the string at the first occurrence of it
# The partition method returns a 3-tuple containing:
# the part before the separator, separator parameter,
# and the part after the separator if the separator parameter is found in the string
# the string itself and two empty strings if the separator parameter is not found
string = "Python is fun"
# 'is' separator is found
print(string.partition('is '))
# 'not' separator is not found
print(string.partition('not '))
string = "Python is fun, isn't it"
# splits at first occurence of 'is'
print(string.partition('is'))

# Python String replace()
text = 'bat ball'
# replace 'ba' with 'ro'
replaced_text = text.replace('ba', 'ro')
print(replaced_text)
# Output: rot roll

# Python String find()
# The find() method returns the index of first occurrence of the substring (if found). If not found, it returns -1
message = 'Python is a fun programming language'
# check the index of 'fun'
print(message.find('fun'))
# Output: 12

# Python String index()
# The index() method returns the index of a substring inside the string (if found).
# If the substring is not found, it raises an exception.
# str.index(sub[, start[, end]] )
# sub - substring to be searched in the string str.
# start and end(optional) - substring is searched within str[start:end]
text = 'Python is fun'
# find the index of is
result = text.index('is')
print(result)
# Output: 7

# Python String rstrip()
# The rstrip() method returns a copy of the
# string with trailing characters removed (based on the string argument passed).
title = 'Python Programming   '
# remove trailing whitespace from title
result = title.rstrip()
print(result)
# Output: Python Programming

# Python String split()
# The split() method splits a string at the specified separator and returns a list of substrings.
cars = 'BMW-Telsa-Range Rover'
# split at '-'
print(cars.split('-'))
# Output: ['BMW', 'Tesla', 'Range Rover']

# Python String startswith()
# method returns True if a string starts with the specified prefix(string). If not, it returns False
message = 'Python is fun'
# check if the message starts with Python
print(message.startswith('Python'))
# Output: True

# Python String isnumeric()
# The isnumeric() method checks if all the characters in the string are numeric.
pin = "523"
# checks if every character of pin is numeric
print(pin.isnumeric())
# Output: True

# Returns the copy of the string with its first character capitalized and the rest of the letters are in lowercased.
str = 'shankar'
print(str.capitalize())

# Returns a lowered case string. It is similar to the lower() method, but the casefold() method converts more characters into lower case.
str = 'SHANKAR'
print(str.casefold())

# Returns a new centered string of the specified length, which is padded with the specified character. The deafult character is space.
print(str.center(11, '*'))
str = 'TutorialsTeacher is a free online Tutorials website'
print(str.count('Tutorials'))
