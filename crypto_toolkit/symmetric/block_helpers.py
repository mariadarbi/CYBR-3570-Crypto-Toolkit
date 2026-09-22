from cryptography.hazmat.primitives import padding

def blocks(data: bytes, block_size: int = 16) -> list[bytes]:
    return [data[i:i + block_size] for i in range(0, len(data), block_size)]


def show_blocks(data: bytes, block_size: int = 16) -> str:
    return "\n".join(block.hex() for block in blocks(data, block_size))


def xor_bytes(a: bytes, b: bytes) -> bytes:
    return bytes(x ^ y for x, y in zip(a, b))


def hamming_distance(a: bytes, b: bytes) -> int:
    return sum((x ^ y).bit_count() for x, y in zip(a, b))


def pkcs7_pad(data: bytes, block_size_bits: int = 128) -> bytes:
    padder = padding.PKCS7(block_size_bits).padder()
    return padder.update(data) + padder.finalize()


def pkcs7_unpad(data: bytes, block_size_bits: int = 128) -> bytes:
    unpadder = padding.PKCS7(block_size_bits).unpadder()
    return unpadder.update(data) + unpadder.finalize()