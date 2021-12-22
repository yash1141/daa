def binary_search(arr, ele):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_number = arr[mid]

        if mid_number == ele:
            return mid

        if mid_number < ele:
            left = mid + 1
        else:
            right = mid - 1

    return -1

lst = [12, 15, 17, 19, 21, 24, 45, 67]
ele = 21
index = binary_search(lst, ele)
if index:
    print(f"Number found at index {index} using binary search")
else:
    print("Number not found")
