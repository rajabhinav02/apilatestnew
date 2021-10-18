import pytest

from api.addbook import AddBook


class Testnow:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.ab = AddBook()

    def test_add(self):
        self.ab.update()
        self.ab.add()
