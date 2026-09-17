"""
Module: crypto_toolkit.classical.vigenere

Educational implementation of the Vigenere cipher.

WARNING: This module is for learning only. Do not use the Vigenere cipher
to protect real information.
"""

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def char_to_num(ch: str) -> int:
    """Convert uppercase A-Z to a number 0-25."""
    return ALPHABET.index(ch)


def num_to_char(n: int) -> str:
    """Convert an integer to uppercase A-Z using modulo 26."""
    return ALPHABET[n % 26]


def vigenere_encrypt(plaintext: str, keyword: str) -> str:
    """Encrypt plaintext with a Vigenere cipher."""
    result = []
    key_index = 0

    for ch in plaintext:
        if ch.upper() in ALPHABET:
            is_lower = ch.islower()

            text_num = char_to_num(ch.upper())
            key_char = keyword[key_index % len(keyword)].upper()
            key_num = char_to_num(key_char)

            encrypted = num_to_char(text_num + key_num)

            if is_lower:
                encrypted = encrypted.lower()

            result.append(encrypted)
            key_index += 1
        else:
            result.append(ch)

    return "".join(result)


def vigenere_decrypt(ciphertext: str, keyword: str) -> str:
    """Decrypt Vigenere ciphertext with a known shift."""
    result = []
    key_index = 0

    for ch in ciphertext:
        if ch.upper() in ALPHABET:
            is_lower = ch.islower()

            text_num = char_to_num(ch.upper())
            key_char = keyword[key_index % len(keyword)].upper()
            key_num = char_to_num(key_char)

            decrypted = num_to_char(text_num - key_num)

            if is_lower:
                decrypted = decrypted.lower()

            result.append(decrypted)
            key_index += 1
        else:
            result.append(ch)

    return "".join(result)


def vigenere_analysis(ciphertext: str) -> list[tuple[int, str]]:
    """Return analysis of various lengths of passphrase"""
    # TODO: Implement in Lab 01.
    raise NotImplementedError
