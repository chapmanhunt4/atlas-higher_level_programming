#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        multi_ret = (0, "None")
        return multi_ret
    else:
        multi_ret = (len(sentence), sentence[0])
        return multi_ret
