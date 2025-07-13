#Example 1: Basic if-else condition 
age = int(input("Enter your age:"))
if age>=18:
    print("You are eligible to vote!")
else:
    print("You are not eligible to vote!")

#Example 2: if-else-else
marks=int(input("Enter your marks:"))
if marks>=90:
    print("Grade A+")
elif marks>=75:
    print("Grade A")
elif marks>=60:
    print("Grade B")
else :
    print("Grade C or below")

#Example 3: Nested if
number=int(input("Enter a number:"))
if number>=0:
    if number==0:
        print("It is a zero!")
    else:
        print("It is a positive number!")
else:
    print("It is a negative number!")
