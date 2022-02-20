
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

    def tearDown(self):
        Credentials.credentials_list = []

    def test_save_many_sites(self):
        self.new_credentials.save_details()
        test_credential=Credentials("facebook","michaelmapesa","Wanzala8")
        test_credential.save_details()
        self.assertEqual(len(Credentials.credentials_list),2)

    def test_delete_credential(self):
        self.new_credentials.save_details()
        test_credential=Credentials("facebook","michaelmapesa","Wanzala8")
        test_credential.save_details()

        self.new_credential.delete_credentials()
        self.assertEqual(len(Credentials.credential_list),1)

    def test_verify_credential(self):
        self.new_credentials.save_details()
        test_credential=Credentials("facebook","michaelmapesa","Wanzala8")
        test_credential.save_details()

        the_credential=Credentials.verify_credential("facebook")
        self.assertEqual(the_credential.site,test_credential.site)

    def test_credential_exist(self):
        self.new_credentials.save_details()
        the_credential=Credentials("facebook","michaelmapesa","Wanzala8")
        the_credential.save_details()
        Credential_is_found=Credentials.if_credential_exist("facebook")
        self.assertTrue(Credential_is_found)

    def test_display_all_saved_credential(self):
        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)


if __name__=="_main_":
    unittest.main()









