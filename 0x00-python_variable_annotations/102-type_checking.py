#!/usr/bin/env python3
"""Module for task 12"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Zooms in on an array by repeating each element
    the specified number of times."""
    zoomed_in: List[int] = [item for item in lst for i in range(factor)]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)
zoom_3x = zoom_array(array, 3)
