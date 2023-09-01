import random
import math

x = float(0)
y = float(0)
laskin = int(0)

lukumaara = int(input("Pisteiden lukumäärä: "))
index = lukumaara

while index > 0:
    index -=1
    x = random.random()
    y = random.random()
    if pow(x, 2) + pow(y, 2) < 1:
        laskin +=1

print("Pi:n arvo: " + str(4 * laskin / lukumaara))