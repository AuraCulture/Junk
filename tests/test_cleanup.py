import os
import unittest
from junk.cleanup import clean_up

class TestCleanupFunctionality(unittest.TestCase):

    def setUp(self):

        self.test_fat_file = 'test_junk.fat'
        with open(self.test_fat_file, 'w') as f:
            f.write('test_file_1.txt\ntest_directory\n')

        with open('test_file_1.txt', 'w') as f:
            f.write('This is a test file.')

        os.mkdir('test_directory')

    def tearDown(self):

        if os.path.exists(self.test_fat_file):
            os.remove(self.test_fat_file)
        if os.path.exists('test_file_1.txt'):
            os.remove('test_file_1.txt')
        if os.path.exists('test_directory'):
            os.rmdir('test_directory')

    def test_clean_up(self):

        clean_up(self.test_fat_file)


        self.assertFalse(os.path.exists('test_file_1.txt'))
        self.assertFalse(os.path.exists('test_directory'))

    def test_empty_fat_file(self):

        with open(self.test_fat_file, 'w') as f:
            f.write('')

        clean_up(self.test_fat_file)


        self.assertTrue(os.path.exists('test_file_1.txt'))
        self.assertTrue(os.path.exists('test_directory'))

if __name__ == '__main__':
    unittest.main()
