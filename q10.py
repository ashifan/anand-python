def unique(l):
	s=[]
	for i in l:
		if i not in s:
				s.append(i)

	return s
print unique([1,2,1,3,2,5])