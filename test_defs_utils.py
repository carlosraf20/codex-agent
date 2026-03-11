def test_palindrome():
    text = "racecar"
    assert text == text[::-1]


def test_reverse_string():
    text = "python"
    assert text[::-1] == "nohtyp"


def test_uppercase_conversion():
    text = "hello"
    assert text.upper() == "HELLO"
