import sys
def word_count_dict():
    word_count = {}
    with open('alice.txt', 'r') as a:
        for line in a:            
            for word in line.split():
                word = word.lower()
                if not word_count.has_key(word): word_count[word] = 1
                else: word_count[word] = word_count[word] + 1
    return word_count
def print_words():
    word_count = word_count_dict()
    words = sorted(word_count.keys())
    for word in words: print word, word_count[word]

print word_count_dict()
print print_words()