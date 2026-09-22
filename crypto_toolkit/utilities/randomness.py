"""Security-focused randomness helpers for CYBR 3570."""

from __future__ import annotations
import math
import secrets
from collections.abc import Iterable

def secure_token_bytes(nbytes: int) -> bytes:
    if nbytes < 0:
        raise ValueError("nbytes must be nonnegative")
    return secrets.token_bytes(nbytes)

def secure_token_hex(nbytes: int) -> str:
    if nbytes < 0:
        raise ValueError("nbytes must be nonnegative")
    return secrets.token_hex(nbytes)

def secure_randbelow(upper_bound: int) -> int:
    if upper_bound <= 0:
        raise ValueError("upper_bound must be positive")
    return secrets.randbelow(upper_bound)

def shannon_entropy(probabilities: Iterable[float]) -> float:
    total = 0.0
    for p in probabilities:
        if p < 0:
            raise ValueError("probabilities cannot be negative")
        if p == 0:
            continue
        total -= p * math.log2(p)
    return total

def random_digit_rejection() -> int:
    while True:
        value = secrets.randbits(8)
        if value < 250:
            return value % 10
