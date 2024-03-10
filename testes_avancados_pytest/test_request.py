# registrar uma função de limpeza usando um acessório interno especial chamado request
import tempfile
import pytest
import os

@pytest.fixture(scope="module")
def tmp_file(request):
    temp = tempfile.NamedTemporaryFile(delete=False)
    def create():
        return temp.name

    def cleanup():
        os.remove(temp.name)

    request.addfinalizer(cleanup)
    return create
