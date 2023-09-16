#!/usr/bin/python3
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage


class TestFileStorage(unittest.TestCase):
    ''' Test File storage '''

    def test_FileStorage(self):
        """test_FileStorage"""
        bm = BaseModel()
        self.assertIn("BaseModel." + bm.id, storage.all().keys())


if __name__ == "__main__":
    unittest.main()
