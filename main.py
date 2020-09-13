from user import User
from credentials import Credential
import random

def create_user(user_name, password):
    """
        This creates a new user
    """
    new_user = User(user_name, password)
    return new_user

def save_user(user):
    """
        Will save the user
    """
    user.save_user()


def check_saved_users(user_name):
    """
        Will check if a user exists with the username
    """
    return User.user_exists(user_name)

def add_credential(account_type, user_name, password):
    """
        Will add a new credential
    """
    new_credential = Credential(account_type, user_name, password)
    return new_credential

# here we now save the new credential
def save_credential(credential):
    credential.save_credential()
    

def main():
    print("Welcome to the locker")

    print("Kindly enter a shortcode to proceed; if new enter- 'cn'- to sign up, enter -'log'- to log in or -'q' to exit")
    short_code = input().lower()

    if short_code == 'cn':
        print("Sign up")
        print("Username")
        user_name = input()
        print("password")
        password = input()

        save_user(create_user(user_name, password))
        print('\n')
        print(f"Login details for {user_name} have been saved successfully")
        print('\n')

        print("Exit the application to log in to see your credentials")
        
    elif short_code == 'log':

        print("Fill in the required details")
        print("Enter your username")
        user_name = input()
        print("Enter your password")
        password = input()

    else:
        print("User does not exist, kindly sign up")
    while True:

        print("Welcome")


        print("Follow the instructions to navigate your account; Enter -'act'- to add credentials, -ds- to display credentials, or ext- to exit the application")
        short_code = input().lower()
        if short_code == 'act':
            print("Add credentials")
            print("-"*10)
            print("Account type...")
            account_type = input()
            print("username..")
            user_name = input()



            print("Enter c to create your password or enter g to generate one")
            code = input().lower()

            if code == 'c':
                print("Enter your password")
                password = input()


            elif code == 'g':
                s = "abcdefghijklmnopqrstuvwxyz0123456789"
                password = ''.join(random.choice(s) for _ in range(8))

            else:
                print("Enter a valid code")

            save_credential(add_credential(account_type, user_name, password))
            print('\n')
            print(f"Credentials Account {account_type} account's username {user_name} with password {password} added")
            print('\n')
        
        elif short_code == 'ds':
            if display_credential():
                print("Here is a list of your credentials")
                print('\n')

                for Credential in display_credential():
                    print(f"{Credential.account_type}..{Credential.user_name} ..{Credential.password}")
                    print('\n')

            else:
                print('\n')
                print("You don't have any credentials saved")
        
        elif short_code == 'ext':
            print("Exiting the locker")
            break

        else:

            print("Enter a valid code")


if __name__ == '__main__':
    main()
