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


        