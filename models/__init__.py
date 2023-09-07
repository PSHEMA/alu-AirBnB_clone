#!/usr/bin/python3

""" Initialization and reload of FileStorag """

from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
