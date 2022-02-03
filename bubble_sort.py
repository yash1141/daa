def bubble_sort(lst):
    l = len(lst)
    for i in range(l):
        for j in range(l):
            if lst[i] < lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst


lst = [4, 1, 7, 0, 8, 3, 2]
print("Before sorting:", lst)
lst = bubble_sort(lst)
print("Before sorting:", lst)