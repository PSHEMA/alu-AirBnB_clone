#!/usr/bin/python3
""" Module for Base """

from datetime import datetime
from uuid import uuid4
import json
import models
from models import storage

format_date = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """ Basemodel class """
    def __init__(self, *args, **kwargs):
        """ Initialization of Database """
        if args is not None and len(args) > 0:
            pass
        if kwargs:
            for key, item in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    item = datetime.strptime(item, format_date)
                if key not in ['__class__']:
                    setattr(self, key, item)
        else:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)  # Add the object to the storage

    def __str__(self):
        """str definition"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """save definition"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
