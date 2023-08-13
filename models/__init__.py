#!/usr/bin/python3
"""Script for Initializing Storage"""
from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
