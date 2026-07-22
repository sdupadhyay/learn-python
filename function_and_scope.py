def calculate_stats(a, b, c):
    return sum([a, b, c]), max(a, b, c), min(a, b, c)

total, maximum, minimum = calculate_stats(3, 7, 2)
print(total, maximum, minimum)

# *args (Multiple Positional Arguments)
# Allows passing any number of values
# Stored as a tuple
# Useful when the number of inputs is unknown

def marks_report(student, *marks):
    return f"{student}'s Total: {sum(marks)}"

print(marks_report("Alice", 90, 85, 80))

# **kwargs (Multiple Keyword Arguments)
# Accepts named arguments
# Stored as a dictionary
# Useful for flexible data like profiles or settings

def student_profile(**details):
    return details

print(student_profile(name="Alice", age=20, grade="A"))