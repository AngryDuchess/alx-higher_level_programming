#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        return 0, None

    tuple_length = len(sentence)
    first = sentence[0]
    return (tuple_length, first)
