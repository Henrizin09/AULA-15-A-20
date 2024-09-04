from minhas_funções import somar
import pytest
def test_somar():
    assert somar(2, 3) == 5
    assert somar(5, 7) == 12
    assert somar(10, -3) == 7

test_somar()