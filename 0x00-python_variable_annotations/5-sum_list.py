#!/usr/bin/env python3

from typing import List
"""
accepts a list argument containing floats
and returning their sum as float
"""


def sum_list(input_list: List[float]) -> float:
    """ sums up the floats variables in the list"""
    sum: float = 0.0
    for i in input_list:
        sum += i
    return sum
