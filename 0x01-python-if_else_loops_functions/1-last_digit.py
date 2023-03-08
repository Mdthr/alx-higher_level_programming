#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = repr(number)
last = num[-1]
if int(last) > 5:
    print(f"Last digit of {num} is {last} and is greater than 5")
elif int(last) == 0:
    print(f"Last digit of {num} is {last} and is 0")
else:
    print("less than 6 and not 0")
