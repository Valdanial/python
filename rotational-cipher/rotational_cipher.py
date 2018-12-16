def rotate(text, key):
    res = ""
    for char in text:
        if ord(char) in range(65, 91):
            res += chr((ord(char) + key - 65) % 26 + 65)
        elif ord(char) in range(97, 123):
            res += chr((ord(char) + key - 97) % 26 + 97)
        else:
            res += char
    return res
