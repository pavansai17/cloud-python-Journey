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