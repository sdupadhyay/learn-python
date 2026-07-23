# Introduction to Dictionaries in Python

# 🔁 Iterating Through a Dictionary (Step by Step)

person = {
    "name": "Alice",
    "age": 25
}

# Prints only keys
for key in person:
    print(key)

# Uses keys to fetch values
for key in person:
    print(person[key])

#  Loop through keys and values together

for key, value in person.items():
    print(key, ":", value)