#!/usr/bin/env python3
"""Module for task 10"""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Returns the first element of a sequence or
    None if the sequence is empty."""
    if lst:
        return lst[0]
    else:
        return None
