def square_of_sum(count):
    r = range(count+1)
    s = sum(r,0)
    return pow(s, 2)


def sum_of_squares(count):
    r = range(count+1)
    s = 0
    for i in r:
        s += pow(i, 2)
    return s


def difference(count):
    return square_of_sum(count) - sum_of_squares(count)
