"""
Module: crypto_toolkit.hashes.hashing

Educational utilities for working with cryptographic hash functions.

WARNING:
These helpers demonstrate correct use of standard hash functions. They do not
turn raw hashes into authentication or password-storage mechanisms.
"""

import hashlib
import hmac
from pathlib import Path


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha3_256_hex(data: bytes) -> str:
    return hashlib.sha3_256(data).hexdigest()


def blake2b_hex(data: bytes, digest_size: int = 32) -> str:
    return hashlib.blake2b(data, digest_size=digest_size).hexdigest()


def hash_file(path: str | Path, algorithm: str = "sha256") -> str:
    raise NotImplementedError("Complete this function")


def compare_digest(a: str, b: str) -> bool:
    return hmac.compare_digest(a, b)
