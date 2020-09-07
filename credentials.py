class Credential:
    """
    The class generates new instances of Credential
    """

    def __init__(self, account_type, user_name, password):
        """
        init method helps define propertis for objects
            Args:
            account_type: Type of account_type
            user_name: username for the account
            password: the password for the account
        """

        self.account_type = account_type
        self.user_name =  user_name
        self.password = password
    
    credential_list = []

    def generate_password(self):
        """

        """
        s = "abcdefghijklmnopqrstuvwxyz0123456789"
        gen_pass=''.join(random.choices(s) for _ in range(8))
        return gen_pass

    def save_credential(self):
        """
            will save credential objects into the list
        """
        Credential.credential_list.append(self)

    @classmethod
    def display_credentials(cls):
        """
            returns the credential list
        """
        return cls.Credential_list


        