import string as st

def is_isogram(string):

    word = []
    for x in string.lower():
        if x in st.ascii_lowercase:
            word.append(x)

    if len(word) > len(set(word)):
        print(string, 'is not an isogram')
    else:
        print(string, ' is an isogram')
