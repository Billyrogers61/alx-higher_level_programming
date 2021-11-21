#!/usr/bin/python3
def element_at(my_list, idx):
    if idx >= len(my_list) or idx < 0:
        return None
    else:
        print("Element at index {} is {}".format(idx, my_list[idx]))
