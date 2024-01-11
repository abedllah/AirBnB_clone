#!/usr/bin/python3

import uuid
from datetime import datetime

class BaseModel:
    def __init__(self):
        self.id = uuid.uuid4()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetinme.now()

    def to_dict(self):
        class_name = self.__class__.__name__
        attributes = self.__dict__.copy()
        attributes['created_at'] = attributes['created_at'].isoformat()
        attributes['updated_at'] = attributes['updated_at'].isoformat()
        attributes['__class__'] = class_name
        return attributes
