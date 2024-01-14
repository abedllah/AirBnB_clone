#!/usr/bin/python3
"""testing class Review"""
import unittest
import datetime
import json
import pep8
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """
    Testing Review class implementation
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up for the whole test class
        """
        cls.pep8style = pep8.StyleGuide(quiet=True)
        cls.files = ['models/review.py', 'tests/test_models/test_review.py']

    def test_doc_module(self):
        """
        Module documentation
        """
        doc = Review.__doc__
        self.assertGreater(len(doc), 1)

    def test_pep8_conformance(self):
        """
        Test that models/review.py and tests/test_models/test_review.py
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
        doc = Review.__init__.__doc__
        self.assertGreater(len(doc), 1)

    def test_class(self):
        """
        Validating the types of attributes and class
        """
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(Review, BaseModel))

        with self.subTest(msg='Attributes'):
            review_instance = Review()
            self.assertTrue(hasattr(review_instance, 'place_id'))
            self.assertTrue(hasattr(review_instance, 'user_id'))
            self.assertTrue(hasattr(review_instance, 'text'))

            self.assertIsInstance(review_instance.place_id, str)
            self.assertIsInstance(review_instance.user_id, str)
            self.assertIsInstance(review_instance.text, str)


if __name__ == '__main__':
    unittest.main()
