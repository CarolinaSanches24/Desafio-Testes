#Aplicar patch e substituir
import pytest
import os


def test_os(monkeypatch):
    #permite substituir a funcao os.path.exists pela função lambda
    monkeypatch.setattr('os.path.exists', lambda x: False)
    assert os.path.exists('/') is False
    
class SomarNumeros:
    def add(self,a,b):
        return a+b
    
def test_somar_numeros(monkeypatch):
    calc = SomarNumeros();
    
    def custom_add(self,a,b):
        return a*b
    
    monkeypatch.setattr(SomarNumeros,'add',custom_add)
    
    assert calc.add(2,3)==6
    
    # Restaurando o método original após o teste
    monkeypatch.undo()
    
    assert calc.add(2,3)==5 