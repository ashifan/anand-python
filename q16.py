def extsort(l):
    l.sort(key=lambda x : ext(x))
    return l



l = ['a.c','c.txt','java.c','perl.py','ruby.c','go.py']

print extsort(l)