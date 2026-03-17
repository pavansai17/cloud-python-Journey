def swap(arr,start1,start2,size):
    for i in range(size):
        temp = arr[start1+i]
        arr[start1+i]=arr[start2+i]
        arr[start2+i]=temp
def leftrotate(arr,k,n):
    if k==0 or k==n:
        return
    if k==n-k:
        swap(arr,0,n-k,k)
    if k<n-k:
        swap(arr,0,n-k,k)
        leftrotate(arr,k,n-k)
    else:
        swap(arr,0,n-k,k)
        leftrotate(arr[n-k:],2*k-n,k)
n = 5
arr = [1,2,3,4,5]
k = 2
leftrotate(arr,k,n)
print(arr)
