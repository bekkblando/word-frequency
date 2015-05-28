import re
import collections
from collections import OrderedDict


final_order = []


def word_frequency(text):
    clean_text = re.sub(r'[^A-Za-z\s]', "", text).lower().split()
    # print(type(clean_text))
    # print(clean_text)
    word_count = {}
    i = 1
    for word in clean_text:
        if word in word_count:
            word_count[word] = word_count[word] + 1
        else:
            word_count[word] = 1
    new_word_count = OrderedDict(
            reversed(sorted(word_count.items(), key=lambda t: t[1])))
    # while i < 20:
    # final_order.update(next(iter(new_word_count.items())))
    # i += 1
    # print(new_word_count)
    return new_word_count

with open('sample.txt') as file_text:
    text = file_text.read()

# print(word_frequency(text))

for key, value in iter(word_frequency(text).items()):
    list_value = [key, value]
    final_order.append(list_value)
print(final_order[:20])
