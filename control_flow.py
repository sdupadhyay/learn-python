# for Loop & for-else in Python
# For loop
# for variable in range(start, stop, step):
#     # code to repeat

# for-else Loop

# Runs the else block only if the loop does NOT encounter break
# Skips the else block if break is used

# 🔢 Understanding range() (Very Important)

# Part    	Meaning
# start =>	Starting number (included)
# stop =>	Ending number (not included)
# step => 	Jump between numbers

# Examples 

# range(3)           # 0, 1, 2
# range(5, 10)       # 5, 6, 7, 8, 9
# range(1, 10, 2)    # 1, 3, 5, 7, 9

for i in range(1, 6):
    print(f"Processing task {i}")

# Loop with negative steps 
for i in range(10, 0, -1):
    print(i)

# Nested Loops in Python

for i in range(1,5):
    for j in range(1,5):
        print(f"{i} X {j} =")

# Iterables & Strings in Python

# 🔤 1. String Manipulation

text = "Python"

for i in text:
    print(i)

# ➕ 2. Data Aggregation

numbers = [10, 20, 30]
total = 0

for ele in numbers:
    total += ele

print(total)

# 🗂️ 3. Iterating Over Dictionaries

student = {"name": "Alice", "age": 20, "grade": "A"}
for key, value in student.items():
    print(key, value)