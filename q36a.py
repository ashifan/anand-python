a = ['bad', 'app', 'sad', 'mad', 'dab','pge', 'bda', 'ppa', 'das', 'dba']
anagrams = {}
for a in a:
    b = ''.join(sorted(a))
    anagrams[b].append(a)
    anagrams[b] = [a]

anagrams= [v for v in anagrams.values() if len(v) > 1]
print anagrams