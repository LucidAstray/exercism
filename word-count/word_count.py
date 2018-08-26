import collections as col
import string

def word_count(phrase):

    do_not = list(string.punctuation)
    do_not.remove("'")

    no_pun = {}
    for x in do_not:
        no_pun[x] = ' '

    phrase = phrase.translate(str.maketrans(no_pun)).lower()
    return col.Counter(phrase.split())
