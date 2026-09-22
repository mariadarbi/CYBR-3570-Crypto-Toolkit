from crypto_toolkit.math.modular import mod_add, mod_mul, mod_pow, mod_reduce
from crypto_toolkit.math.gcd import gcd, mod_inverse
from crypto_toolkit.utilities.randomness import shannon_entropy, secure_randbelow

def test_modular_arithmetic():
    assert mod_reduce(42, 9) == 6
    assert mod_reduce(-1, 26) == 25
    assert mod_add(8, 4, 9) == 3
    assert mod_mul(6, 8, 9) == 3
    assert mod_pow(3, 8, 7) == 2

def test_gcd_inverse():
    assert gcd(15, 26) == 1
    assert gcd(14, 26) == 2
    assert mod_inverse(3, 26) == 9
    assert mod_inverse(15, 26) == 7

def test_entropy():
    assert abs(shannon_entropy([0.5, 0.5]) - 1.0) < 1e-9
    assert abs(shannon_entropy([1/256] * 256) - 8.0) < 1e-9

def test_secure_randbelow_range():
    for _ in range(100):
        x = secure_randbelow(10)
        assert 0 <= x < 10
