# Python Dictionary
# In Python, a dictionary is a collection that allows us to store data in key-value pairs.

# Create a Dictionary
# We create dictionaries by placing key:value pairs inside curly brackets {}, separated by commas.
# creating a dictionary
country_capitals = {
  "United States": "Washington D.C.",
  "Italy": "Rome",
  "England": "London"
}
# printing the dictionary
print(country_capitals)

# Note: Dictionary keys must be immutable, such as tuples, strings, integers, etc.
# We cannot use mutable (changeable) objects such as lists as keys.

# Valid dictionary
my_dict = {
  1: "Hello",
  (1, 2): "Hello Hi",
  3: [1, 2, 3]
}
print(my_dict)

# Invalid dictionary
# Error: using a list as a key is not allowed
# my_dict = {
#   1: "Hello",
#   [1, 2]: "Hello Hi",
# }
# print(my_dict)

# Python Dictionary Length
country_capitals = {
  "United States": "Washington D.C.",
  "Italy": "Rome",
  "England": "London"
}
# get dictionary's length
print(len(country_capitals)) # 3

# Access Dictionary Items
# We can access the value of a dictionary item by placing the key inside square brackets
# We can also use the get() method to access dictionary items.
country_capitals = {
  "United States": "Washington D.C.",
  "Italy": "Rome",
  "England": "London"
}
print(country_capitals["United States"])  # Washington D.C.
print(country_capitals["England"]) # London

# Change Dictionary Items
# Python dictionaries are mutable (changeable).
# We can change the value of a dictionary element by referring to its key.
country_capitals = {
  "United States": "Washington D.C.",
  "Italy": "Naples",
  "England": "London"
}
# change the value of "Italy" key to "Rome"
country_capitals["Italy"] = "Rome"
print(country_capitals)

# Add Items to a Dictionary
# We can add an item to the dictionary by assigning a value to a new key
# (that does not exist in the dictionary).
# We can also use the update method() to add or change dictionary items.
country_capitals = {
  "United States": "Washington D.C.",
  "Italy": "Naples"
}
# add an item with "Germany" as key and "Berlin" as its value
country_capitals["Germany"] = "Berlin"
print(country_capitals)

# Remove Dictionary Items
# We use the del statement to remove an element from the dictionary.
# We can also use the pop method() to remove an item from the dictionary.
country_capitals = {
  "United States": "Washington D.C.",
  "Italy": "Naples"
}
# delete item having "United States" key
del country_capitals["United States"]
print(country_capitals)

# If we need to remove all items from the dictionary at once, we can use the clear() method.
country_capitals = {
  "United States": "Washington D.C.",
  "Italy": "Naples"
}
country_capitals.clear()
print(country_capitals) # {}

# Dictionary Membership Test
# We can check whether a key exists in a dictionary using the in operator.
my_list = {1: "Hello", "Hi": 25, "Howdy": 100}
print(1 in my_list) # True
# the not in operator checks whether key doesn't exist
print("Howdy" not in my_list) # False
print("Hello" in my_list) # False
# Note: The in operator checks whether a key exists; it doesn't check whether a value exists or not

# Iterating Through a Dictionary
# A dictionary is an ordered collection of items (starting from Python 3.7).
# Meaning a dictionary maintains the order of its items.
# We can iterate through dictionary keys one by one using a for loop.
country_capitals = {
  "United States": "Washington D.C.",
  "Italy": "Naples"
}
# print dictionary keys one by one
for country in country_capitals:
    print(country)
print("----------")
# print dictionary values one by one
for country in country_capitals:
    capital = country_capitals[country]
    print(capital)


# Python Dictionary Methods

# The pop() method removes and returns an element from a dictionary having the given key.
# create a dictionary
marks = { 'Physics': 67, 'Chemistry': 72, 'Math': 89 }
element = marks.pop('Chemistry')
print('Popped Marks:', element)
# Output: Popped Marks: 72

# The update() method updates the dictionary
# with the elements from another dictionary object or from an iterable of key/value pairs.
marks = {'Physics':67, 'Maths':87}
internal_marks = {'Practical':48}
marks.update(internal_marks)
print(marks)
# Output: {'Physics': 67, 'Maths': 87, 'Practical': 48}

# The keys() method extracts the keys of the dictionary and returns the list of keys as a view object.
numbers = {1: 'one', 2: 'two', 3: 'three'}
# extracts the keys of the dictionary
dictionaryKeys = numbers.keys()
print(dictionaryKeys)
# Output: dict_keys([1, 2, 3])

# The values() method returns a view object that displays a list of all the values in the dictionary.
marks = {'Physics':67, 'Maths':87}
print(marks.values())
# Output: dict_values([67, 87])

# The get() method returns the value of the specified key in the dictionary.
scores = {
    'Physics': 67,
    'Maths': 87,
    'History': 75
}
result = scores.get('Physics')
print(scores)    # 67

# The popitem() method removes and returns the (key, value) pair from the dictionary
# in the Last In, First Out (LIFO) order.
# Returns the latest inserted element (key,value) pair from the dictionary.
# Removes the returned element pair from the dictionary.
# Note: Before Python 3.7, the popitem() method returned and removed an arbitrary element (key, value)
# pair from the dictionary.
person = {'name': 'Phill', 'age': 22, 'salary': 3500.0}
# ('salary', 3500.0) is inserted at the last, so it is removed.
result = person.popitem()
print('Return Value = ', result)
print('person = ', person)
# inserting a new element pair
person['profession'] = 'Plumber'
# now ('profession', 'Plumber') is the latest element
result = person.popitem()
print('Return Value = ', result)
print('person = ', person)
