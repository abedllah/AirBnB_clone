#!/usr/bin/python3
"""testing class Place"""
import unittest
import datetime
import json
import pep8
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    Testing Place class implementation
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up for the whole test class
        """
        cls.pep8style = pep8.StyleGuide(quiet=True)
        cls.files = ['models/place.py', 'tests/test_models/test_place.py']

    def test_doc_module(self):
        """
        Module documentation
        """
        doc = Place.__doc__
        self.assertGreater(len(doc), 1)

    def test_pep8_conformance(self):
        """
        Test that models/place.py and tests/test_models/test_place.py
        conform to pycodestyle
        """
        result = self.pep8style.check_files(self.files)
        self.assertEqual(result.total_errors, 0, "Found code style errors (and warnings).")

    def test_doc_constructor(self):
        """
        Constructor documentation
        """
        doc = Place.__init__.__doc__
        self.assertGreater(len(doc), 1)

    def test_class(self):
        """
        Validating the types of attributes and class
        """
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(Place, BaseModel))

        with self.subTest(msg='Attributes'):
            place_instance = Place()
            self.assertTrue(hasattr(place_instance, 'city_id'))
            self.assertTrue(hasattr(place_instance, 'user_id'))
            self.assertTrue(hasattr(place_instance, 'name'))
            self.assertTrue(hasattr(place_instance, 'description'))
            self.assertTrue(hasattr(place_instance, 'number_rooms'))
            self.assertTrue(hasattr(place_instance, 'number_bathrooms'))
            self.assertTrue(hasattr(place_instance, 'max_guest'))
            self.assertTrue(hasattr(place_instance, 'price_by_night'))
            self.assertTrue(hasattr(place_instance, 'latitude'))
            self.assertTrue(hasattr(place_instance, 'longitude'))
            self.assertTrue(hasattr(place_instance, 'amenity_ids'))

            self.assertIsInstance(place_instance.city_id, str)
            self.assertIsInstance(place_instance.user_id, str)
            self.assertIsInstance(place_instance.name, str)
            self.assertIsInstance(place_instance.description, str)
            self.assertIsInstance(place_instance.number_rooms, int)
            self.assertIsInstance(place_instance.number_bathrooms, int)
            self.assertIsInstance(place_instance.max_guest, int)
            self.assertIsInstance(place_instance.price_by_night, int)
            self.assertIsInstance(place_instance.latitude, float)
            self.assertIsInstance(place_instance.longitude, float)
            self.assertIsInstance(place_instance.amenity_ids, list)


if __name__ == '__main__':
    unittest.main()
