# file = open("filename.txt", "r")
# print(file.readlines())
# file.close()
#
# file = open("filename.txt", "r")
#
# for line in file:
#     print(line)
#
# file.close()
#
# file = open("newfile.txt", "w")
# file.write("This has been written to a file")
# file.close()
#
# file = open("newfile.txt", "r")
# print(file.read())
# file.close()
#
# file = open("newfile.txt", "r")
# print("Reading initial contents")
# print(file.read())
# print("Finished")
# file.close()
#
# file = open("newfile.txt", "w")
# file.write("Some new text")
# file.close()
#
# file = open("newfile.txt", "r")
# print("Reading new contents")
# print(file.read())
# print("Finished")
# file.close()
#
# msg = "Hello world!"
# file = open("newfile.txt", "w")
# amount_written = file.write(msg)
# print(amount_written)
# file.close()
#
# try:
#    f = open("filename.txt")
#    print(f.read())
#    print(1 / 0)
# finally:
#    f.close()

with open("filename.txt") as f:
    print(f.read())

try:
    print(1)
    print(20 / 0)
    print(2)
except ZeroDivisionError:
    print(3)
finally:
    print(4)

try:
    with open("test.txt") as f:
        print(f.read())
except:
    print("Error")

try:
    print(1)
    assert 2 + 2 == 5
except AssertionError:
    print(3)
except:
    print(4)

a = [i for i in range(20) if i % 3 == 0]
print(a)

# even = [ 2 * i for i in range(10 ** 100) ]
# print(even)

a = [x * 10 for x in range(5, 9)]
print(a)

nums = [4, 5, 6]
msg = "Numbers: {0} {1} {2}". format(nums[0], nums[1], nums[2])
print(msg)

print("{0}{1}{0}".format("abra", "cad"))

a = "{x}, {y}".format(x=5, y=12)
print(a)

str = "{c}, {b}, {a}".format(a=5, b=9, c=7)
print(str)

print(", ".join(["spam", "eggs", "ham"]))
# prints "spam, eggs, ham"

print("Hello ME".replace("ME", "world"))
# prints "Hello world"

print2("This is a sentence.".startswith("This"))
# prints "True"

print("This is a sentence.".endswith("sentence."))
# prints "True"

print("This is a sentence.".upper())
# prints "THIS IS A SENTENCE."

print("AN ALL CAPS SENTENCE".lower())
# prints "an all caps sentence"

print("spam, eggs, ham".split(", "))
# prints "['spam', 'eggs', 'ham']"

a = "Spam"
b = a.upper()
#b = "SPAM"

print(min(1, 2, 3, 4, 0, 2, 1))
# prints smallest number (minimum) in the list
print(max([1, 4, 9, 2, 5, 6, 8]))
# prints largest number (maximum) in the list
print(abs(-99))
# prints the absolute value of the number
print(abs(42))
# prints the absolute value of the number
print(sum([1, 2, 3, 4, 5]))
#prints the sum of the list

a = min([sum([11, 22]), max(abs(-30), 2)])
print(a)
# prints 30 because 11 + 22 = 33, abs(-30) = 30 and max(30, 2) = 30 so
# min(33, 30) = 30

nums = [55, 44, 33, 22, 11]

if all([i > 5 for i in nums]):
    print("All larger than 5")

if any([i % 2 == 0 for i in nums]):
    print("At least one is even")

for v in enumerate(nums):
    print(v)

'''
>>>
All larger than 5
At least one is even
(0, 55)
(1, 44)
(2, 33)
(3, 22)
(4, 11)
>>>
'''

nums = [-1, 2, -3, 4, -5]
if all([abs(i) < 3 for i in nums]):
print(1)
else:
print(2)

# prints 2


def count_char(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count
