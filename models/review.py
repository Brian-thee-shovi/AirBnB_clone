#!/usr/bin/python3
<<<<<<< HEAD
"""import base model class"""
=======
"""Import the base model class"""
>>>>>>> b458881c3c2aaff89f059879c2deaa1981e49939
from models.base_model import BaseModel

"""Creating our Reviewclass"""
class Review(BaseModel):
    """Class attributes"""
    place_id = ""
    user_id = ""
    text = ""
