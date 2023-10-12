# We create a list by placing elements inside [], separated by commas. For example,
ages = [19, 26, 23]
print(ages)

# A list can
# store elements of different types (integer, float, string, etc.)
# store duplicate elements

# list with elements of different data types
list1 = [1, "Hello", 3.4]
print(list1)
# list with duplicate elements
list2 = [1, "Hello", 3.4, "Hello", 1]
print(list2)
# empty list
list3 = []
print(list3)

# In Python, lists are ordered and each item in a list is associated with a number.
# The number is known as a list index.
# The index of the first element is 0, second element is 1 and so on. For example,
languages = ["Python", "Swift", "C++"]

# access item at index 0
print(languages[0])  # Python

# access item at index 2
print(languages[2])  # C++

# Python allows negative indexing for its sequences. The index of -1 refers to the last item,
# -2 to the second last item and so on.
languages = ["Python", "Swift", "C++"]

# access item at index 0
print(languages[-1])  # C++

# access item at index 2
print(languages[-3])  # Python

# In Python, it is possible to access a portion of a list using the slicing operator :. For example,

# List slicing in Python

my_list = ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z']

# items from index 2 to index 4
print(my_list[2:5])

# items from index 5 to end
print(my_list[5:])

# my_list[2:5] returns a list with items from index 2 to index 4.
# my_list[5:] returns a list with items from index 5 to the end.
# my_list[:] returns all list items

# items beginning to end
print(my_list[:])

# Add Elements to a List
# Lists are mutable (changeable). Meaning we can add and remove elements from a list.
# Python list provides different methods to add items to a list

# 1. Using append()
# The append() method adds an item at the end of the list.
numbers = [21, 34, 54, 12]
print("Before Append:", numbers)
# using append method Here, append() adds 32 at the end of the array.
numbers.append(32)
print("After Append:", numbers)

# 2. Using extend()
# We use the extend() method to add all the items of an iterable (list, tuple, string, dictionary, etc.)
# to the end of the list.
numbers = [1, 3, 5]
even_numbers = [4, 6, 8]
# add elements of even_numbers to the numbers list
numbers.extend(even_numbers)
print("List after append:", numbers)

# 3. Using insert()
# We use the insert() method to add an element at the specified index.
numbers = [10, 30, 40]
# insert an element at index 1 (second position)
numbers.insert(1, 20)
print(numbers)  # [10, 20, 30, 40]

# Python lists are mutable. Meaning lists are changeable.
# And we can change items of a list by assigning new values using the = operator.
languages = ['Python', 'Swift', 'C++']
# changing the third item to 'C'
languages[2] = 'C'
print(languages)  # ['Python', 'Swift', 'C']

# Remove an Item From a List

# 1. Using del Statement
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

# 2. Using remove()
# We can also use the remove() method to delete a list item. For example,
languages = ['Python', 'Swift', 'C++', 'C', 'Java', 'Rust', 'R']
# remove 'Python' from the list
languages.remove('Python')
print(languages)  # ['Swift', 'C++', 'C', 'Java', 'Rust', 'R']

# The list pop() method removes the item at the specified index.
# The method also returns the removed item.
prime_numbers = [2, 3, 5, 7]
# remove the element at index 2
removed_element = prime_numbers.pop(2)
print('Removed Element:', removed_element)
print('Updated List:', prime_numbers)

# The clear() method removes all items from the list.
prime_numbers = [2, 3, 5, 7, 9, 11]
# remove all elements
prime_numbers.clear()
# Updated prime_numbers List
print('List after clear():', prime_numbers)

# The count() method returns the number of times the specified element appears in the list.
# create a list
numbers = [2, 3, 5, 2, 11, 2, 7]
# check the count of 2
count = numbers.count(2)
print('Count of 2:', count)
# Output: Count of 2: 3

# The sort() method sorts the items of a list in ascending or descending order.
prime_numbers = [11, 3, 7, 5, 2]
# sorting the list in ascending order
prime_numbers.sort()
print(prime_numbers)
# Output: [2, 3, 5, 7, 11]

# The sort() method accepts a reverse parameter as an optional argument.
# Setting reverse = True sorts the list in the descending order.
# vowels list
vowels = ['e', 'a', 'u', 'o', 'i']
# sort the vowels
vowels.sort(reverse=True)
# print vowels
print('Sorted list (in Descending):', vowels)

# The copy() method returns a shallow copy of the list.
# mixed list
prime_numbers = [2, 3, 5]
# copying a list
numbers = prime_numbers.copy()
print('Copied List:', numbers)
# Output: Copied List: [2, 3, 5]