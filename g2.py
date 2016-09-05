def front_x(words):
  x_list = []
  other_list = []
  for w in words:
    if w.startswith('x'):
      x_list.append(w)
    else:
      other_list.append(w)
  return sorted(x_list) + sorted(other_list)

words = ['mix', 'xyz', 'apple', 'xanadu', 'aardvark']
print front_x(words)