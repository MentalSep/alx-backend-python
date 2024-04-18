#!/usr/bin/env python3
"""Module for task 6"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Calculates the sum of elements in a list of integers and floats."""
    return float(sum(mxd_lst))
