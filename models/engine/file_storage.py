#!/usr/bin/python3

import json
from os.path import isfile
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    FileStorage class
    """
    __file_path = "file.json"
    __objects = {}

    Classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review,
    }

    def all(self):
        """
        return the dictinary objects
        """
        return self.__objects

    def new(self, obj):
        """
        adds a new instance to objects
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        serializes objects to json and saves them to a file
        """
        serialized_objects = {}
        for key, value in self.__objects.items():
            serialized_objects[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """
        deserializes the json from the file and populates objects
        """
        if isfile(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    cls = self.Classes.get(class_name, BaseModel)
                    obj = cls(**value)
                    self.__objects[key] = obj
