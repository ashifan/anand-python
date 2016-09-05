def fun(a):
    b = range(1,a)

    for i in range(1,a+1):
       print "x"*i

    for i in b[::-1]:
        print "x"*i   
fun(a=input("enter limit:"))


