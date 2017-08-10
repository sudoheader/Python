fizz_array = {3: "Fizz", 5: "Buzz"}
fizz_keys = fizz_array.keys()

for i in range(1, 101):
    output = ""
    for key in fizz_keys:
        if i % key == 0:
            output += fizz_array[key]

    if not output:
        output = i

    print output﻿
