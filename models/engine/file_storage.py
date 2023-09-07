#!/usr/bin/python3
""" File Storage module """

import json
from models.base_model import BaseModel

class FileStorage:
    """ File storage class """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Return the dictionary """
        return self.__objects

    def new(self, obj):
        """ Add the object """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ Serialize the object """
        serialized = {}
        for key, value in self.__objects.items():
            serialized[key] = value.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(serialized, file)

    def reload(self):
        """ Deserialize the object """
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name = value['__class__']
                    obj = eval(class_name)(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
