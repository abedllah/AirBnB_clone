#!/usr/bin/python3
"""testing Amenity class"""
import unittest
import datetime
import json
import pep8
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """
    Test State for class implementation
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up for the whole test class
        """
        cls.pep8style = pep8.StyleGuide(quiet=True)
        cls.files = ['models/amenity.py', 'tests/test_models/test_amenity.py']

    def test_doc_module(self):
        """
        the Module documentation
        """
        doc = Amenity.__doc__
        self.assertGreater(len(doc), 1)

    def test_pep8_conformance(self):
        """
        Test that models/amenity.py and tests/test_models/test_amenity.py
        conform to pycodestyle
        """
        result = self.pep8style.check_files(self.files)
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_doc_constructor(self):
        """
        the Constructor documentation
        """
        doc = Amenity.__init__.__doc__
        self.assertGreater(len(doc), 1)

    def test_class(self):
        """
        Validate the types of attributes in some class
        """
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(Amenity, BaseModel))

        with self.subTest(msg='Attributes'):
            amenity = Amenity()
            self.assertTrue(hasattr(amenity, 'name'))
            self.assertIsInstance(amenity.name, str)


if __name__ == '__main__':
    unittest.main()
