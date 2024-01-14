#!/usr/bin/python3
"""testing Filestorage"""
import unittest
import models
import json
import pep8
import contextlib
import os
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.place import Place
from models.state import State
from models.user import User
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """
    Testing the FileStorage
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up for the whole test class
        """
        cls.style = pep8.StyleGuide(quiet=True)
        cls.files = ['models/engine/file_storage.py']

    def test_pep8_FileStorage(self):
        """Tests pycodestyle style"""
        result = self.style.check_files(self.files)
        self.assertEqual(result.total_errors, 0, "Fix pep8")

    def setUp(self):
        """Setting up a class test"""
        self.b1 = BaseModel()
        self.a1 = Amenity()
        self.c1 = City()
        self.p1 = Place()
        self.r1 = Review()
        self.s1 = State()
        self.u1 = User()
        self.storage = FileStorage()
        self.storage.save()
        if not os.path.exists("file.json"):
            os.mknod("file.json")

    def tearDown(self):
        """
        Tears down testing environment
        """
        del self.b1
        del self.a1
        del self.c1
        del self.p1
        del self.r1
        del self.s1
        del self.u1
        del self.storage
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_all(self):
        """
        Check the all
        """
        obj = self.storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, self.storage._FileStorage__objects)

    def test_storage_empty(self):
        """
        Check the storage if it is not empty
        """
        self.assertIsNotNone(self.storage.all())

    def test_storage_all_type(self):
        """
        Check the type of storage
        """
        self.assertEqual(dict, type(self.storage.all()))

    def test_new(self):
        """
        Check the new user
        """
        obj = self.storage.all()
        self.u1.id = 1234
        self.u1.name = "Julien"
        self.storage.new(self.u1)
        key = "{}.{}".format(self.u1.__class__.__name__, self.u1.id)
        self.assertIsNotNone(obj[key])

    def test_check_json_loading(self):
        """
        Checks if methods from Storage Engine work.
        """
        with open("file.json") as f:
            dic = json.load(f)
            self.assertEqual(isinstance(dic, dict), True)

    def test_file_existence(self):
        """
        Checking if methods from Storage Engine work.
        """
        with open("file.json") as f:
            self.assertTrue(len(f.read()) > 0)

    def test_docstrings(self):
        """
        Check the docstrings for each function
        """
        self.assertTrue(FileStorage.all.__doc__)
        self.assertTrue(hasattr(FileStorage, 'all'))
        self.assertTrue(FileStorage.new.__doc__)
        self.assertTrue(hasattr(FileStorage, 'new'))
        self.assertTrue(FileStorage.save.__doc__)
        self.assertTrue(hasattr(FileStorage, 'save'))
        self.assertTrue(FileStorage.reload.__doc__)
        self.assertTrue(hasattr(FileStorage, 'reload'))


if __name__ == '__main__':
    unittest.main()
