from ast import Delete
import string
import random
import pyperclip

class Person:
    person_list=[]
    def _init_(self,username,password):
       self.username = username
       self.password = password

    def _save_person(self):
        Person.person_list.append(self)

    @classmethod
    def dispay_person(cls):
        return cls.person_list

    def delete_person(self):
        Person.person_list.remove(self)

class Credentials():
    credentials_list=[]
    @classmethod
    def verify_person(cls,username,password):
        a_person=''
        for person in Person.person_list:
            if(person.username == username and person.password == password):
                a_person == person.username
        return a_person

    def _init_(self,site,username,password):
        self.site=site
        self.username=username
        self.password=password

    def save_credentials(self):
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        Credentials.credentials_list.remove(self)

    @classmethod
    def verify_credential(cls,site):
        for credentials in cls.credentials_list:
            if credentials.site == site:
                return credentials

    @classmethod
    def copy_password(cls,site):
        verified_credentials = Credentials.verify_credential(site)
        pyperclip.copy(verified_credentials.password)

    @classmethod
    def check_credential_exit(cls,site):
        for credential in cls.credentials_list:
            if credential.site == site:
                return True
        return False

    @classmethod
    def display_credentials(cls):
        return cls.credentials_list

    def generate_password(stringLength=8,char=string.ascii_uppercase+string.ascii_lowercase+string.digits):
        gen_pass=''.join(random.choice(char)for _ in range(stringLength))
        return gen_pass





    
