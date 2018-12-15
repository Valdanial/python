# Score categories
# Change the values as you see fit
YACHT = lambda dice: 50 if yacht(dice) else 0
ONES = lambda dice: dice.count(1)
TWOS = lambda dice: 2 * dice.count(2)
THREES = lambda dice: 3 * dice.count(3)
FOURS = lambda dice: 4 * dice.count(4)
FIVES = lambda dice: 5 * dice.count(5)
SIXES = lambda dice: 6 * dice.count(6)
FULL_HOUSE = lambda dice: sum(dice) if full_house(dice) else 0
FOUR_OF_A_KIND = lambda dice: four_of_a_kind(dice)
LITTLE_STRAIGHT = lambda dice: 30 if straight(dice, 1) else 0
BIG_STRAIGHT = lambda dice: 30 if straight(dice, 2) else 0
CHOICE = lambda dice: sum(dice)

def score(dice, category):
    dice.sort()
    return category(dice)

def full_house(dice):
    for i in range(1, 7):
        if dice.count(i) == 1 or dice.count(i) == 4 or dice.count(i) == 5:
            return False
    return True

def four_of_a_kind(dice):
    for i in range(1 ,7):
        if dice.count(i) >= 4:
            return 4 * i
    return False

def straight(dice, i):
    for die in dice:
        if die != i :
            return False
        i += 1
    return True

def yacht(dice):
    for i in range(1 ,7):
        if dice.count(i) == 5:
            return True
    return False
