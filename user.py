class User:
    """
    The class generates new instances for users
    """

    def __init__(self, user_name, password):
        """
        method to define properties of the object
        Args:
            user_name: New username.
            password: New password.
        """
        self.user_name = user_name
        self.password = password
    user_name = []

    def save_user(self):
        """
        The method save_user saves objects into the user_name
        """
        User.user_name.append(self)

    @classmethod 
    def user_exist(cls, user_name):
        """
        The method checks if a user exists in the user_names
        """
        for user in cls.user_name:
            if user.user_name == user_name:
                return True
        return False