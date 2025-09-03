

def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    """
def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    """
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])


def test():
    assert encode_shift("hello") == "mjqqt"
    assert encode_shift("world") == "btwqi"
    assert decode_shift("mjqqt") == "hello"
    assert decode_shift("btwqi") == "world"
    assert encode_shift("python") == "udymts"
    assert decode_shift("udymts") == "python"
    assert encode_shift("programming") == "udymts"
    assert decode_shift("udymts") == "programming"
    assert encode_shift("udymts") == "programming"
    assert decode_shift("programming") == "udymts"
    assert encode_shift("udymts") == "programming"
    assert decode_shift("programming") == "udymts"
    assert encode_shift("udymts") == "programming"
    assert decode_shift("programming") == "udymts"
    assert encode_shift("udymts") == "programming"
    assert decode_shift("programming") == "udymts"
    assert encode_shift("udymts") == "programming"
    assert decode_shift("programming") == "udymts"
    assert encode_shift("udymts") == "programming"
    assert decode_shift("programming") == "udymts"
    assert encode_shift("udymts") == "programming"
    assert decode_shift("programming") == "udymts"
    assert encode_shift("udymts") == "programming"
    assert decode_shift("programming") == "udymts"
    assert encode_shift("udymts") == "programming"
    assert decode_shift("programming") == "udymts"
    assert encode_shift("udymts") == "programming"
    assert decode_shift("programming") == "udymts"
    assert encode_shift("udymts") == "programming"
    assert decode_shift("programming") == "udymts"
    assert encode_shift("udymts") == "programming"
    assert decode_shift("programming") == "udymts"
    assert encode_shift("udymts") == "programming"
    assert decode_shift("programming") == "udymts"
    assert encode_shift("udymts") == "programming"
    assert decode_shift("programming") == "udymts"
    assert encode_shift("udymts") == "programming"
    assert decode_shift("programming") == "udymts"
    assert encode_shift("udymts") == "programming"
    assert decode_shift("programming") == "udymts"
    assert encode_shift("udymts") == "programming"
    assert decode_shift("programming") == "udymts"
    assert encode_shift("udymts") == "programming"
    assert decode_shift("programming") == "udymts"
    assert encode_shift("udymts") == "programming"
    assert decode_shift("programming") == "udymts"
    assert encode_shift("udymts") == "programming"
    assert decode_shift("programming") == "udymts"
    assert encode_shift("udymts") == "programming"
    assert decode_shift("programming") == "ud