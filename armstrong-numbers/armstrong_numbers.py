def is_armstrong(number):
    size = len(str(number))
    s = 0
    n = number
    while(n != 0):
        d = n%10
        s += pow(d, size)
        n = (n - n%10) / 10
    return (number == s)
