#!/usr/bin/python3
"""importing the BaseModel class"""
from models.base_model import BaseModel

"""creating user class"""


class User(BaseModel):
    """attributes for the class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
