from crypto_toolkit.classical.caesar import caesar_encrypt, caesar_decrypt, brute_force_caesar


def test_caesar_known_value():
    assert caesar_encrypt("ABC XYZ", 3) == "DEF ABC"


def test_caesar_round_trip():
    message = "Attack at dawn!"
    shift = 5
    assert caesar_decrypt(caesar_encrypt(message, shift), shift) == message


def test_brute_force_has_26_candidates():
    candidates = brute_force_caesar("DWWDFN")
    assert len(candidates) == 26
    assert any(candidate == "ATTACK" for _, candidate in candidates)
