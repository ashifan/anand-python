def product(l):
	s = 1
	for i in l:
		s = s * i
	return s


def factorial(n):
	p = product(range(1,n+1))
	return p


print factorial(4)