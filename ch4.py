def mostfrequent(text):
    frequencies = [(c, text.count(c)) for c in set(text)]
    return max(frequencies, key=lambda x: x[1])[0]
s = 'hello world'
print(mostfrequent(s))