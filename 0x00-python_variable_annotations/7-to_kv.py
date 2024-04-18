#!/usr/bin/env python3
"""Module for task 7"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Creates a tuple with a key and the square of the value (int/float)."""
    return k, v**2
