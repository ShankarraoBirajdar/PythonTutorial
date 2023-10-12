# Python Sets
# A set is a collection of unique data. That is, elements of a set cannot be duplicate.

# Create a Set in Python
# In Python, we create sets by placing all the elements inside curly braces {}, separated by comma.
# A set can have any number of items and they may be of different types (integer, float, tuple, string etc.).
# But a set cannot have mutable elements like lists, sets or dictionaries as its elements.

# create a set of integer type
student_id = {112, 114, 116, 118, 115}
print('Student ID:', student_id)
# create a set of string type
vowel_letters = {'a', 'e', 'i', 'o', 'u'}
print('Vowel Letters:', vowel_letters)
# create a set of mixed data types
mixed_set = {'Hello', 101, -2, 'Bye'}
print('Set of mixed data types:', mixed_set)
# Note: When you run this code, you might get output in a different order. This is because the set has no particular order.

# Create an Empty Set in Python
# Creating an empty set is a bit tricky.
# Empty curly braces {} will make an empty dictionary in Python.
# To make a set without any elements, we use the set() function without any argument.
# create an empty set
empty_set = set()
# create an empty dictionary
empty_dictionary = {}
# check data type of empty_set
print('Data type of empty_set:', type(empty_set))
# check data type of dictionary_set
print('Data type of empty_dictionary', type(empty_dictionary))
# Data type of empty_set: <class 'set'>
# Data type of empty_dictionary <class 'dict'>

# Duplicate Items in a Set
numbers = {2, 4, 6, 6, 2, 8}
print(numbers)  # {8, 2, 4, 6}

# Add and Update Set Items in Python
# Sets are mutable. However,
# since they are unordered, indexing has no meaning.
# We cannot access or change an element of a set using indexing or slicing.
# Set data type does not support it.

# Add Items to a Set in Python
# In Python, we use the add() method to add an item to a set
numbers = {21, 34, 54, 12}
print('Initial Set:',numbers)
# using add() method
numbers.add(32)
print('Updated Set:', numbers)

# Update Python Set
# The update() method is used to update the set with items other collection types (lists, tuples, sets, etc).
companies = {'Lacoste', 'Ralph Lauren'}
tech_companies = ['apple', 'google', 'apple']
companies.update(tech_companies)
print(companies)
# Output: {'google', 'apple', 'Lacoste', 'Ralph Lauren'}

# Remove an Element from a Set
# We use the discard() method to remove the specified element from a set.
languages = {'Swift', 'Java', 'Python'}
print('Initial Set:',languages)
# remove 'Java' from a set
removedValue = languages.discard('Java')
print('Set after remove():', languages)

# Built-in Functions with Set

# The all() function returns True if all elements in the given iterable are true. If not, it returns False.
boolean_list = ['True', 'True', 'True']
# check if all elements are true
result = all(boolean_list)
print(result)
# Output: True

# The any() function returns True if any element of an iterable is True. If not, it returns False.
boolean_list = ['True', 'False', 'True']
# check if any element is true
result = any(boolean_list)
print(result)
# Output: True

# The enumerate() function adds a counter to an iterable and returns it (the enumerate object).
languages = ['Python', 'Java', 'JavaScript']
enumerate_prime = enumerate(languages)
# convert enumerate object to list
print(list(enumerate_prime))
# Output: [(0, 'Python'), (1, 'Java'), (2, 'JavaScript')]

# The len() function returns the number of items (length) in an object.
languages = ['Python', 'Java', 'JavaScript']
# compute the length of languages
length = len(languages)
print(length)
# Output: 3

# The max() function returns the largest item in an iterable.
# It can also be used to find the largest item between two or more parameters.
numbers = [9, 34, 11, -4, 27]
# find the maximum number
max_number = max(numbers)
print(max_number)
# Output: 34

# The min() function returns the smallest item in an iterable.
# It can also be used to find the smallest item between two or more parameters.
numbers = [9, 34, 11, -4, 27]
# find the smallest number
min_number = min(numbers)
print(min_number)
# Output: -4

# The sorted() function sorts the elements of a given iterable
# in a specific order (ascending or descending) and returns it as a list.
# sorted(iterable, key=None, reverse=False)
# vowels list
py_list = ['e', 'a', 'u', 'o', 'i']
print(sorted(py_list))
# string
py_string = 'Python'
print(sorted(py_string))
# vowels tuple
py_tuple = ('e', 'a', 'u', 'o', 'i')
print(sorted(py_tuple))

# Sort in descending order
# set
py_set = {'e', 'a', 'u', 'o', 'i'}
print(sorted(py_set, reverse=True))
# dictionary
py_dict = {'e': 1, 'a': 2, 'u': 3, 'o': 4, 'i': 5}
print(sorted(py_dict, reverse=True))
# frozen set
frozen_set = frozenset(('e', 'a', 'u', 'o', 'i'))
print(sorted(frozen_set, reverse=True))

# The sum() function adds the items of an iterable and returns the sum.
marks = [65, 71, 68, 74, 61]
# find sum of all marks
total_marks = sum(marks)
print(total_marks)
# Output: 339