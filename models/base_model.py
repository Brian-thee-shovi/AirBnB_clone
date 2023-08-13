#!/usr/bin/python3
"""import modules"""
from datetime import datetime
import uuid
import models
import json

"""Creating the BaseModel class"""
class BaseModel:
    def __init__(self, *args, **kwargs):
        """Constructor method
        Args:
            args: Arguments
            kwargs: Keyword arguments
        """
        if kwargs:
            if 'id' in kwargs:
                self.id = kwargs['id']
            else:
                self.id = str(uuid.uuid4())
            if 'name' in kwargs:
                self.name = kwargs['name']
            if 'my_number' in kwargs:
                self.my_number = kwargs['my_Number']
            if 'created_at' in kwargs:
                self.created_at = (
                    datetime.strptime(kwargs['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
                )
            else:
                self.created_at = datetime.now()
            if 'updated_at' in kwargs:
                self.updated_at = (
                    datetime.strptime(kwargs['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")
                )
            else:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Return a string representation of the instance"""
        return (
            "[{}] ({}) {}"
            .format(self.__class__.__name__, self.id, self.__dict__)
        )

    def to_dict(self):
        """
        Return a dictionary containing all keys/values of __dict__ of the instance
        """
        my_dict = self.__dict__
        my_dict['created_at'] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        my_dict['updated_at'] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        my_dict.update({'__class__': self.__class__.__name__})
        return my_dict
    
    def save(self):
        """
        Update the public instance attribute 'updated_at' with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()
