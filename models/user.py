#!/usr/bin/python3
"""importing the BaseModel class"""
from models.base_model import BaseModel

"""Creating user class"""


class User(BaseModel):
    """attributes for the class"""
    password = ""
    email = ""
    first_name = ""
    last_name = ""
