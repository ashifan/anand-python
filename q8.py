def cumilsum(l):
	s=[]
	x=0
	for i in l:

		x=x+i
		s.append(x)
	return s
	
print cumilsum([1,2,3,4])	