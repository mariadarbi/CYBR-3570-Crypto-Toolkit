import hashlib
import hmac


def sha256_digest(message: bytes) -> bytes:
    """Return the SHA-256 digest of a message."""
    return hashlib.sha256(message).digest()


def hmac_sha256(key: bytes, message: bytes) -> bytes:
    """Generate an HMAC-SHA256 tag using a secret key."""
    return hmac.new(key, message, hashlib.sha256).digest()


def verify_hmac_sha256(
    key: bytes, message: bytes, tag: bytes
) -> bool:
    """Verify an HMAC-SHA256 tag using safe comparison."""
    expected = hmac_sha256(key, message)
    return hmac.compare_digest(expected, tag)