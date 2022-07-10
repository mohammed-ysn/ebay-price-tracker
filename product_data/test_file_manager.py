import os
from unittest import TestCase

import file_manager


class TestFileManager(TestCase):
    def test_dump_and_load(self):
        # ARRANGE
        my_dict = {
            'name': 'Yaseen',
            'age': 587,
        }
        f_path = 'test_dump_and_load.pickle'

        # ACT
        file_manager.dump(f_path, my_dict)
        res = file_manager.load(f_path)
        file_manager.remove(f_path)

        # ASSERT
        self.assertDictEqual(res, my_dict)

    def test_remove(self):
        # ARRANGE
        f_path = 'test_remove.txt'
        # create empty file
        open(f_path, 'a').close()

        # ACT
        file_manager.remove(f_path)

        # ASSERT
        self.assertFalse(os.path.exists(f_path))
