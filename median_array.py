arr = [2,5,1,3,0]
arr.sort()
n = len(arr)
if n%2==0:
    median=arr[n//2]
else:
    median=(arr[n//2-1]+arr[n//2])/2
print("Median:",median)