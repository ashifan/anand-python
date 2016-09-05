def front_back(a,b):
	a_middle = len(a) / 2
	b_middle = len(b) / 2
	if len(a) % 2 == 1:
		a_middle = a_middle + 1 
		if len(b) % 2 ==1:
			b_middle = b_middle + 1
	return a[:a_middle] + b[:b_middle] + a[a_middle:] + b[b_middle:]
a = 'asdfg'
b = 'qazxs'
print front_back(a,b)