import hashlib
import hmac


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha3_256_hex(data: bytes) -> str:
    return hashlib.sha3_256(data).hexdigest()


def blake2b_hex(data: bytes, digest_size: int = 32) -> str:
    return hashlib.blake2b(data, digest_size=digest_size).hexdigest()


def hash_file(path: str, algorithm: str = "sha256") -> str:
    if algorithm == "sha256":
        hasher = hashlib.sha256()
    elif algorithm == "sha3_256":
        hasher = hashlib.sha3_256()
    elif algorithm == "blake2b":
        hasher = hashlib.blake2b()
    else:
        raise ValueError("Unsupported algorithm")

    with open(path, "rb") as file:
        while True:
            chunk = file.read(8192)
            if not chunk:
                break
            hasher.update(chunk)

    return hasher.hexdigest()


def compare_digest(a: str, b: str) -> bool:
    return hmac.compare_digest(a, b)