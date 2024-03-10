# Usar vários argumentos

#Teste para verificar se um objeto tem um atributo,com o uso da função interna hasattr() do Python
import pytest

@pytest.mark.parametrize("item, attribute", [("", "format"), (list(), "append")])
def test_attributes(item, attribute):
    assert hasattr(item, attribute)
