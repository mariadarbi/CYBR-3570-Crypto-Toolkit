
from __future__ import annotations

import math
import secrets

SECONDS_PER_YEAR = 60 * 60 * 24 * 365.25


def bit_security(operations: int | float) -> float:
    """Convert an attack cost in operations to a bit-security estimate."""
    if operations <= 0:
        raise ValueError('operations must be positive')
    return math.log2(operations)


def brute_force_success_probability(key_bits: int, attempts: int) -> float:
    """Return the probability of brute-force success after a number of attempts."""
    if key_bits <= 0:
        raise ValueError('key_bits must be positive')
    if attempts < 0:
        raise ValueError('attempts cannot be negative')
    return min(attempts / (2 ** key_bits), 1.0)


def brute_force_years(
    key_bits: int,
    keys_per_second: float,
    cores: int = 1,
    targets: int = 1,
    average_case: bool = True
) -> float:
    """Estimate brute-force search time in years under a simplified model."""
    if key_bits <= 0:
        raise ValueError('key_bits must be positive')
    if keys_per_second <= 0:
        raise ValueError('keys_per_second must be positive')
    if cores <= 0 or targets <= 0:
        raise ValueError('cores and targets must be positive')

    attempts = 2 ** key_bits

    if average_case:
        attempts /= 2

    attempts /= cores
    attempts /= targets

    seconds = attempts / keys_per_second
    return seconds / SECONDS_PER_YEAR


def generate_symmetric_key(bits: int = 128) -> bytes:
    """Generate a symmetric key using Python's cryptographic randomness source."""
    if bits <= 0 or bits % 8 != 0:
        raise ValueError('bits must be a positive multiple of 8')

    return secrets.token_bytes(bits // 8)
