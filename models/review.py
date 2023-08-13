#!/usr/bin/python3
"""import base model class"""
from models.base_model import BaseModel

"""Creating our Reviewclass"""
class Review(BaseModel):
    """Class attributes"""
    place_id = ""
    user_id = ""
    text = ""
