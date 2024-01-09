#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        top_score = max(a_dictionary)
        return a_dictionary[top_score]
