import random
names_list = []

class Robot(object):
    def __init__(self):
        self.name = generate_unique_robot_name()
    def reset(self):
        self.name = generate_unique_robot_name()

def generate_unique_robot_name():
    name = generate_uppercase_string(2)
    name += generate_digit_string(3)
    if name in names_list:
        return generate_unique_robot_name()
    names_list.append(name)
    return name

def generate_uppercase_string(length):
    r = ""
    for i in range(length):
        r += chr(random.randint(0, 25) + 65)
    return r

def generate_digit_string(length):
    r = ""
    for i in range(length):
        r += str(random.randint(0,9))
    return r
