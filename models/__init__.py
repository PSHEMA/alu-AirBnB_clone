#!/usr/bin/python3
"""init file for models"""

from model.base_model import BaseModel
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
classes = {}
