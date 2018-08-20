import string
def verify(isbn):

    validation=[]

    for num in isbn:
        if num in string.digits:
            validation.append(int(num))
        if num.lower() == 'x':
            validation.append(10)

    for i, num in enumerate(validation):
        if validation[i] > 9:
            if i == 9:
                pass
            else:
                return False
    if len(validation) < 10:
        return False

    for i, num in enumerate(validation):
        validation[i] = num * (10-i)

    return sum(validation) % 11 == 0
