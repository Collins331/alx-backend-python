#!/usr/bin/env python3
"""
a function that takes in a float argument
and return the floor of the argument
"""


def floor(n: float) -> int:
    """
    returns the floor of n as interger
    """
    res = str(n).split(".")
    return int(res[0])
