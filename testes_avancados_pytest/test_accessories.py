# Criar um acessório
import pytest
import tempfile

@pytest.fixture
def tmp_file(): #acessorio
    def create():
        temp = tempfile.NamedTemporaryFile(delete=False)
        return temp.name
    return create

import os

def test_file(tmp_file):
    path = tmp_file()
    assert os.path.exists(path)