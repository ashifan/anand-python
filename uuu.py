def fact(n):
	if n == 1:
		return 1
	else:
		return n * fact(n-1)
a=raw_input('enter the number you want to compute: ')
print fact(int(a))
