from cipher_rc3373 import cipher_rc3373
import pytest
def test_cipher_with_word():
    example = ['Love',1]
    expected = 'Mpwf'
    actual = cipher_rc3373.cipher(example[0], example[1], encrypt=True)
    assert actual == expected, "Don't work with a single word"
