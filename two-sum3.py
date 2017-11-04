def twoSum(self, target):
    lookup = {}
    for count, num in enumerate(self):
        try:
            return lookup[num], count
        except KeyError:
            lookup.setdefault(target - num, count)

a = [3, 2, 4]
b = 6
print(twoSum(a, b))
