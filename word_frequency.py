import re
import collections
from collections import OrderedDict


def word_frequency(text):
    clean_text = re.sub(r'[^A-Za-z\s]', "", text).lower().split()
    # print(type(clean_text))
    # print(clean_text)
    word_count = {}
    for word in clean_text:
        if word in word_count:
            word_count[word] = word_count[word] + 1
        else:
            word_count[word] = 1
    #new_word_count = OrderedDict(reversed(sorted(word_count.items(), key=lambda t: t[1])))
    #print(new_word_count)
    return word_count

with open('sample.txt') as file_text:
    text = file_text.read()

print(word_frequency(text))
