def unique(l):
   x=[]
   key=lambda s:s.lower()
   for i in l:
    x.append(key(i))
   return list(set(x))
l=["python","Python","java","Java"]
print unique(l)