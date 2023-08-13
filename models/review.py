#!/usr/bin/python3
"""Import the base model class"""
from models.base_model import BaseModel

"""Creating our Reviewclass"""
class Review(BaseModel):
    """Class attributes"""
    place_id = ""
    user_id = ""
    text = ""
