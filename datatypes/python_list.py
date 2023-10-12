# A list can
# store elements of different types (integer, float, string, etc.)
# store duplicate elements

# Access List Elements
languages = ["Python", "Swift", "C++"]

# Remember: The list index always starts with 0. Hence, the first element of a list is present at index 0, not 1.
# access item at index 0
print(languages[0])  # Python
# access item at index 2
print(languages[2])  # C++

# Python allows negative indexing for its sequences. The index of -1 refers to the last item, -2 to the second last item and so on.
# access item at index -1
print(languages[-1])  # C++
# access item at index -3
print(languages[-3])  # Python

# Slicing of a List
# In Python, it is possible to access a portion of a list using the slicing operator :
# List slicing in Python

my_list = ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z']

# items from index 2 to index 4
print(my_list[2:5])
# items from index 5 to end
print(my_list[5:])
# items beginning to end
print(my_list[:])
# items from index -1 to end
print(my_list[:-1])
# items from index -5 to index -2
print(my_list[-5:-2])

# Add Elements to a List

# The append() method adds an item at the end of the list
numbers = [21, 34, 54, 12]
print("Before Append:", numbers)
# using append method
numbers.append(32)
print("After Append:", numbers)

# We use the extend() method to add all the items of an iterable (list, tuple, string, dictionary, etc.) to the end of the list.
numbers = [1, 3, 5]
even_numbers = [4, 6, 8]
# add elements of even_numbers to the numbers list
numbers.extend(even_numbers)
print("List after append:", numbers)

# We use the insert() method to add an element at the specified index.
numbers = [10, 30, 40]
# insert an element at index 1 (second position)
numbers.insert(1, 20)
print(numbers)  # [10, 20, 30, 40]

# Change List Items
# Python lists are mutable. Meaning lists are changeable. And we can change items of a list by assigning new values using the = operator
languages = ['Python', 'Swift', 'C++']
# changing the third item to 'C'
languages[2] = 'C'
print(languages)  # ['Python', 'Swift', 'C']

# Remove an Item From a List
# In Python we can use the del statement to remove one or more items from a list. For example,
languages = ['Python', 'Swift', 'C++', 'C', 'Java', 'Rust', 'R']
# deleting the second item
del languages[1]
print(languages)  # ['Python', 'C++', 'C', 'Java', 'Rust', 'R']
# deleting the last item
del languages[-1]
print(languages)  # ['Python', 'C++', 'C', 'Java', 'Rust']
# delete the first two items
del languages[0: 2]  # ['C', 'Java', 'Rust']
print(languages)

# We can also use the remove() method to delete a list item. For example,
languages = ['Python', 'Swift', 'C++', 'C', 'Java', 'Rust', 'R']
# remove 'Python' from the list
languages.remove('Python')
print(languages)  # ['Swift', 'C++', 'C', 'Java', 'Rust', 'R']

# Iterating through a List
languages = ['Python', 'Swift', 'C++']
# iterating through the list
for language in languages:
    print(language)

    # Check if an Element Exists in a  List
    languages = ['Python', 'Swift', 'C++']
    print('C' in languages)  # False
    print('Python' in languages)  # True

    # We use the len() function to find the size of a list.

    languages = ['Python', 'Swift', 'C++']
    print("List: ", languages)
    print("Total Elements: ", len(languages))  # 3

    # List Comprehension
    # create a list with value n ** 2 where n is a number from 1 to 5
    numbers = [n ** 2 for n in range(0, 10)]
    print(numbers)
