#!/usr/bin/python3
"""importing BaseModel"""
from models.base_model import BaseModel

"""creating our City class"""


class City(BaseModel):
    """class attributes"""
    state_id = ""
    name = ""
