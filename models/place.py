#!/usr/bin/python3
"""import the base model class"""
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

