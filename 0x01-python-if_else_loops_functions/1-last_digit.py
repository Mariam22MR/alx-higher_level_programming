#!/usr/bin/python3
import random
import math
number = random.randint(-10000, 10000)
modluse = number % 10 if number > 10 else number % -10
print("Last digit of {:d} is {:d} and is "
        .format(number, modluse), end="")
if modluse > 5:
    print("greater than 5")
elif modluse == 0:
    print("0")
else:
    print("less than 6 and not 0")
