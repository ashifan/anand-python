def verbing(s):
    if len(s) >=3:
        if s[-3:] != 'ing': s = s + 'ing'
        else: s = s + 'ly'
    return s
s = 'string'
print verbing(s)