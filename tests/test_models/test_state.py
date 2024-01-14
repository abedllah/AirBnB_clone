#!/usr/bin/python3
"""testing class State"""
import unittest
import datetime
import json
import pep8
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """
    Testing State class implementation
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up for the whole test class
        """
        cls.pep8style = pep8.StyleGuide(quiet=True)
        cls.files = ['models/state.py', 'tests/test_models/test_state.py']

    def test_doc_module(self):
        """
        Module documentation
        """
        doc = State.__doc__
        self.assertGreater(len(doc), 1)

    def test_pep8_conformance(self):
        """
        Test that models/state.py and tests/test_models/test_state.py
        conform to pycodestyle
        """
        result = self.pep8style.check_files(self.files)
        self.assertEqual(result.total_errors, 0, "Found code style errors (and warnings).")

    def test_doc_constructor(self):
        """
        Constructor documentation
        """
        doc = State.__init__.__doc__
        self.assertGreater(len(doc), 1)

    def test_class(self):
        """
        Validating the types of attributes and class
        """
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(State, BaseModel))

        with self.subTest(msg='Attributes'):
            state_instance = State()
            self.assertTrue(hasattr(state_instance, 'name'))

            self.assertIsInstance(state_instance.name, str)


if __name__ == '__main__':
    unittest.main()
