#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number[:4] > 5:
    print("Last digit of", number, "is", number[5], "and is greater than 5")
elif number[:4] == 0:
    print("Last digit of", number, "is", number[:5], "and is 0")
else:
    print("Last digit of", number, "is", number[:5], "and is less than 6 and not 0")
