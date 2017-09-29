# Algorithm MaxsubFastest(A):
#   Input: An n-element array A of numbers, indexed from 1 to n.
#   Output: The maximum subarray sum of array A.
# M_0 <- 0  // the initial prefix maximum
# for t <- 1 to n do
#   M_i <- max{0, M_t-1 + A[t]}
# m <- 0    // the maxumum found so far
# for i <- 1 to n do
#   m <- max{m, M_t}
# return m
def maxSubFastest(a):
    m = 0 # the initial prefix maximum
    t = 1
    for t in n:
        m[t] = max(0, m[t - 1] + a[t])
    m = 0
    t = 1
    for t in n:
        m = max(m, m[t])
    return m

n = [1, 2, 3])
maxSubFastest(n)
