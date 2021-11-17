#!/usr/bin/python3
def print_last_digit(number):
    if (number > 0):
        last_num = number % 10
        print(last_num, end='')
    elif (number < 0):
        num = number * -1
        last_num = num % 10
        print(last_num, end='')
    else:
        print("{:1d}".format(0), end='')
