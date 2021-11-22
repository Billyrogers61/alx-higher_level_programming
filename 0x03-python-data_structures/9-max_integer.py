#!/usr/bin/python3
def max_integer(my_list=[]):
    big_int = 0
    for num in my_list:
        if num > big_int:
            big_int = num
        else:
            continue
    return big_int
