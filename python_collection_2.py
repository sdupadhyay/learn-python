# A tuple is one of Python’s built-in data types used to store multiple values together in a single variable.

# 💡 Think of a tuple like a sealed box 📦 — once you put items inside, you cannot change them.

# A tuple is an ordered, immutable collection of items.

# Tuples are useful when:

#  -> 🔒 Data should not be modified (e.g., coordinates, fixed settings)
#  -> ⚡ They are faster than lists (because they are immutable)
#  -> 🔑 They can be used as dictionary keys (lists cannot!

# 📌 Comma is the Real Hero!

point = (1, 2, 3)
print(point)

data = (1, 2)
print(data)

data = 1, 2, 3
print(data)

data = 7,
print(type(data))   # <class 'tuple'>

data = 7
print(type(data))   # <class 'int'>

# → Integer
# , → Tuple with one element
# 👉 The comma (,) creates the tuple, not the brackets!

# Tuple Multiplication (Repeating Tuples)
nums = (2, 3, 4) * 2
print(nums) # (2, 3, 4, 2, 3, 4)

# 📌 The tuple is repeated, not modified.

#  Creating Tuples from Lists & Strings

values = tuple([12, 14, 16])
print(values)

characters = tuple("Coding")
print(characters)
# (12, 14, 16)
# ('C', 'o', 'd', 'i', 'n', 'g')

# Tuple Unpacking

coordinates = (15, 25, 35)
x, y, z = coordinates
print(x, y, z)

# 15 25 35

#  Membership Testing

data = (10, 20, 30, 40)

if 30 in data:
    print("Present")
else:
    print("Not Present")

# Swapping Variables Using Tuples

a, b = 5, 10
a, b = b, a
print(a, b)

# 10 5

# 📌 Different Ways to Create a Set

# Creating an empty set
empty_set = set()
print(type(empty_set))

# Creating a set from a list
num_set = set([10, 20, 30, 40])
print(num_set)

# Creating a set directly
fruits = {"apple", "banana", "cherry"}
print(fruits)

# Creating a set with duplicate values
numbers = {1, 2, 3, 3, 4, 5, 5}
print(numbers)

# ⚙️ Common Set Operations

# ➕ 1. Adding and Removing Elements

my_set = {2, 4, 6, 8}

my_set.add(10)
print(my_set)

my_set.remove(4)
print(my_set)

popped_element = my_set.pop()
print("Popped:", popped_element)
print(my_set)

# 🔗 2. Union
# Combines all unique elements from both sets.

set_a = {1, 2, 3}
set_b = {3, 4, 5}

print(set_a | set_b)
print(set_a.union(set_b))

# 🔁 3. Intersection
# Finds common elements between two sets.

print(set_a & set_b)
print(set_a.intersection(set_b))

# ➖ 4. Difference
# Finds elements in the first set but not in the second.

print(set_a - set_b)
print(set_a.difference(set_b))
