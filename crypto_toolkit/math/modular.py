"""Educational modular arithmetic utilities for CYBR 3570."""

def mod_reduce(a: int, m: int) -> int:
    if m <= 0:
        raise ValueError("modulus must be positive")
    return a % m

def mod_add(a: int, b: int, m: int) -> int:
    return (a + b) % m

def mod_mul(a: int, b: int, m: int) -> int:
    return (a * b) % m

def mod_pow(base: int, exponent: int, modulus: int) -> int:
    if exponent < 0:
        raise ValueError("negative exponents are not supported")
    if modulus <= 0:
        raise ValueError("modulus must be positive")
    return pow(base, exponent, modulus)
