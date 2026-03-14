# Start sum is zero
# Traverse each element of the array
# Add each element sum.
arr = [2,5,1,3,0]
total = 0
for num in arr:
    total = total + num
print("Total sum is:",total)
 # If we want to find the sum of first half of the array then we can find as
arr = [2,5,1,3,0]
mid = len(arr) // 2
total = 0
for i in range(mid):
   total = total + arr[i]
print("Sum of first Half is:",total)
