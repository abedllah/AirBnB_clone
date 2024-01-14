#!/usr/bin/python3
"""testing class User"""
import unittest
import datetime
import json
import pep8
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """
    Testing User class implementation
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up for the whole test class
        """
        cls.pep8style = pep8.StyleGuide(quiet=True)
        cls.files = ['models/user.py', 'tests/test_models/test_user.py']

    def test_doc_module(self):
        """
        Module documentation
        """
        doc = User.__doc__
        self.assertGreater(len(doc), 1)

    def test_pep8_conformance(self):
        """
        Test that models/user.py and tests/test_models/test_user.py
        conform to pycodestyle
        """
        result = self.pep8style.check_files(self.files)
        self.assertEqual(result.total_errors, 0, "Found code style errors (and warnings).")

    def test_doc_constructor(self):
        """
        Constructor documentation
        """
        doc = User.__init__.__doc__
        self.assertGreater(len(doc), 1)

    def test_class(self):
        """
        Validating the types of attributes and class
        """
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(User, BaseModel))

        with self.subTest(msg='Attributes'):
            user_instance = User()
            self.assertTrue(hasattr(user_instance, 'email'))
            self.assertTrue(hasattr(user_instance, 'password'))
            self.assertTrue(hasattr(user_instance, 'first_name'))
            self.assertTrue(hasattr(user_instance, 'last_name'))

            self.assertIsInstance(user_instance.email, str)
            self.assertIsInstance(user_instance.password, str)
            self.assertIsInstance(user_instance.first_name, str)
            self.assertIsInstance(user_instance.last_name, str)


if __name__ == '__main__':
    unittest.main()
