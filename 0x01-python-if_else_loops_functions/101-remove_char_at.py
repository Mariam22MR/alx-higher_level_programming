#!/usr/bin/python3
def remove_char_at(str, n):
    new = ""
    for x, c in enumerate(str):
        if x != n:
            new += c
    return new
