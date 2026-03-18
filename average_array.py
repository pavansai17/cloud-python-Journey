arr = [2,5,1,3,45]
n=len(arr)
total = 0
for num in range(n):
    total = total+arr[num]
average = total/n
print(average)