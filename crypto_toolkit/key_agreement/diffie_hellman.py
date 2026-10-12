

import hashlib
import hmac


def dh_public(g: int, private: int, p: int) -> int:
    """Calculate a public Diffie-Hellman value."""
    return pow(g, private, p)


def dh_shared(peer_public: int, private: int, p: int) -> int:
    """Calculate a shared secret."""
    return pow(peer_public, private, p)


def discrete_log_bruteforce(g: int, x: int, p: int):
    """Find an exponent using brute force."""
    for a in range(p - 1):
        if pow(g, a, p) == x:
            return a
    return None


def is_generator(g: int, p: int) -> bool:
    """Check whether g generates all nonzero values modulo p."""
    values = {pow(g, k, p) for k in range(1, p)}
    required = set(range(1, p))
    return values == required


def derive_session_key(
    shared_secret: int,
    context: bytes = b"CYBR3570"
) -> bytes:
    """Derive a 32-byte key using HKDF-SHA256."""
    salt = b"CYBR3570 fixed demo salt"

    length = max(1, (shared_secret.bit_length() + 7) // 8)
    ikm = shared_secret.to_bytes(length, "big")

    prk = hmac.new(salt, ikm, hashlib.sha256).digest()

    return hmac.new(
        prk,
        context + b"\x01",
        hashlib.sha256
    ).digest()
