#!/usr/bin/python3
import unittest
import os
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = storage
        self.file_path = self.storage._FileStorage__file_path

    def tearDown(self):
        try:
            os.remove(self.file_path)
        except FileNotFoundError:
            pass

    def test_class_properties(self):
        self.assertIsInstance(self.storage, FileStorage)
        self.assertTrue(hasattr(self.storage, "_FileStorage__file_path"))
        self.assertTrue(hasattr(self.storage, "_FileStorage__objects"))

    def test_all(self):
        all_objects = self.storage.all()
        self.assertIsInstance(all_objects, dict)
        self.assertEqual(len(all_objects), 0)

    def test_new(self):
        base = BaseModel()
        key = "{}.{}".format(base.__class__.__name__, base.id)
        all_objects = self.storage.all()
        self.assertIn(key, all_objects.keys())
        self.assertEqual(all_objects[key], base)

    def test_save_reload(self):
        base = BaseModel()
        key = "{}.{}".format(base.__class__.__name__, base.id)

        # Save objects to the file
        self.storage.save()

        # Clear the objects from memory
        self.storage._FileStorage__objects = {}

        # Reload objects from the file
        self.storage.reload()
        reloaded_objects = self.storage.all()

        self.assertIn(key, reloaded_objects.keys())
        reloaded_base = reloaded_objects[key]
        self.assertEqual(reloaded_base.id, base.id)
        self.assertEqual(reloaded_base.created_at, base.created_at)
        self.assertEqual(reloaded_base.updated_at, base.updated_at)

if __name__ == "__main__":
    unittest.main()
