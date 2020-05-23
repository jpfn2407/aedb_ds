import unittest
from aed_ds.exceptions import NoSuchElementException, DuplicatedKeyException
from aed_ds.dictionaries.hash_table import HashTable

class TestHashTable(unittest.TestCase):
    def setUp(self):
        self.hash_table = HashTable()

    def add_items(self, quantity):
        for i in range(quantity):
            self.hash_table.insert(f"key {i+1}",f"value {i+1}")

    def test_size(self):
        self.assertEqual(self.hash_table.size(), 0)
        self.add_items(1)
        self.assertEqual(self.hash_table.size(), 1) 

