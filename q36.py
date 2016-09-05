def anagram(a, b):
    a = list(a)
    a.sort()
    b = list(b)
    b.sort()
    return (a == b)
a=['eat', 'ate', 'done', 'tea', 'soup', 'node']
b=['eat', 'ate', 'done', 'tea', 'soup', 'node']
print anagram(a,b)
