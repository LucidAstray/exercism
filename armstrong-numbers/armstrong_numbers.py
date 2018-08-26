def is_armstrong(number):
    x = len(str(number))
    return number == sum(int(y)**x for y in str(number))
