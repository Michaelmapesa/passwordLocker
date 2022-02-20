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

def create_new_credential(site,userName,password):
    new_credential = Credentials(site,userName,password)
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


def main():
    print('')
    print("Hi! Welcome to Password Locker...\n Enter a choice below to proceed. \n a---Sign up for an account \n  b---Login with your account \n")
    letter=input("").lower().strip()
    if letter=="a":
        print("Please sign up for an account")
        print("")
        username=input("Enter your user_name:")
        while True:
            print("You have option either to create your own pass.. or we generate? \n c---Enter your password: \n d---Generate random password")
            option=input().lower().strip()
            if option=='c':
                password=input("Enter password\n")
                break
            elif option=="d":
                password=generate_password()
                break
            else:
                print("Error,try again")

        save_person(create_Person(username,password))
        print("")
        print(f"Your account has been created successful with username: {username} and password: {password}")
        print("")

    elif letter=="b":
        print(" ")
        print("Fill in your account details below:")
        username=input("User name:")
        password=input("password:")
        login=login_person(username,password)
        if login_person==login:
            print("You have successfully login to Password locker")
            print("\n")

    while True:
        print("continue with the below options to proceed. \n e---Create a new credential \n f---Display Credentials \n g--Find a credential \n h---Generate a random password \n i---Delete credential  \n EX---Exit app\n")
        letter=input().lower().strip()
        if letter=="e":
            print("create a new Credential:")
            print("")
            print("Site name..")
            site=input().lower()
            print("enter your site username..")
            userName=input()
            while True:
                print("You have option either to create your own pass.. or we generate? \n c---Enter your password: \n d---Generate random password")
                option=input().lower().strip()
                if option=='c':
                    password=input("Enter password\n")
                    break
                elif option=="d":
                    password=generate_password()
                    break
                else:
                    print("Error,try again")
            save_credentials(create_new_credential(site,userName,password))
            print("\n")
            print(f"the site was created successfully {site},{userName},{password}")
            print('\n')
        elif letter=="f":
            if display_sites_details():
                print("view list of available sites")
                print("\n")
                for site in display_sites_details():
                    print(f"site:")








                











