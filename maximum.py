def maximum(lst):
    l = len(lst)
    max = lst[0]
    for i in range(1,l):
        if lst[i]>max:
            max = lst[i]
    return max 


lst = [2, 1, 4, 0, 8, 12]
print(maximum(lst))