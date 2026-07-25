# zip() Function in Python

# Combines elements from multiple iterables position by position
# Creates tuples of paired elements
# Stops when the shortest iterable ends
# Returns a zip object (an iterator)

# zip(iterable1, iterable2, iterable3, ...)

list1 = [1, 2, 3]
list2 = ["a", "b", "c"]

zipped = list(zip(list1, list2))
print(zipped)

students = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

student_scores = dict(zip(students, scores))
print(student_scores)

# temp = zip(students,scores)
# print(temp)

for ele, ite in zip(students, scores):
    print(ele, ite)

# unzipp data
zipped_data = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]

names, scores = zip(*zipped_data)

print(names)
print(scores)

# ⚙️ Introduction to Generators in Python
# Generators are a smart and memory-efficient way to work with data in Python. 
# Instead of storing all values at once (like lists), generators produce values one at a time, only when needed.

# 🔑 Key Benefits of Generators
# Efficient memory usage
# Faster execution for large data
# Lazy evaluation (compute only when needed)
# Works well with big files and streams

# 🛠️ Creating Generators

# 1. Generator Expression
# Generator expressions look like list comprehensions but use parentheses () instead of square brackets [].

values = (x for x in range(5))

print(values)
print(type(values))

# Creates a generator object
# Values are not stored in memory
# Numbers are generated only when requested

# 2. Generator Function (Using yield)
# A function becomes a generator when it uses yield instead of return.

def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

counter = count_up_to(5)
print(next(counter))
print(next(counter))

for num in counter:
    print(num)

# ✅ Advantages of Generators
# Memory-efficient
# Faster for large sequences
# Ideal for streaming data
# Can generate infinite values


# 📦 Unpacking Operators in Python (* and **)

# * → Used for iterables like lists, tuples, strings
# ** → Used for dictionaries (key–value pairs)

numbers = [1, 2, 3, 4, 5]

print(numbers)
print(*numbers)

values = [*numbers, *range(5), *"Hello"]
print(values)

def sum_numbers(a, b, c):
    return a + b + c

nums = [5, 10, 15]
result = sum_numbers(*nums)
print(result)

print("Hello")
print(*"Hello")

first = {"a": 1}
second = {"a": 10, "b": 2}

merged = {**first, **second, "z": 1}
print(merged)