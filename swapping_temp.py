def swap(a, b):
    temp = b
    b = a
    a = temp
    return a, b


a = int(input("Enter value of A:"))
b = int(input("Enter value of B:"))
print("Before swapping a and b is :", a, b)
a, b = swap(a, b)
print("After swapping a and b is :", a, b)