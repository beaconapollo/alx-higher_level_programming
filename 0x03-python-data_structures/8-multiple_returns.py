#!/usr/bin/python3
def multiple_returns(sentence):
    len = 0
    first = ''
    for c in sentence:
        if len == 0:
            first = c
        len += 1
    return len, first
