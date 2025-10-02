# Defining a basic function
def say_hello():
    print("Hello, welcome to Python functions!")
say_hello()

# Function with parameters
def greet(name):
    print("Hello,", name)
greet("Pavan")

# Function with return statement
def square(n):
    return n * n
print("Square of 4:", square(4))

# Function with default parameter
def greet_user(name="Guest"):
    print("Welcome,", name)
greet_user()
greet_user("Sai")

# Keyword arguments
def student_info(name, age):
    print("Name:", name, "Age:", age)
student_info(age=20, name="Teja")

# Variable-length arguments
# *args (non-keyworded)
def add_numbers(*numbers):
    total = 0
    for n in numbers:
        total += n
    return total

print("Total:", add_numbers(1, 2, 3, 4))

# **kwargs (keyworded)
def display_info(**details):
    for key, value in details.items():
        print(key, ":", value)

display_info(name="Pavan", course="Cloud + Python")

# Local vs Global variables
x = 50  # global

def demo_scope():
    x = 10  # local
    print("Inside function:", x)

demo_scope()
print("Outside function:", x)

# Modify global variable
count = 0

def increase():
    global count
    count += 1

increase()
print("Updated count:", count)

#  Nested Functions
def outer():
    print("Outer function")

    def inner():
        print("Inner function")

    inner()

outer()

# Docstring example
def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b

print(multiply.__doc__)
print("Multiply result:", multiply(5, 6))
