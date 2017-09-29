# Alogorithm MaxsubFaster(A):
#   Input: An n-element array A of numbers, indexed from 1 to n.
#   Output: The maximum subarray sum of array A.
#   S_0 <- 0 // the initial prefix sum
#   for i <- 1 to n do
#       S_i <- S_i-1 + A[i]
#   m <- 0  // the maximum found so far
#   for j <- 1 to n do
#       for k <- j to n do
#           s <- S_k - S_j-1
#           if s > m then
#               m <- s
#   return m

def maxSubFaster(n):
    S = []
    A = []
    i = 1
    for i in n:
        S[i] = S[i - 1] + A[i]
    m = 0 # the maximum found so far
    for j in n:
        k = j
        for k in n:
            s = S[k] - S[j - 1]
            if s > m:
                m = s
    return m
