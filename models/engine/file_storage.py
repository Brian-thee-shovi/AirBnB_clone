#!/usr/bin/python3
"""Importing modules"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

"""Class to handle storage in a file"""
class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        """
        Adds an object to the dictionary of objects with key as <obj class name>.id
        Args:
            obj: The object to be added
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path)
        """
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as myFile:
            objects_json = {
                k: v.to_dict() for k, v in FileStorage.__objects.items()
            }
            json.dump(objects_json, myFile)

    def reload(self):
        """
        Deserializes the JSON file to __objects (if the file exists)
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding="utf-8") as myFile:
                for k, v in json.load(myFile).items():
                    instance = eval(v['__class__'])(**v)
                    self.__objects[k] = instance

    def all(self):
        """
        Returns the dictionary of objects
        """
        return FileStorage.__objects
