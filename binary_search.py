def binary_search(lst, ele):
    start = 0
    end = len(lst)-1
    while start <= end:
        mid = (start+end)//2
        if lst[mid] == ele:
            return mid
        elif lst[mid] > ele:
            end = mid - 1
        else:
            start = mid + 1
    return 0


lst = [1, 2, 3, 4, 5, 6]
ele = int(input("Enter the element to search:"))
x = binary_search(lst, ele)
if x:
    print("Element found at", x, "th index")
else:
    print("Element not found")