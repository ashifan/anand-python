def cumilproduct(l):
	s=[]
	x=1
	for i in l:

		x=x+i
		s.append(x)
	return s
	
print cumilproduct([1,2,3,4])	