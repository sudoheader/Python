def stoogesort(a, i, j):
	n = j - i + 1 # The size of the subarray we are sorting
	if n == 2:
		if a[i] > a[j]:
			swap(a[i] and a[j])
	elif n > 2:
		m = math.floor(n / 3)
		stoogesort(a, i, j - m) # Sort the first part
		stoogesort(a, i + m, j) # Sort the last part
		stoogesort(a, i, j - m) # Sort the first part again
	return a

def swap(a, i, j):
	if i != j:
		temp = i
		i = j
		j = temp
	return a

def stooge(A):
	return stoogesort(A, 0, len(A) - 1)

a = [ 1, 3, -4, 3, 5, 2, -3, 4, 5, -6, 7, -8, 9, 0, 10 ]
stooge(a)
