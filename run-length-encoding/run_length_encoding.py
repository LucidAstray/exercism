def decode(code):
    decoded = ''
    x = ''

    for i in range(len(code)):
        if code[i].isdigit():
            x += code[i]
        elif len(x) != 0:
            decoded += int(x) * code[i]
            x = ''
        else:
            decoded += code[i]

    return decoded




def encode(code):
    encoded = ''
    x = 0

    for i in range(len(code)):
        if i == len(code) - 1:
            if x == 0:
                encoded +=  code[i]
            else:
                encoded += str(x+1) + code[i]
        elif code[i] != code[i+1]:
            if x == 0:
                encoded += code[i]
            else:
                encoded += str(x+1) + code[i]
                x = 0
        else:
            x += 1

    return encoded
