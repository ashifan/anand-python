def dup(l):
    s = []
    for i in l:
        if l.count(i)>1 and i not in s:

            
            s.append(i)
    return s
print dup([1,1,2,3,2,4,5,5])