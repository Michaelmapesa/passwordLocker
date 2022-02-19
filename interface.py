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



