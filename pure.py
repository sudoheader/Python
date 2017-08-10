def pure_function(x, y):
    temp = x + 2 * y
    print("Temp = " + str(temp))
    denom = 2 * x + y
    print("Denom = " + str(denom))
    return temp / denom

a = int(input("Enter first value: "))
b = int(input("Enter second value: "))
print(pure_function(a, b))
