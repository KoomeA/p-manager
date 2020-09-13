import unittest
from user import User


class TestUser(unittest.TestCase):
    """

    """

    def setUp(self):
        """
            method to run before each testcase
        """
        self.new_user = User("Koome", "4444")

    def tearDown(self):
        """
        clean up after each test case runs

        """
        User.user_name = []

    def test_init(self):
        """
        Test if object is initialised

        """

        self.assertEqual(self.new_user.user_name, "Koome")
        self.assertEqual(self.new_user.password, "4444")

    def test_save_user(self):
        """

        """

        self.new_user.save_user()
        self.assertEqual(len(User.user_name),1)

    def test_save_multiple_users(self):

        self.new_user.save_user()
        test_user =User("Pros", "0000")
        test_user.save_user()
        self.assertEqual(len(User.user_name), 2)

    def test_user_exists(self):

        self.new_user.save_user()
        test_user = User("Pros", "0000")
        test_user.save_user()

        user_exists = User.user_exist("Pros")
        self.assertTrue(user_exists)


if __name__ == '__main__':
    unittest.main()
    