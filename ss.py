def cat(test.txt):
    for f in test.txt:
        for line in open(f):
            print line,