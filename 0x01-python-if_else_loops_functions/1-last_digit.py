#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    last_num = number % 10
else:
    num = number * -1
    last_num = (num % 10) * -1
if last_num > 5:
    print("{} {} {} {} {}".format('Last digit of', number, 'is', last_num, 'and is greater than 5'))
elif last_num < 6 and last_num != 0:
    print("{} {} {} {} {}".format('Last digit of', number, 'is', last_num, 'and is less than 6 and not 0'))
else:
    print("{} {} {} {} {}".format('Last digit of', number, 'is', last_num, 'and is 0'))

    
