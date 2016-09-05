def mix_up(a,b):
    a_swapped = b[:2] + a[2:]
    b_swapped = a[:2] + b[2:]
    return a_swapped + '' + b_swapped
a = 'dog'
b = 'dinner'
print mix_up(a,b)