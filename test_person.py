import unittest
from person import Person

class PersonTest(unittest.TestCase):
    def setUp(self):
        self.p1 = Person("zohreh","abbasi")
        self. p2 = Person("amir","big")

    def tesrDown(self):
        print("Done!..")

    def test_fullname(self):
        self.assertEqual(self.p1.fullname(),"zohreh ABBASI")
        self.assertEqual(self.p1.fullname(),"zohreh abbasi")

    def test_email(self):
        self.assertEqual(self.p2.email(),"amirbig@email.com")
        

if __name__ == "__main__":
    unittest.main()