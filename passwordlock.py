import string
import random

class person:
    person_list=[]
    def _init_(self,username,password):
       self.username = username
       self.password = password

    def _save_person(self):
        person.person_list.append(self)

    @classmethod
    def dispay_person(cls):
        return cls.person_list
        

    
