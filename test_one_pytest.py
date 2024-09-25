import one
import pytest

class TestOne:
        
    def test_add(self):
        assert one.add(1,-1)== 0
        assert one.add(7,1)== 8
    def test_divition(self):
        assert one.divition(6,2)== 3
    def test_mutiply(self):
        assert one.mutiply(3,1) == 3