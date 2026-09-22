#!/usr/bin/env python3

number = __import__('random').randint(-10000, 10000)
if (number < 0):
    last_digit = - ((- number) % 10)
else:
    last_digit = number % 10

if (last_digit == 0):
    print("Last digit of {} is {} and is 0".format(number, last_digit))
elif (last_digit < 6):
    print("Last digit of {} is {} and is".format(number, last_digit), end=' ')
    print("less than 6 and not 0")
else:
    print("Last digit of {} is {} and".format(number, last_digit), end=' ')
    print("is greater than 5")
