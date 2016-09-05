def match_end(words):
    count=0
    for word in words:
        if len(word)>=2 and word[0] == word[-1]:
            count=count + 1
    return count
words = ["larry","lill","ashif","dhoni","afia"]
print match_end(words)