import unittest
from unittest.mock import patch
import fun_with_collections.sort_and_search_list as topic1


class MyTestCase(unittest.TestCase):
    @patch('fun_with_collections.sort_and_search_list.make_list', return_value=[5,31,45])
    def test_item_found(self, input):
        self.assertEqual(topic1.search_list(31), 1)

    @patch('fun_with_collections.sort_and_search_list.make_list', return_value=[5,31,45])
    def test_item_not_found(self, input):
        self.assertEqual(topic1.search_list(15), -1)

    @patch('fun_with_collections.sort_and_search_list.make_list', return_value=[45,31,5])
    def test_sort_list(self, input):
        self.assertEqual(topic1.sort_list(), [5,31,45])


if __name__ == '__main__':
    unittest.main()
