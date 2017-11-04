def fib(num):
    if(n == 0):
        return 0
    elif(n == 1):
        return 1
    else:
        x = fib(n - 1)
        y = fib(n - 2)
        return x + y

n = "Enter a number to return fibonacci number at index"
print(fib(int(input(n))))
