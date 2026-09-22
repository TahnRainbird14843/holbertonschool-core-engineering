#!/usr/bin/env python3

number = __import__('random').randint(-10000, 10000)
if (number < 0):
    last_digit = (-number) % 10
else:
    last_digit = number % 10

if (last_digit == 0):
    print("Last digit of %s is %s and is 0" % (number, last_digit))
elif (last_digit < 6):
    print("Last digit of %s is %s and is less than 6 and not 0" % (number, last_digit))
else:
    print("Last digit of %s is %s and is greater than 5" % (number, last_digit))
