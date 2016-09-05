def sort_last(tuples):
    return sorted(tuples, key = last)
tuples = [(1, 7), (1, 3), (3, 4, 5), (2, 2)]
print sort_last(tuples)