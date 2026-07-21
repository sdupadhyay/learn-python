import json
# 🌐 Web Applications (JSON Data)
user_data = '{"age": "30"}' 
# json.loads convert into json formate
age = int(json.loads(user_data)["age"])
print(age + 5)

# 🤖 Implicit Type Conversion (Automatic)

# ✅ Boolean to Integer
x = True
y = 5
result = x + y

print(result)
print(type(result))
# 🧠 True behaves like 1, False behaves like 0.

data = [1, 2, 3]
print(tuple(data))     # list → tuple

data_tuple = (4, 5, 6)
print(list(data_tuple))  # tuple → list

text = "Python"
print(list(text))     # string → list

# 🔗 List → String
data = [1, 2, 3]
result = ",".join(map(str, data))
print(result)
 
# Ternary Operator
# value_if_true if condition else value_if_false

age = 15
message = "Eligible" if age >= 18 else "Not Eligible"
print(message) # Not Eligible

purchase = 5000
discount = 20 if purchase >= 5000 else 10
print(f"Discount: {discount}%")


# 🎓 Assign "Pass" or "Fail" based on marks
marks = 15
res = "Pass" if marks >= 12 else "Fail"
print(res)

# 👦 Check if a person is a Teenager (age between 13 and 19)
age = 12
status = "Teenager" if 13 <= age <= 19 else "Not a Teenager"

# nesting if condition 

x = 5
result = "Positive" if x > 0 else "Zero" if x == 0 else "Negative"
print(result)

# Logical Operators
# and
# or
# not

# 🔐 Access Control
username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("Access granted.")
else:
    print("Access denied.")

# 🛒 E-commerce Discounts
total_purchase = 4000
first_time_buyer = True

if total_purchase > 5000 or first_time_buyer:
    print("Discount applied!")
else:
    print("No discount available.")

# 📋 Input Validation
user_input = ""

if not user_input:
    print("Input cannot be empty.")