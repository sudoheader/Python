# Alogorithm MaxsubSlow(A):
#   Input: An n-element array A of numbers, indexed from 1 to n.
#   Output: The maximum subarray sum of array A.
#   m <- 0 // the maximum found so far
#   for j <- 1 to n do
#       for k <- j to n do
#           s <- 0 // the next partial sum we are computing
#           for i <- j to k do
#               s <- s + A[i]
#           if s > m then
#               m <- s
#   return m

def maxSubSlow():
    m = 0
    j = 1
    for j in n:
        k = j
        for k in n:
            s = 0 # the next partial sum we are computing
            i = j
            for i in k:
                s = s + A[i]
            if s > m:
                m = s
    return m
