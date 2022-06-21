import os
from unittest import TestCase

from file_manager import FileManager


class TestFileManager(TestCase):
    def test_dump_and_load(self):
        # ARRANGE
        my_dict = {
            'name': 'Yaseen',
            'age': 587,
        }
        f_path = 'test_dump_and_load.pickle'

        # ACT
        FileManager.dump(f_path, my_dict)
        res = FileManager.load(f_path)
        FileManager.remove(f_path)

        # ASSERT
        self.assertDictEqual(res, my_dict)

    def test_remove(self):
        # ARRANGE
        f_path = 'test_remove.txt'
        # create empty file
        open(f_path, 'a').close()

        # ACT
        FileManager.remove(f_path)

        # ASSERT
        self.assertFalse(os.path.exists(f_path))