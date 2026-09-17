"""
Module: crypto_toolkit.classical.caesar

Educational implementation of the Caesar cipher.

WARNING: This module is for learning only. Do not use the Caesar cipher
to protect real information.
"""

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def char_to_num(ch: str) -> int:
    """Convert uppercase A-Z to a number 0-25."""
    return ALPHABET.index(ch)


def num_to_char(n: int) -> str:
    """Convert an integer to uppercase A-Z using modulo 26."""
    return ALPHABET[n % 26]


def caesar_encrypt(plaintext: str, shift: int) -> str:
    """Encrypt plaintext with a Caesar shift."""
    result = []

    for ch in plaintext:
        if ch.upper() in ALPHABET:
            is_lower = ch.islower()
            number = char_to_num(ch.upper())
            encrypted = num_to_char(number + shift)

            if is_lower:
                encrypted = encrypted.lower()

            result.append(encrypted)
        else:
            result.append(ch)

    return "".join(result)


def caesar_decrypt(ciphertext: str, shift: int) -> str:
    """Decrypt Caesar ciphertext with a known shift."""
    return caesar_encrypt(ciphertext, -shift)


def brute_force_caesar(ciphertext: str) -> list[tuple[int, str]]:
    """Return all possible Caesar decryptions."""
    candidates = []

    for shift in range(26):
        decrypted = caesar_decrypt(ciphertext, shift)
        candidates.append((shift, decrypted))

    return candidates