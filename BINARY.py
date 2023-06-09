#Write a program for binary search
def Search(arr, x, l, h):
    while l <= h:
        mid = l + (h - l)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = m + 1
        else:
            h = m - 1
    return -1
arr = [10,23,21,19,14,7]
x = 21
r = Search(arr, x, 0, len(arr)-1)
if r != -1:
    print("Element is present at index " , str(r))
else:
    print("Not found")