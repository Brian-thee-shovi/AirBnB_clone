#!/usr/bin/python3
<<<<<<< HEAD
"""import the base model class"""
=======
"""Import the base model class"""
>>>>>>> b458881c3c2aaff89f059879c2deaa1981e49939
from models.base_model import BaseModel

"""Creating our Place class"""
class Place(BaseModel):
    """Class attributes"""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    city_id = ""
    user_id = ""
    amenity_ids = []  # Unique list of amenity IDs

