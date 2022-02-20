import unittest
from passwordlock import Person
from passwordlock import Credentials

class TestClass(unittest.TestCase):
    def setUp(self):
        self.new_person=Person('michael','Michael8')

    def test_init(self):
        self.assertEqual(self.new_person.username,'michael')
        self.assertEqual(self.new_person.password,'Michael8')

    def test_save_person(self):
        self.new_person.save_person()
        self.assertEqual(len(Person.person_list),1)
        

