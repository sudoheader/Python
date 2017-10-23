def stoogesort(a, i, j):
	n = j - i + 1
	if n == 2:
		if a[i] > a[j]:
			swap(a[i]) and swap(a[j])
	elif n > 2:
		m = n / 3
		stoogesort(a, i, j - m)
		stoogesort(a, i + m, j)
		stoogesort(a, i, j - m)
	return a

def swap(a, i, j):
	if i != j:
		temp = i
		i = j
		j = temp
	return a

def stooge(S):
	return stoogesort(S, 0, len(S) - 1)

a = { 1, 3, -4, 5, 2, -3, 4, 5, -6, 7, -8, 9, 0, 10 }
i = 0
j = len(a) / 2
stooge(a)
