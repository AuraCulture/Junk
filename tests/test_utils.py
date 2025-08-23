import os
import unittest
from junk.utils import file_exists, delete_file

class TestUtils(unittest.TestCase):

    def test_file_exists(self):

        test_file = 'test_file.txt'
        with open(test_file, 'w') as f:
            f.write('This is a test file.')

        self.assertTrue(file_exists(test_file))


        os.remove(test_file)

    def test_delete_file(self):

        test_file = 'test_file_to_delete.txt'
        with open(test_file, 'w') as f:
            f.write('This file will be deleted.')

        delete_file(test_file)
        self.assertFalse(file_exists(test_file))

if __name__ == '__main__':
    unittest.main()
