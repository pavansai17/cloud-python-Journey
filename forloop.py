#Example 1 - Multiplication table using for loop[Nested loop]
for i in range(1,6): 
    for j in range(1,6): 
        print(i*j, end="\t")
    print() 

#Example 2 - Star Pattern Right angle Triangle[nested loop]
for i in range(1,6):
    for j in range(i):
        print("*",end=" ")
    print()

#Example 3 - using loop through lists
fruits=["Apple","banana","mango"]
for fruit in fruits:
    print(fruit)
#Example 4 - using loop through strings
text="Pavan sai teja"
for letter in text:
    print(letter)