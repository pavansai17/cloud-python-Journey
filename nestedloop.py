#Example : 1
for i in range(1, 3): 
    for j in range(1, 4): 
        print(f"i={i}, j={j}")
#Example : 2
#Printing a rectangle of asterisks
rows = 3
cols = 4
for i in range(rows):
    for j in range(cols):
        print("*", end=" ")
    print()
#Example : 3
# Printing a multiplication table

for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}", end="\t")
    print()
#Example : 4
#Printing a pattern of numbers*
for i in range(1, 4):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

