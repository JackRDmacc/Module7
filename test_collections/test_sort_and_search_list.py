import unittest
from unittest.mock import patch
import fun_with_collections.sort_and_search_list as topic1


class MyTestCase(unittest.TestCase):
    @patch('fun_with_collections.sort_and_sort_list.make_list', return_value=[5,31,45])
    def test_item_found(self, input):
        self.assertEqual(topic1.search_list(31), 1)

    @patch('fun_with_collections.sort_and_sort_list.make_list', return_value=[5,31,45])
    def test_item_not_found(self, input):
        self.assertEqual(topic1.search_list(15), -1)


if __name__ == '__main__':
    unittest.main()
