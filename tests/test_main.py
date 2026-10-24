import os
import tempfile
import unittest

# Ensure the root directory is in the path so we can import loginLib
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import loginLib

class TestLoginSystem(unittest.TestCase):

    def setUp(self):
        # Use a temporary file for credentials
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.temp_file.close()
        loginLib.CREDENTIALS_FILE = self.temp_file.name

    def tearDown(self):
        os.remove(self.temp_file.name)

    def test_register_and_login(self):
        username = "testuser"
        password = "testpass"
        loginLib.register(username, password)

        self.assertTrue(loginLib.login(username, password))
        self.assertFalse(loginLib.login(username, "wrongpass"))

    def test_view_profile(self):
        username = "profileuser"
        password = "profilepass"
        loginLib.register(username, password)

        profile = loginLib.viewProfile(username)
        self.assertEqual(profile[1], username)

    def test_change_password(self):
        username = "changepassuser"
        old_password = "oldpass"
        new_password = "newpass"

        loginLib.register(username, old_password)
        self.assertTrue(loginLib.login(username, old_password))

        loginLib.change_password(username, new_password)
        self.assertFalse(loginLib.login(username, old_password))
        self.assertTrue(loginLib.login(username, new_password))

if __name__ == "__main__":
    unittest.main()
