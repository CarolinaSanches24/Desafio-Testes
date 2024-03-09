# Adicionar um arquivo com testes para este exercício
# Executar os testes e explorar o relatório
# Mover um teste existente para um acessório

import pytest 
import os

#Código Real
#Recebe uma cadeia de caracteres e retorna um valor booleano
def str_to_bool(string):
    if string.lower() in ['yes', 'y', '1']:
        return True
    elif string.lower() in ['no', 'n', '0']:
        return False
    
#Teste parametrizado com valores verdadeiros
@pytest.mark.parametrize("string", ['Y', 'y', '1', 'YES'])
def test_str_to_bool_true(string):
    assert str_to_bool(string) is True

#Teste parametrizado com valores falsos
@pytest.mark.parametrize("string", ['N', 'n', '0', 'NO'])
def test_str_to_bool_false(string):
    assert str_to_bool(string) is False

#Criação do acessório tempdir
@pytest.fixture
def tmpfile(tmpdir):
    def write():
        file = tmpdir.join("done")
        file.write("1")
        return file.strpath
    return write

#Classe de Teste
class TestFile:

    def test_f(self, tmpfile):
        path = tmpfile()
        with open(path) as _f:
            contents = _f.read()
        assert contents == "1"
    
#Versão anterior da classe de teste
        
# class TestFile:

#     def setup(self):
#         with open("/tmp/done", 'w') as _f:
#             _f.write("1")

#     def teardown(self):
#         try:
#             os.remove("/tmp/done")
#         except OSError:
#             pass

#     def test_done_file(self):
#         with open("/tmp/done") as _f:
#             contents = _f.read()
#         assert contents == "1"