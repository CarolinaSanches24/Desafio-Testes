#Usar a parametrização
def test_string_is_digit():
    items = ["No", "1", "10", "33", "Yes"]
    for item in items:
        assert item.isdigit()
        
import pytest

@pytest.mark.parametrize("item", ["No", "1", "10", "33", "Yes"])
def test_string_is_digit(item):
    assert item.isdigit()
    
# Relatórios com aprovação úteis

@pytest.mark.parametrize("item", ["0", "1", "10", "33", "9"])
def test_string_is_digit(item):
    assert item.isdigit()