def square_of_sum(count):
    y = list(range(count + 1))
    return sum(y)**2


def sum_of_squares(count):
    y = [x**2 for x in range(count + 1)]
    return sum(y)


def difference(count):
    return abs(square_of_sum(count) - sum_of_squares(count))
