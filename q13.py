def lensort(l):
    l.sort(key=lambda x : len(x))
    return l
l = ['python', 'c', 'java', 'perl', 'ruby', 'javascript', 'go', 'haskel']

print lensort(l)