import random

def arpakuutio():
    noppa = 0
    while noppa!=6:
        noppa = random.randint(1, 6)
        print(noppa)
    return noppa

arpakuutio()