#!/usr/bin/python3
"""testing class City"""
import unittest
import datetime
import json
import pep8
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """
    Testing City class implementation
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up for the whole test class
        """
        cls.pep8style = pep8.StyleGuide(quiet=True)
        cls.files = ['models/city.py', 'tests/test_models/test_city.py']

    def test_doc_module(self):
        """
        Module documentation
        """
        doc = City.__doc__
        self.assertGreater(len(doc), 1)

    def test_pep8_conformance(self):
        """
        Test that models/city.py and tests/test_models/test_city.py
        conform to pycodestyle
        """
        result = self.pep8style.check_files(self.files)
        self.assertEqual(
            result.total_errors,
            0,
            "Found code style errors (and warnings).")

    def test_doc_constructor(self):
        """
        Constructor documentation
        """
        doc = City.__init__.__doc__
        self.assertGreater(len(doc), 1)

    def test_class(self):
        """
        Validate the types of attributes
        """
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(City, BaseModel))

        with self.subTest(msg='Attributes'):
            city_instance = City()
            self.assertTrue(hasattr(city_instance, 'name'))
            self.assertTrue(hasattr(city_instance, 'state_id'))
            self.assertIsInstance(city_instance.name, str)
            self.assertIsInstance(city_instance.state_id, str)


if __name__ == '__main__':
    unittest.main()
