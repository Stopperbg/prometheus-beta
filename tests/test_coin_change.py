import pytest
from src.coin_change import coin_change

def test_simple_coin_change():
    assert coin_change([1, 2, 5], 11) == 3  # 5 + 5 + 1
    assert coin_change([2], 3) == -1  # Cannot make change

def test_zero_amount():
    assert coin_change([1, 2, 5], 0) == 0

def test_single_coin():
    assert coin_change([1], 5) == 5
    assert coin_change([5], 5) == 1

def test_multiple_denominations():
    assert coin_change([1, 3, 4], 6) == 2  # 3 + 3
    assert coin_change([2, 5, 10, 1], 27) == 4  # 10 + 10 + 5 + 2

def test_invalid_inputs():
    with pytest.raises(ValueError, match="Coin denominations list cannot be empty"):
        coin_change([], 10)
    
    with pytest.raises(ValueError, match="All coin denominations must be positive"):
        coin_change([1, -2, 5], 10)
    
    with pytest.raises(ValueError, match="All coin denominations must be positive"):
        coin_change([0], 10)

def test_edge_cases():
    # Impossible scenarios
    assert coin_change([2], 3) == -1
    assert coin_change([3], 1) == -1
    
    # Large amount
    assert coin_change([1, 2, 5], 100) == 20  # 20 times coin 5

def test_complex_denominations():
    assert coin_change([186, 419, 83, 408], 6249) == 20  # A more complex scenario