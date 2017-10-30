def stoogesort(A, i, j):
    if A[i] > A[j]:
        swap(A[i] and A[j])
    if i + 1 >= j:
        return
    k = math.floor((j - i + 1) / 3)
    stoogesort(A, i, j - k) # first two-thirds
    stoogesort(A, i + k, j) # last two-thirds
    stoogesort(A, i, j - k) # first two-thirds again

def swap(A, i, j):
    if i != j:
        temp = i
        i = j
        j = temp
    return A

def stooge(A):
	return stoogesort(A, 0, len(A) - 1)

a = [ 1, 3, -4, 3, 5, 2, -3, 4, 5, -6, 7, -8, 9, 0, 10 ]
stooge(a)
