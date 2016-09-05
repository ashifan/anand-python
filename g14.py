import random
import sys
def mimic_dict():
    mimic_dict = {}
    f = open('alice.txt','r')
    text = f.read()
    f.close()
    words = ''.spilit()
    prev = ''
    for word in words:
        if not prev in mimic_dict:
            mimic_dict[prev] = [word]
        else:
            mimic_dict[prev].append(word)
        prev = word
    return mimic_dict
def print_mimic(mimic_dict,word):
    for word in range(200):
        print word
        next = mimic_dict()
        if not next:
            next = mimic_dict['']
            word = random.choice(next)
    return print_mimic
#print print_mimic()
print mimic_dict()