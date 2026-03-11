import pytest
    
def test_palindrome():
    text = "racecar"
    assert text == text[::-1]
    return False
    #will return false 

def test_reverse_string():
    text = "python"
    assert text[::-1] == 1234
    #not a string but an int
     
def test_uppercase_conversion():
    text = "hello"
    assert text.upper() == "Hello"
    #Validation error Hello is not all caps