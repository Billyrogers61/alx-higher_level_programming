#!/usr/bin/python3
def best_score(a_dictionary):
    dict_values = (a_dictionary.values())
    sorted_values = sorted(dict_values)
    dict_keys = a_dictionary.keys()
    for word in dict_keys:
        if a_dictionary[word] == sorted_values[-1]:
            return a_dictionary[word]
