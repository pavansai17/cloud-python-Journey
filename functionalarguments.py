#1 Positional arguments
def full_name(first,last):
    print(f" My name is {first} and my surname is {last}")
full_name('Pavan Sai Teja','Ankala')

#2 Default arguments
#Use when a function has default value for a parameter
def greet(name="Guest"):
    print(f" Hello {name}")
greet()
greet("Pavan")

#3 Keyword Arguments
#arguments are passed using parameter names.
def student_details(name,age,department):
    print(f"My name is {name}.Iam {age} years old. Iam studying Btech final year in {department}")
student_details(name="Pavan Sai Teja",age="20",department="CSE")

#Arbitary Arguments
#Multiple positional Arguments are passed as a tuple
def sum_numbers(*numbers):
    total = sum(numbers)
    print(f"Sum of {total}")
sum_numbers(1,2,3,4,5)

#Multi Keyword Arguments
#Allows passing using a dictionary
def display_info(**info):
    for key,value in info.items():
        print(f"{key}:{value}")

display_info("name= Pavan Sai Teja",age = 20,city= "Tirupathi")
