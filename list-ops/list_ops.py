# Insert ys list at the end of xs.
def append(xs, ys):
    xsl = length(xs)
    delta = 0
    for ysi in ys:
        xs.insert(xsl + delta, ysi)
        delta += 1
    return xs

# Concatenates every list in lists into a big list.
def concat(lists):
    s = []
    for list in lists:
        s = append(s, list)
    return s

# Returns a new list with the elements of xs where function(element)==True. Bascially removes elements in excess. Got it?
def filter_clone(function, xs):
    l = []
    index = 0
    for xsi in xs:
        if function(xsi):
            l.insert(index, xsi)
            index += 1
    return l

# Returns the number of elements in xs.
def length(xs):
    l = 0
    for osef in xs:
        l += 1
    return l

# Applies function for each element of xs.
def map_clone(function, xs):
    l = []
    index = 0
    for xsi in xs:
        l.insert(index, function(xsi))
        index += 1
    return l


def foldl(function, xs, acc):
    r = acc
    for xsi in xs:
        r = function(r, xsi)
    return r


def foldr(function, xs, acc):
    r = acc
    xsl = length(xs) - 1
    index = 0
    while index <= xsl:
        r = function(xs[xsl - index], r)
        index += 1
    return r


def reverse(xs):
    xsl = length(xs) - 1
    l = []
    index = 0
    while index <= xsl:
        l.insert(index, xs[xsl - index])
        index += 1
    return l
