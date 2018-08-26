import string

def rotate(text, key):
    abc = string.ascii_lowercase
    ABC = string.ascii_uppercase

    bca = abc[key:] + abc[:key]
    BCA = ABC[key:] + ABC[:key]

    out = []
    for letter in text:
        if letter.isalpha():
            for x in range(len(abc)):
                if letter == abc[x]:
                    out.append(bca[x])
                elif letter == ABC[x]:
                    out.append(BCA[x])
        else:
            out.append(letter)

    return ''.join(out)


#just remember about maketrans you idiot

def rotate_maketrans(text, key):
    abc = string.ascii_lowercase
    bca = abc[key:] + abc[:key]
    return text.translate(str.maketrans(abc + abc.upper(), bca + bca.upper()))

print(rotate_maketrans("The quick brown fox jumps over the lazy dog.", 13))
