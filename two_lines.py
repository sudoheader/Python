for i in range(1, 101):
    print("".join([buzzer for number, buzzer in ((3, "Fizz"), (5, "Buzz")) if i % number == 0]) or i)﻿
