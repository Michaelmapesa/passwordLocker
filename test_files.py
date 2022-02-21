import unittest
from passwordlock import Person
from passwordlock import Credentials

class TestClass(unittest.TestCase):
   
    def setUp(self):
        
        self.new_person = Person('Michaelwa','VyZ3thf2')

    def test_init(self):
        
        self.assertEqual(self.new_person.username,'Michaelwa')
        self.assertEqual(self.new_person.password,'VyZ3thf2')

    def test_save_person(self):
        
        self.new_person.save_person()
        self.assertEqual(len(Person.person_list),1)

class TestCredentials(unittest.TestCase):
    
    def setUp(self):
       
        self.new_credential = Credentials('Youtube','michael_mapesa','Vy5Gij49')
    def test_init(self):
        
        self.assertEqual(self.new_credential.site,'Youtube')
        self.assertEqual(self.new_credential.userName,'michael_mapesa')
        self.assertEqual(self.new_credential.password,'Vy5Gij49')

    def save_credential_test(self):
        
        self.new_credential.save_details()
        self.assertEqual(len(Credentials.credentials_list),1)

    def tearDown(self):
        
        Credentials.credentials_list = []

    def test_save_many_site(self):
        
        self.new_credential.save_details()
        test_credential = Credentials("Facebook","johnboy","Ffh45hfk") 
        test_credential.save_details()
        self.assertEqual(len(Credentials.credentials_list),2)

    def test_delete_credential(self):
        
        self.new_credential.save_details()
        test_credential = Credentials("Facebook","johnboy","Ffh45hfk")
        test_credential.save_details()

        self.new_credential.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_verify_credentialr(self):
       
        self.new_credential.save_details()
        test_credential = Credentials("Facebook","johnboy","Ffh45hfk") 
        test_credential.save_details()

        the_credential = Credentials.verify_credential("Facebook")

        self.assertEqual(the_credential.site,test_credential.site)

    def test_credential_exist(self):
        
        self.new_credential.save_details()
        the_credential = Credentials("Facebook", "johnboy", "Ffh45hfk")  
        the_credential.save_details()
        credential_is_found = Credentials.if_credential_exist("Facebook")
        self.assertTrue(credential_is_found)

    def test_display_all_saved_credentials(self):
       

        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)

if __name__ == "__main__":
    unittest.main()
