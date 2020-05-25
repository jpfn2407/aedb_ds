import unittest
from aed_ds.exceptions import NoSuchElementException, DuplicatedKeyException
from aed_ds.dictionaries.hash_table import HashTable

class TestHashTable(unittest.TestCase):
    def setUp(self):
        self.hash_table = HashTable()

    def add_items(self, quantity, offset=0):
        for i in range(quantity):
            self.hash_table.insert(f"key {i+1+offset}",f"value {i+1+offset}")

    def remove_items(self, quantity, offset=0):
        for i in range(quantity):
            self.hash_table.remove(f"key {i+1+offset}")        

    def test_size(self):
        self.assertEqual(self.hash_table.size(), 0)
        self.add_items(1)
        self.assertEqual(self.hash_table.size(), 1)
        self.add_items(4,1)
        self.assertEqual(self.hash_table.size(), 5)

    def test_if_full(self):
        self.assertFalse(self.hash_table.is_full())
        self.add_items(101)
        self.assertEqual(self.hash_table.size(), 101)
        self.assertTrue(self.hash_table.is_full())

    def test_get(self):
        self.add_items(4)
        with self.assertRaises(NoSuchElementException):
            self.hash_table.get("key 5")
        self.assertEqual(self.hash_table.get("key 4"), "value 4")       


