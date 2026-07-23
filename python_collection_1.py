# enumerate() (Index + Value)
# enumerate() gives:

# 📍 Index
# 📦 Value

colors = ["Red", "Green", "Blue"]

for ind, ele in enumerate(colors):
    print(f"Color at index {ind}: {ele}")

# append() – Add at the End

fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)

# insert() – Add at a Specific Position

letters = ["a", "b", "c"]
letters.insert(1, "X")
print(letters)

# extend() – Add Multiple Items

numbers = [1, 2, 3]
numbers.extend([4, 5, 6])
print(numbers)

#  pop() – Remove by Index

letters = ["a", "b", "c"]
removed = letters.pop()
print(letters, removed)  # ['a', 'b'] c

numbers = [10, 20, 30]
numbers.pop(0)
print(numbers)  # [20, 30]

#  remove() – Remove by Value
fruits = ["apple", "banana", "apple"]
fruits.remove("apple")
print(fruits)

# del – Delete by Index or Slice

languages = ["Python", "Java", "C++", "Ruby"]
del languages[1]
print(languages)

numbers = [1, 2, 3, 4, 5, 6]
del numbers[2:4]
print(numbers)  # [1, 2, 5, 6 ]

# index() – Find Position

letters = ["x", "y", "z"]
print(letters.index("y"))  # 1

# in – Check if Item Exists

colors = ["red", "green", "blue"]

if "green" in colors:
    print("Green is available")

# sorted() Function

# Creates a new sorted list
# Original list remains unchanged
# Give me a new sorted copy.

numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = sorted(numbers)

print("Original List:", numbers) # [5, 2, 9, 1, 5, 6]
print("Sorted List:", sorted_numbers) # [1, 2, 5, 5, 6, 9]

# .sort() Method

# Sorts the list in place
# Original list is modified
# Change this list and sort it.

numbers = [5, 2, 9, 1, 5, 6]
numbers.sort()

print("Sorted List:", numbers) # [1, 2, 5, 5, 6, 9]

# Sorting in Descending Order
# Use reverse=True 🔄

numbers = [10, 50, 30, 20, 40]

sorted_desc = sorted(numbers, reverse=True)
numbers.sort(reverse=True)

print("Using sorted():", sorted_desc)
print("Using .sort():", numbers)

# 🔤 Sorting Different Data Types
words = ["banana", "apple", "cherry", "date"]
print(sorted(words)) # ['apple', 'banana', 'cherry', 'date']

# Sorting by Length of Words

words = ["elephant", "cat", "dolphin", "bee"]
print(sorted(words, key=len)) # ['bee', 'cat', 'dolphin', 'elephant']

def sort_order(items):
    return items[1]

students = [("Alice", 85), ("Bob", 90), ("Charlie", 78)]
sorted_by_marks = sorted(students, key=sort_order)

print(sorted_by_marks)

products = [("Laptop", 1000), ("Phone", 500), ("Tablet", 750)]
products.sort(key=lambda x: x[1])
print(products)
