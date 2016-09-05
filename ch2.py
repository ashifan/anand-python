def median(a):
    a.sort()
    if len(a) % 2 == 1:
        return a[len(a)/2]
    else:
        return (a[len(a)/2-1]+a[len(a)/2])/2
a=[1,2,3,4,5,6,7,8]
print median(a)