def fix_start(s):
	front = s[0]
	back = s[1:]
	fixed_back = back.replace(front, '**')
	return front + fixed_back
s = 'babbfle'
print fix_start(s)