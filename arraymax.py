"""
Algorithm Design and Applications: An Example of Pseudo-Code
"""
# Algorithm arrayMax(A, n):
#   Input: An array A storing n >= 1 integers.
#   Output: The maximum element in A.
# currentMax <- A[0] ............2
# for i <- 1 to n - 1 do.........1 + n - 1
#   if currentMax < A[i] then....4(n - 1)
#      currentMax <- A[i]........and 6(n - 1)
# return currentMax..............1
# ---------------------------------------------
# best case: 2 + 1 + n + 4(n - 1) + 1 = 5n
# worst case: 2 + 1 + n + 6(n - 1) + 1 = 7n - 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
def arrayMax(n):
    currentMax = a[0]
    for i in n:
        if currentMax < a[i]:
            currentMax = a[i]
    return currentMax

print arrayMax(a)