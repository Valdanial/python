def is_armstrong(number):
    number_str = str(number)
    s = 0
    for digit in number_str:
        s += pow(int(digit), len(number_str))
    return (number == s)
