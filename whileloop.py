#Example 1: Reverse countdown
i = 5
while i >= 1:
    print("Countdown:", i)
    i -= 1

#Example 2: Sum of first N numbers
n=int(input("Enter a value:"))
i=1
total=0
while i<=n:
    total+=i
    i+=1
print("Total sum is ",total)
#Example 3:Print all Even numbers from 1 to N
i=1
n=int(input("Enter a value:"))
while i<=n:
    if i%2==0:
        print(i)
    i+=1

#Example 4:Infinite Loop
while True:
    name = input("Type 'exit' to stop: ")
    if name == "exit":
        break
    print("You typed:", name)


#Example 5:Prints each value of a string
text=input("Enter a name:")
i=0
while i<len(text):
    print(text[i])
    i+=1
