#!/usr/bin/python3
def max_integer(my_list=[]):
    big_int = 0
    count = 0
    for num in my_list:
        count = count + 1
        if count == 0:
            return None
        else:
            if num > big_int:
                big_int = num
            else:
                continue
    return big_int
