def decode(string):
    decoded = ""
    count = ""
    for char in string:
        if char.isdigit():
            count += char
        else:
            if count == "":
                count = "1"
            for i in range(int(count)):
                decoded += char
            count = ""
    return decoded


def encode(string):
    encoded = ""
    count = 0
    current = None
    for char in string:
        if char == current:
            count += 1
        else:
            if current != None:
                encoded += (str(count) if count > 1 else "") + current
            count = 1
            current = char
    if count >= 1:
        encoded += (str(count) if count > 1 else "") + current
    return encoded
