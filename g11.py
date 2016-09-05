def not_bad(s):
	n = s.find('not')
	b = s.find('bad')
	if n != -1 and b != -1 and b>n:
		s = s[:n] + 'good' + s[b+3:]
	return s
s = 'this dinner is not that bad'
print not_bad(s)