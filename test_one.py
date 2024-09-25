import unittest

import one

class OneTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(one.add(2,-1),1)
        self.assertEqual(one.add(2,3),5)

    def test_mutiply(self):
        self.assertEqual(one.mutiply(2,1),2)
    def test_divition(self):
        self.assertEqual(one.divition(6,2),3)
        self.assertRaises(ZeroDivisionError,one.divition,3,2)


if __name__ == '__name__':
    unittest.main()