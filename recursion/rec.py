def f(n):
	if n == 1:
		return 1
	else:
		print 'N = ',n
		return n * f(n-1)

print f(12)
