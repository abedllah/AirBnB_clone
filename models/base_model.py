#!/usr/bin/python3

"""
Base_model module
"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """
    Defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """initialize variables"""
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        setattr(
                            self, key, datetime.strptime(
                                value, '%Y-%m-%dT%H:%M:%S.%f'))
                    else:
                        setattr(self, key, value)
            self.id = kwargs.get('id', str(uuid.uuid4()))
            self.updated_at = kwargs.get('updated_at', datetime.now())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        method that returns a string representation of an object/instance
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """
        method that updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary representation of the instance."""
        attributes = self.__dict__.copy()
        attributes['__class__'] = self.__class__.__name__
        attributes['created_at'] = attributes['created_at'].isoformat()

        if isinstance(attributes['updated_at'], datetime):
            attributes['updated_at'] = attributes['updated_at'].isoformat()

        return attributes
