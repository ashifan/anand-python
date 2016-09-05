def both_ends(s):
    if len(s) < 2:
        return ''
    first2 = s[0:2]
    last2 = s[-2:]
    return first2 + last2
s = 'spring'
print both_ends(s)