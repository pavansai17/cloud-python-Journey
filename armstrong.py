num =int(input("Enter a value:"))
num_dig= len(str(num))
total = 0
temp = num
while temp > 0:
    digit=temp%10
    total+=digit**num_dig
    temp //=10
if total==num:
    print(num,"is an armstrong number")
else:
    print(num,"is not an armstrong number")
