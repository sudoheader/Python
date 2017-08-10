def my_func(f, arg):
    return f(arg)


print(my_func(lambda x: 2 * x * x, 5))
my_func(lambda x: 2 * x * x, 5)

# named function


def polynomial(x):
    return x**2 + 5 * x + 4


print(polynomial(-4))

# lambda
print((lambda x: x**2 + 5 * x + 4)(-4))

a = (lambda x: x * x)(8)
print(a)


def double(x): return x * 2


print(double(7))


def triple(x): return x * 3


def add(x, y): return x + y


print(add(triple(3), 4))


# map and filter
def add_five(x):
    return x + 5


nums = [11, 22, 33, 44, 55]
result = list(map(add_five, nums))
print(result)


# With lambda syntax
nums = [11, 22, 33, 44, 55]

result = list(map(lambda x: x + 5, nums))
print(result)


nums = [11, 22, 33]
a = list(map(lambda x: x * 2, nums))
print(a)


nums = [11, 22, 33, 44, 55]
res = list(filter(lambda x: x % 2 == 0, nums))
print(res)

nums = [1, 2, 5, 8, 3, 0, 7]
res = list(filter(lambda x: x < 5, nums))
print(res)

# Generators


def countdown():
    i = 5
    while i > 0:
        yield i
        i -= 1


for i in countdown():
    print(i)


def is_prime(x):
    if x == 2:
        return 1
    if x % 2 == 0:
        return 0
    max = x**0.5 + 1
    i = 3
    while i <= max:
        if x % i == 0:
            return 0
        i += 2
    return 1


def get_primes():
    num = 2
    while num < 100:
        if is_prime(num):
            yield num
        num += 1


for num in get_primes():
    print(num)


def numbers(x):
    for i in range(x):
        if i % 2 == 0:
            yield i


print(list(numbers(11)))


def make_word():
    word = ""
    for ch in "spam":
        word += ch
        yield word


print(list(make_word()))

# Decorators


def decor(func):
    def wrap():
        print("============")
        func()
        print("============")
    return wrap


def print_text():
    print("Hello world!")


decorated = decor(print_text)
decorated()


def print_text():
    print("Hello world!")


print_text = decor(print_text)


@decor
def print_text():
    print("Hello world!")


# Recursion

# Factorial
def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)


print(factorial(5))


def sum_to(x):
    return x + sum_to(x - 1)


print (sum_to(5))


def is_even(x):
    if x == 0:
        return True
    else:
        return is_odd(x - 1)


def is_odd(x):
    return not is_even(x)


print(is_odd(17))
print(is_even(23))


def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)


print(fib(4))

# Sets
num_set = {1, 2, 3, 4, 5}
word_set = set(["spam", "eggs", "sausage"])

print(3 in num_set)
print("spam" not in word_set)

letters = {"a", "b", "c", "d"}
if "e" not in letters:
    print(1)
else:
    print(2)

nums = {1, 2, 1, 3, 1, 4, 5, 6}
print(nums)
nums.add(-7)
print(nums)
nums.remove(3)
print(nums)
nums = {"a", "b", "c", "d"}
nums.add("z")
print(len(nums))

first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}

print(first | second)  # union
print(first & second)  # intersection
print(first - second)  # difference
print(second - first)
print(first ^ second)  # symmetric difference (XOR)

a = {1, 2, 3}
b = {0, 3, 4, 5}
print(a & b)

from itertools import count

for i in count(3):
    print(i)
    if i >= 11:
        break
from itertools import accumulate, takewhile

nums = list(accumulate(range(8)))
print(nums)
print(list(takewhile(lambda x: x <= 6, nums)))
from itertools import takewhile
nums = [2, 4, 6, 7, 9, 8]
a = takewhile(lambda x: x % 2 == 0, nums)
print(list(a))

from itertools import product, permutations

letters = ("A", "B")
print(list(product(letters, range(2))))
print(list(permutations(letters)))
from itertools import product
a = {1, 2}
print(len(list(product(range(3), a))))

nums = {1, 2, 3, 4, 5, 6}
nums = {0, 1, 2, 3} & nums
nums = filter(lambda x: x > 1, nums)
print(len(list(nums)))


def power(x, y):
    if y == 0:
        return 1
    else:
        return x * power(x, y - 1)


print(power(2, 3))

a = (lambda x: x * (x + 1))(6)
print(a)

nums = [1, 2, 8, 3, 7]
res = list(filter(lambda x: x % 2 == 0, nums))
print(res)
