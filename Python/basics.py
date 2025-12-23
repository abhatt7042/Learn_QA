# basics.py
# Python fundamentals practice

# -----------------------------
# 1. Variables & Data Types
# -----------------------------
name = "Ankita"
age = 25
is_learning = True
pi = 3.14159

print("Name:", name)
print("Age:", age)
print("Learning Python:", is_learning)
print("Pi:", pi)

# -----------------------------
# 2. Lists & Loops
# -----------------------------
fruits = ["apple", "banana", "cherry"]

print("\nFruits:")
for fruit in fruits:
    print("-", fruit)

# Loop with index
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")

# -----------------------------
# 3. Conditionals
# -----------------------------
temperature = 30

if temperature > 25:
    print("\nIt's a hot day!")
elif temperature > 15:
    print("\nIt's a pleasant day!")
else:
    print("\nIt's cold today!")

# -----------------------------
# 4. Functions
# -----------------------------
def greet_user(user_name):
    """Function to greet a user"""
    return f"Hello, {user_name}! Welcome to Python learning."

print("\n" + greet_user(name))

# -----------------------------
# 5. Simple example: Sum of numbers
# -----------------------------
def sum_numbers(numbers):
    """Return the sum of a list of numbers"""
    total = 0
    for num in numbers:
        total += num
    return total

numbers_list = [10, 20, 30, 40]
print("\nNumbers:", numbers_list)
print("Sum:", sum_numbers(numbers_list))


# -----------------------------
# 6. Bonus: Dictionary
# -----------------------------
person = {"name": "Ankita", "age": 25, "city": "Austin"}

print("\nPerson Info:")
for key, value in person.items():
    print(f"{key}: {value}")
