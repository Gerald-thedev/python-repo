import random
def presidency(candidate):
    if candidate == 1:
        return 'Tinubu'
    elif candidate == 2:
        return 'Peter Obi'
    elif candidate == 3:
        return 'Amaechi'
    elif candidate == 4:
        return 'Buhari'
    elif candidate == 5:
        return 'Atiku'
    elif candidate == 6:
        return 'Obasanjo'
    elif candidate == 7:
        return 'Goodluck Jonathan'
r = random.randint(1,7)
president = presidency(r)
print(president)
