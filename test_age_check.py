from age_check import is_adult
import pytest

def test_adult_true():
    assert is_adult(2001) 

def test_adult_false():
    assert not is_adult(2023)

def test_adult_null():
    with pytest.raises(ValueError):
        is_adult(2030)