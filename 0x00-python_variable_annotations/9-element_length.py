#!/usr/bin/env python3
"""Module for task 9"""
from typing import List, Sequence, Iterable, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list containing the lengths of elements in the input list."""
    return [(i, len(i) if isinstance(i, str) else i) for i in lst]
