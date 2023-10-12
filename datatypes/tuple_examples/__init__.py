# A tuple in Python is similar to a list. The difference between the two is that
# list is mutable
# tuple is immutable

# A tuple is created by placing all the items (elements) inside parentheses (),
# separated by commas.
# The parentheses are optional, however, it is a good practice to use them.
# A tuple can have any number of items and they may be of different types (integer, float, list, string, etc.).

# Different types of tuples
# Empty tuple
my_tuple = ()
print(my_tuple)
# Tuple having integers
my_tuple = (1, 2, 3)
print(my_tuple)
# tuple with mixed datatypes
my_tuple = (1, "Hello", 3.4)
print(my_tuple)
# nested tuple
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple)

# As mentioned earlier, we can also create tuples without using parentheses:
my_tuple = 1, 2, 3
my_tuple = 1, "Hello", 3.4

# Create a Python Tuple With one Element
# In Python, creating a tuple with one element is a bit tricky.
# Having one element within parentheses is not enough.
# We will need a trailing comma to indicate that it is a tuple
var1 = ("hello")
print(type(var1))  # <class 'str'>
# Creating a tuple having one element
var2 = ("hello",)
print(type(var2))  # <class 'tuple'>
# Parentheses is optional
var3 = "hello",
print(type(var3))  # <class 'tuple'>
# ("hello") is a string so type() returns str as class of var1 i.e. <class 'str'>
# ("hello",) and "hello", both are tuples so type() returns tuple as class of var1 i.e. <class 'tuple'>

# Access Python Tuple Elements
# Like a list, each element of a tuple is represented by index numbers (0, 1, ...) where the first element is at index 0.
# We use the index number to access tuple elements.

# 1. Indexing
# We can use the index operator [] to access an item in a tuple,
# where the index starts from 0.
# So, a tuple having 6 elements will have indices from 0 to 5.
# Trying to access an index outside of the tuple index range( 6,7,... in this example)
# will raise an IndexError.
# The index must be an integer, so we cannot use float or other types.
# This will result in TypeError.
# accessing tuple elements using indexing
letters = ("p", "r", "o", "g", "r", "a", "m", "i", "z")
print(letters[0])  # prints "p"
print(letters[5])  # prints "a"

# 2. Negative Indexing
# Python allows negative indexing for its sequences.
# The index of -1 refers to the last item, -2 to the second last item and so on.
# accessing tuple elements using negative indexing
letters = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
print(letters[-1])  # prints 'z'
print(letters[-3])  # prints 'm'

# 3. Slicing
# We can access a range of items in a tuple by using the slicing operator colon :
# accessing tuple elements using slicing
my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
# elements 2nd to 4th index
print(my_tuple[1:4])  # prints ('r', 'o', 'g')
# elements beginning to 2nd
print(my_tuple[:-7])  # prints ('p', 'r')
# elements 8th to end
print(my_tuple[7:])  # prints ('i', 'z')
# elements beginning to end
print(my_tuple[:])  # Prints ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')

# Python Tuple Methods
# In Python ,methods that add items or remove items are not available with tuple.
# Only the following two methods are available.
my_tuple = ('a', 'p', 'p', 'l', 'e',)
print(my_tuple.count('p'))  # prints 2
print(my_tuple.index('l'))  # prints 3
# my_tuple.count('p') - counts total number of 'p' in my_tuple
# my_tuple.index('l') - returns the first occurrence of 'l' in my_tuple

# Iterating through a Tuple in Python
languages = ('Python', 'Swift', 'C++')
# iterating through the tuple
for language in languages:
    print(language)

# Check if an Item Exists in the Python Tuple
languages = ('Python', 'Swift', 'C++')
print('C' in languages)  # False
print('Python' in languages)  # True

# Advantages of Tuple over List in Python
# Since tuples are quite similar to lists, both of them are used in similar situations.
# However, there are certain advantages of implementing a tuple over a list:
# 1)We generally use tuples for heterogeneous (different) data types and lists for homogeneous (similar) data types.
# 2)Since tuples are immutable, iterating through a tuple is faster than with a list. So there is a slight performance boost.
# 3)Tuples that contain immutable elements can be used as a key for a dictionary. With lists, this is not possible.
# 4)If you have data that doesn't change, implementing it as tuple will guarantee that it remains write-protected.
