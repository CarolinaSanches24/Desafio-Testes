import os
import tempfile
import pytest

def is_done(path):
    if not os.path.exists(path):
        return False
    with open(path) as _f:
        contents = _f.read()
    if "yes" in contents.lower():
        return True
    elif "no" in contents.lower():
        return False
    
class TestIsDone:
    @classmethod
    def setup_class(cls):
        cls.tmp_dir = tempfile.mkdtemp()
        cls.tmp_file = os.path.join(cls.tmp_dir, "test_file")

    @classmethod
    def teardown_class(cls):
        os.remove(cls.tmp_file)
        os.rmdir(cls.tmp_dir)

    def test_yes(self):
        with open(self.tmp_file, "w") as _f:
            _f.write("yes")
        assert is_done(self.tmp_file) is True

    def test_no(self):
        with open(self.tmp_file, "w") as _f:
            _f.write("no")
        assert is_done(self.tmp_file) is False