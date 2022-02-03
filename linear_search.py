def linear_search(lst, ele):
    l = len(lst)
    for i in range(l):
        if lst[i] == ele:
            return i
    return 0


lst = [4, 1, 7, 0, 8, 3, 2]
ele = int(input("Enter the element to search:"))
x = linear_search(lst,ele)
if x:
    print("Element found at", x, "th index")
else:
    print("Element not found")