def isFibo(prev, curr, n):
	if curr == n:
		return 'IsFibo'
	elif curr > n:
		return 'IsNotFibo'
	return isFibo(curr, prev + curr, n)

cases = int(input())
for i in range(cases):
	print(isFibo(0, 1, int(input())))