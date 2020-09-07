from user import User
from credentials import Credential
import random

def create_user(user_name, password):
    """
        This creates a new user
    """
    new_user = User(user_name, password)
    return new_user

