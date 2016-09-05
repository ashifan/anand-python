def dup(l):
   s=[]
   for i in l:
       if i in s:
           s.append(i)
   return s
 print dup([1,2,1,3,2,5])