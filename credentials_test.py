import unittest
from credentials import Credential

class TestCredential(unittest.TestCase):
    """

    """

    def setUp(self):
        self.new_credential = Credential("Google", "Pros", "0000")


    def tearDown(self):
        Credential.credential_list = []

    def test_init(self):
        self.assertEqual(self.new_credential.account_type, "Google")
        self.assertEqual(self.new_credential.user_name, "Pros")
        self.assertEqual(self.new_credential.generate_password, "0000")


    def test_generate_password(self):
        """
        

        """
        self.assertEqual(Credential.password(), Credential.password)


    def test_save_credential(self):
        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credential_list), 1)

    def test_save_multiple_credentials(self):
        self.new_credential.save_credential()
        test_credential = Credential("Gmail", "Patt", "0000")
        test_credential.save_credential()
        self.assertEqual(len(Credential.credential_list), 2)

    def test_display_credential(self):

        self.assertEqual(Credential.display_credentials(), Credential.credential_list)




if __name__ == '__main__':
    unittest.main()
    