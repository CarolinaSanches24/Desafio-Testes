# Trabalhar com escopos

@pytest.fixture(scope="module")
def tmp_file():
    def create(contents):
        temp = tempfile.NamedTemporaryFile(delete=False)
        return temp.name
    return create