import unittest
from unittest.mock import patch
import array as arr
import fun_with_collections.sort_and_search_array as topic1


class MyTestCase(unittest.TestCase):
    @patch('fun_with_collections.sort_and_search_array.make_list', return_value=[5,31,45])
    def test_item_found(self, input):
        self.assertEqual(topic1.search_array(31), 1)

    @patch('fun_with_collections.sort_and_search_array.make_list', return_value=[5,31,45])
    def test_item_not_found(self, input):
        self.assertEqual(topic1.search_array(15), -1)


if __name__ == '__main__':
    unittest.main()
