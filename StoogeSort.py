def stoogesort(L, i, j):
	if L[j] < L[i]:
		L[i], L[j] = L[j], L[i]
	if j - i > 1:
		t = (j - i + 1) // 3
		stoogesort(L, i, j - t)
		# print(L)
		stoogesort(L, i + t, j)
		# print(L)
		stoogesort(L, i, j - t)
		print(L)
	return L

def stooge(L):
    return stoogesort(L, 0, len(L) - 1)

# data = [1, 4, 5, 3, -6, 3, 7, 10, -2, -5, 7, 5, 9, -3, 7]
# stooge(data)
data = [3, 7, 2, 6, 8, 9, 12, 3, 10, 5, 1, 3]
stooge(data)
