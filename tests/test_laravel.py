import unittest

from classes import laravel

class TestLaravel(unittest.TestCase):
    def test_list_int(self):
        result = 3 + 3
        self.assertEqual(result, 6)
    

if __name__ == '__main__':
    unittest.main()