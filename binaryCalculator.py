x = int(input("Enter your number: "))
if x < 256:
    print(bin(x))
else:
    print("Your value is too high ")

y = int(input("Enter your number: "))
y = int(y)
if y < 256:
    print(bin(x))
else:
    print("Your value is too high")
print("Your answer is", x + y, "the binary is", bin(x + y))
