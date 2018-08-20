import string

def is_pangram(sentence):
    for x in sentence:
        if x not in string.printable:
            raise Exception('You need to provide a sentence consisting only of ASCII letters')

    check = set(string.ascii_lowercase)

    for x in sentence.lower():
        if x in check:
            check.remove(x)

    return len(check) == 0
