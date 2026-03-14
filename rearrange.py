# Re - arranging array first half in ascending order and second order in descending order
def rearrange(arr):
    n = len(arr)
    arr.sort()
    mid = n//2
    first_half = arr[:mid]
    second_half = arr[mid:]
    second_half.reverse()
    result = first_half + second_half
    return result
arr = [2,5,11,5,62,1,5]
print(rearrange(arr))
# Here three things are happening 
# 1.Sort the array
# 2.Entire array is split into two components
# 3.Reverse the second half of the array.