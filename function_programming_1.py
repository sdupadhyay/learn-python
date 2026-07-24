# ⚡ Lambda Functions in Python
# A lambda function is created using the lambda keyword, followed by:

# Input parameters
# A colon :
# A single expression that produces the output

# Syntax
# lambda arguments: expression

square = lambda n: n**2
print(square(4))

multiply = lambda a, b: a * b
print(multiply(2, 6))

even_odd = lambda n: "Even" if n % 2 == 0 else "odd"
print(even_odd(20))

# 🔄 map() Function in Python

# map(function,iterable)

num = [1, 2, 3, 4]

# def sum_num(n):
#    return n ** 2

# result = list(map(sum_num,num))
# print(result)

result = list(map(lambda n: n**2, num))
print(result)

words = ["hello", "world", "python"]

res = list(map(lambda n : n.upper(),words))
print(res)

products = [("Laptop", 1200), ("Phone", 800), ("Tablet", 500), ("Monitor", 300)]

def get_price(product):
    return product[1]

prices = list(map(get_price, products))
print(prices)

# filter() Function in Python

# The filter() function is used to select elements from an iterable based on a condition. 
# Only the elements that satisfy the condition (True) are kept.
# filter(function, iterable)
# function → Returns True or False
# iterable → List, tuple, set, string, etc.
# Returns → A filter object (usually converted to a list)

def is_even(n):
    return n % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(is_even, numbers))
print(even_numbers)

# Each number is checked
# Only even numbers are kept

products = [("Laptop", 1200), ("Mouse", 30), ("Keyboard", 80), ("Monitor", 250)]
expensive_products = list(filter(lambda p: p[1] > 100, products))
print(expensive_products)

# 🧾 List Comprehensions in Python

# List comprehensions provide a clean, short, and powerful way to create lists in Python. 
# They replace longer loops with simple one-line expressions, making code easier to read and write.

# [expression for item in iterable]

# expression → What to store in the new list
# item → Each element from the iterable
# iterable → Source of data (list, range, tuple, etc.)

num1 = [1,2,3,4]
square_num1 = [ele ** 2 for ele in num1]
print(square_num1)

words1 = ["hello", "world", "python"]

upper_case_words = [ele.upper() for ele in words1]
print(upper_case_words)

# Using filter()

numbers = [1, 2, 3, 4, 5, 6]
eve_number = [ele for ele in numbers if ele % 2 == 0]
print(eve_number)

# Apply a 10% Discount to Prices
products = [("Laptop", 1500), ("Smartphone", 899), ("Tablet", 499)]
discounted_prices = [(ele[0],ele[1]*0.90) for ele in products]
print(discounted_prices)

# Extract Students with Marks Above 80

students = [("Alice", 85), ("Bob", 75), ("Charlie", 90)]
top_students = [stu[1] for stu in students if stu[1] > 80]
print(top_students)