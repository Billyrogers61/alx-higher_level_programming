#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if None in a_dictionary:
        return a_dictionary
    else:
        dict_keys = a_dictionary.keys()
        for key in dict_keys:
            if a_dictionary[key] == value:
                a_dictionary.pop(key)
            else:
                continue
            return a_dictionary
