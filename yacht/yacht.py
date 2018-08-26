from collections import Counter

YACHT = (lambda x: 50 if 5 in Counter(x).values() else 0)
ONES = (lambda x: digits(x,1))
TWOS = (lambda x: digits(x,2))
THREES = (lambda x: digits(x,3))
FOURS = (lambda x: digits(x, 4))
FIVES = (lambda x: digits(x, 5))
SIXES = (lambda x: digits(x, 6))
FULL_HOUSE = (lambda x: sum(x) if 2 in Counter(x).values() and 3 in Counter(x).values() else 0)
FOUR_OF_A_KIND = (lambda x: flan(x))
LITTLE_STRAIGHT = (lambda x: 30 if sorted(x) == [1,2,3,4,5] else 0)
BIG_STRAIGHT = (lambda x: 30 if sorted(x) == [2,3,4,5,6] else 0)
CHOICE = (lambda x: sum(x))

def digits(x, digit):
    return digit*x.count(digit)

def flan(x):
    y = Counter(x)
    if 4 in y.values():
        return 4 * list(y.keys())[list(y.values()).index(4)]
    elif 5 in y.values():
        return 4 * x[0]
    else:
        return 0

def score(dice, category):
    return category(dice)
