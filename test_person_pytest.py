import pytest

from person import Person
import time

class TestPerson():
    @pytest.fixture
    def setup(self):
        self.p1 = Person("zohreh","abbasi")
        self. p2 = Person("amir","big")
        yield "setup"
        time.sleep(2)

    def test_fullname(self,setup):
        assert self.p1.fullname() == "zohreh ABBASI"
        assert self.p1.fullname() == "zohreh abbasi"

    def test_email(self,setup):
        assert self.p2.email() == "amirbig@email.com"
        
