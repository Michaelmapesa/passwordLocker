from enum import auto
from tabnanny import check
from passwordlock import Person,Credentials

def create_Person(username,password):
    new_person=Person(username,password)
    return new_person

def save_person(person):
    person.save_person()

def display_person():
    return Person.dispay_person()

def login_person(username,password):
    check_person = Credentials.verify_person(username,password)
    return check_person

def create_new_credential(site,username,password):
    new_credential = Credentials(site,username,password)
    return new_credential

def save_credentials(credentials):
    credentials.save_details()

def display_sites_details():
    return Credentials.display_credentials()

def delete_credentials(credentials):
    credentials.delete_credentials()

def verify_credential(site):
    return Credentials.if_credential_exist(site)

def generate_password():
    auto_password=Credentials.generate_password()
    return auto_password

def copy_password(site):
    return Credentials.copy_password(site)







