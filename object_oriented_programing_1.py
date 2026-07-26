# 🚗 Understanding Classes & Objects in Python (Real-Life Analogies)

class Car:
    def __init__(self, brand, color, engine_type):
        self.brand = brand
        self.color = color
        self.engine_type = engine_type
        self.is_running = False

    def start_engine(self):
        self.is_running = True
        print(f"The {self.color} {self.brand} has started")

    def stop_engine(self):
        self.is_running = False
        print(f"The {self.color} {self.brand} has stopped")


car1 = Car("Tesla", "Red", "Electric")
car2 = Car("Ford", "Blue", "Petrol")

car1.start_engine()
car2.start_engine()
car1.stop_engine()

# Car → Class (blueprint)
# brand, color, engine_type → Attributes
# start_engine(), stop_engine() → Methods
# car1, car2 → Objects

# Class Attributes vs Instance Attributes in Python

# There are two kinds of attributes in Python classes:

# Class Attributes → Shared by all objects of the class
# Instance Attributes → Unique to each object

# 🧠 1. Class Attributes
# Defined outside the __init__ method
# Belong to the class itself
# Shared by all instances
# Real-life example: All cars have 4 wheels → common property

# 🧍 2. Instance Attributes
# Defined inside the __init__ method
# Belong to individual objects
# Each object can have different values
# Real-life example: Each car has a different color or brand

class Car:
    # Class Attribute
    wheels = 4

    def __init__(self, brand, color):
        # Instance Attributes
        self.brand = brand
        self.color = color

car1 = Car("Toyota", "Red")
car2 = Car("BMW", "Black")

print(car1.brand, car1.color, car1.wheels)
print(car2.brand, car2.color, car2.wheels)

# 🏷️ Class Methods in Python (Beginner-Friendly Guide)
# Class methods are special methods in Python that work with the class itself, not with a single object. 
# They are mainly used when an action or change should affect all objects together.

# 📌 A class method is a method that:

# Belongs to the class, not to individual objects
# Works with class-level data
# Uses cls instead of self
# Is defined using the @classmethod decorator

class Car:
    wheels = 4  # Class attribute

    def __init__(self, brand):
        self.brand = brand

    @classmethod
    def change_wheels(cls, new_wheel_count):
        cls.wheels = new_wheel_count

car1 = Car("Toyota")
car2 = Car("BMW")

print(car1.wheels)  # 4
print(car2.wheels)  # 4

Car.change_wheels(6)

print(car1.wheels)  # 6
print(car2.wheels)  # 6


class Company:
    bonus_percentage = 10  # Class attribute

    @classmethod
    def update_bonus(cls, new_bonus):
        cls.bonus_percentage = new_bonus


print(Company.bonus_percentage)  # 10

Company.update_bonus(15)

print(Company.bonus_percentage)  # 15

# 🏭 Factory Methods in Python

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def origin(cls):
        return cls(0, 0)

p1 = Point.origin()
print(p1.x, p1.y)  # 0 0

class IceCream:
    def __init__(self, flavor, size):
        self.flavor = flavor
        self.size = size

    @classmethod
    def default_ice_cream(cls):
        return cls("Vanilla", "Medium")

    def describe(self):
        print(f"This is a {self.size} {self.flavor} ice cream.")

ice1 = IceCream.default_ice_cream().describe()




