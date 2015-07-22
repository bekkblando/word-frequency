import re
import collections
from collections import OrderedDict


final_order = []

ignored_words = """the,a,able,about,across,after,all,almost,also,am,among,an,and,any,are,as,at,be,
because,been,but,by,can,cannot,could,dear,did,do,does,either,else,ever,every,
for,from,get,got,had,has,have,he,her,hers,him,his,how,however,i,if,in,into,is,
it,its,just,least,let,like,likely,may,me,might,most,must,my,neither,no,nor,
not,of,off,often,on,only,or,other,our,own,rather,said,say,says,she,should,
since,so,some,than,that,the,their,them,then,there,these,they,this,tis,to,too,
twas,us,wants,was,we,were,what,when,where,which,while,who,whom,why,will,with,
would,yet,you,your"""


def word_frequency(text):
    clean_text = re.sub(r'[^A-Za-z\s]', "", text).lower().split()
    clean_ignored_text = ignored_words.lower().split(',')
    for word in clean_text:
        for ignore_word in ignored_words:
            if word == ignore_word:
                print(word)
                print(ignore_word)
                try:
                    clean_text.remove(word)
                except:
                    pass
            else:
                pass
    print(clean_ignored_text)
    word_count = {}
    i = 1
    for word in clean_text:
        if word in word_count:
            word_count[word] = word_count[word] + 1
        else:
            word_count[word] = 1
    new_word_count = OrderedDict(
            reversed(sorted(word_count.items(), key=lambda t: t[1])))
    return new_word_count

with open('sample.txt') as file_text:
    text = file_text.read()


for key, value in iter(word_frequency(text).items()):
    list_value = [key, value]
    final_order.append(list_value)
print(final_order[:20])
