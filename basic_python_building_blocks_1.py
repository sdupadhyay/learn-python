# Data Types in Python 
from typing import Text
age = 25          # int
price = 99.5      # float
name = "Alice"    # str
is_active = True  # bool
result = None     # None 

# Feature ===	Primitive ====	Non-Primitive
# Complexity ===  Simple ===	Complex
# Stores ===	Single value ===	Multiple values
# Examples ===	int, float, str, bool. ===	list, tuple, set, dict


# Immutable Data Types 
# -> Onced created cannot be changed 
# int, float, str, tuple

x = 5
x = x + 1   # new object created

# You’re not changing the value — you’re creating a new one.

s = "Hello"
s = s + " World"

# 📌 A new string is created, not modified.

# Non-Primitive (Complex) Data Types

# 1). List 
# Ordered, mutable
fruits = ["apple", "banana", "cherry"]

# 2).Tuple
# Ordered, immutable
coordinates = (10, 20)

# 3). Set
# Unordered, unique values
numbers = {1, 2, 3, 3}

# 4. Dictionary
person = {"name": "Alice", "age": 25}

# 5. Range
numbers = range(5)

# String 
#  Types of Quotes in Python
# Single quotes → 'Hello'
# Double quotes → "Hello"
# Triple quotes → '''Hello''' or """Hello""" (Used for multi-line text)

text = "Python is the best language"
print(len(text))
print(text[0]) # First character 
print(text[-1]) # Last Character

# ✂️ String Slicing (Cutting Strings)

# string[start : end]

# ✂️ 6. Slice from Start to End
print(text[0:6])   # Python

# ✂️ 7. Slice from Beginning
print(text[:6])    # Python

# ✂️ 8. Slice Till the End
print(text[0:]) # Python is the best language

# ✂️ 9. Entire String
print(text[:]) # Python is the best language


# 🔄 Reversing a String

text = "Hello World"
print(text[::-1]) 

# sequence[start : stop : step] 

# start → Index where slicing begins.
# stop → Index where slicing ends.
# step → How many positions to move each time.

print(text[::2]) # HloWrd

# Important Rule: Strings are Immutable

name = "Python"
# name[0] = "J"  ❌ Not allowed

# Escape sequences help include special characters.

# Escape	Meaning
# \" =>	Double quote
# \' =>	Single quote
# \\ =>	Backslash
# \n =>	New line

# ✨ String Formatting (f-Strings)

first = "Naved"
last = "Khan"
print(f"{first} {last}")

# Python String Methods – Beginner-Friendly Notes

# 🧹 1. Data Cleaning (Removing Extra Spaces)
user_input = "  Hello World  "
print(user_input.strip())

# 🔍 2. Search and Replace
sentence = "The sky is blue."
print(sentence.replace("blue", "clear"))

# ✅ 3. Validation (Checking Content)
email = "user@example.com"
if "@" in email:
    print("Valid email address")


# 🔠 4. Change Case
text = "python programming"
print(text.upper())   # PYTHON PROGRAMMING
print(text.lower())   # python programming
print(text.title())   # Python Programming


# 🧹 5. Remove Whitespace
text = "  Hello Python  "

print(text.lstrip())  # Removes left spaces
print(text.rstrip())  # Removes right spaces
print(text.strip())   # Removes both sides

# 🔍 6. Find and Replace Text
text = "I love Python programming."

print(text.find("Python"))     # 7
print(text.replace("Python", "Java"))

# ✅ 4. Check Substrings
text = "Python is fun"

print("fun" in text)        # True
print("boring" not in text) # True
