from ast import Delete
import string
import random

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


    
