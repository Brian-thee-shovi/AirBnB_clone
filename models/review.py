#!/usr/bin/python3
"""import base model class"""
from models.base_model import BaseModel

"""class creation"""


class Review(BaseModel):
    """class attributes"""
    place_id = ""
    user_id = ""
    text = ""
