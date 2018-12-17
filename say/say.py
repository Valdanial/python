exceptions = {
    0: "zero",
    1: "one",
    2:"two",
    3:"three",
    4:"four",
    5:"five",
    6:"six",
    7:"seven",
    8:"eight",
    9:"nine",
    10:"ten",
    11:"eleven",
    12:"twelve",
    13:"thirteen",
    14:"fourteen",
    15:"fifteen",
    16:"sixteen",
    17:"seventeen",
    18:"eighteen",
    19:"nineteen"
    }

decades = {
    2: "twenty",
    3: "thirty",
    4: "forty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninety"
}

thousands = [' billion', " million", " thousand", ""]

def say(number):
    if number < 0 :
        raise ValueError("Number to say cannot be negative")
    if number >= 1e12:
        raise ValueError("Number to say cannot be bigger than 1e12")
    if number in exceptions:
        return exceptions[number]
    if number < 100:
        unit = number % 10
        decade = (int)((number - unit) / 10)
        return (str)(decades[decade]) + (("-" + say(unit)) if unit != 0 else "")
    if number < 1000:
        rest = number % 100
        hundred = (int)((number - rest) / 100)
        return (say(hundred) + " hundred" if hundred != 0 else "") + (" and " if hundred != 0 and rest != 0 else "") + (say(rest) if rest != 0 else "")
    split = []
    for i in range(4):
        tmp = number % 1000
        split.insert(0, tmp)
        number = (int)((number - tmp) / 1000)
    res = ""
    for i in range(4):
        if split[i] != 0:
            res += (" " if res != "" else "") + say(split[i]) + thousands[i]
    return res
