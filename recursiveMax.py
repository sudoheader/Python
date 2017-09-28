# Algorithm recursiveMax(A, n):
#   Input: An array A storing n >= 1 integers.
#   Output: The maximum element in A.
#   if n = 1 then...................................
#       return A[0].................................
#   return max{recursiveMax(A, n - 1), A[n - 1]}

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
n = 1
def recursiveMax(a, n):
    if n == 1:
        return a[0]
    return max(recursiveMax(a, n - 1), a[n - 1])

print recursiveMax(a, n)