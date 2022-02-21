import random
import string
#import pyperclip
class Person:
    
    person_list = []

    def __init__(self, username, password):
        
        self.username = username
        self.password = password

    def save_person(self):
       
        Person.person_list.append(self)
    

    @classmethod
    def display_person(cls):
        return cls.person_list

    def delete_person(self):
       
        Person.person_list.remove(self)

class Credentials():
    
    credentials_list = []
    @classmethod
    def verify_person(cls,username, password):
       
        a_person = ""
        for person in Person.person_list:
            if(person.username == username and person.password == password):
                    a_person == person.username
        return a_person

    def __init__(self,site,userName, password):
        
        self.site = site
        self.userName = userName
        self.password = password
    
    def save_details(self):
        
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        
        Credentials.credentials_list.remove(self)
    
    @classmethod
    def verify_credential(cls, site):
        
        for credential in cls.credentials_list:
            if credential.site == site:
                return credential
    @classmethod
    def copy_password(cls,site):
        found_credentials = Credentials.verify_credential(site)
        pyperclip.copy(found_credentials.password)

    @classmethod
    def if_credential_exist(cls, site):
        
        for credential in cls.credentials_list:
            if credential.site == site:
                return True
        return False
    @classmethod
    def display_credentials(cls):
        
        return cls.credentials_list

    def generatePassword(stringLength=8):
        password = string.ascii_uppercase + string.ascii_lowercase + string.digits + "~!@#$%^&*"
        return ''.join(random.choice(password) for i in range(stringLength))