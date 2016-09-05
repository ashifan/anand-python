class reverse_iterator:
    def __init__(self, other):
        self.i = other
        self.n = len(self.i)
    def __iter__(self):
        return self
    def next(self):
        if self.n == 0:
            self.n = self.n - 1
            return i
        else:
            raise StopIteration
for a in reverse_iterator([1, 2, 3,4]):
     print a