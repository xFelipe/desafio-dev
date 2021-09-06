from typing import NamedTuple
from numbers import Number
from collections.abc import Callable

def positive(n: Number):
    return abs(n)

def negative(n: Number):
    return -abs(n)

class TransactionType(NamedTuple):
    name: str
    operation: Callable[[Number], Number]
