<<<<<<< HEAD
import unittest
from aed_ds.exceptions import NoSuchElementException, DuplicatedKeyException
from aed_ds.dictionaries.hash_table import HashTable

class TestHashTable(unittest.TestCase):
    def setUp(self):
        self.hash_table = HashTable(10)

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
        self.add_items(10)
        self.assertEqual(self.hash_table.size(), 10)
        self.assertTrue(self.hash_table.is_full())

    def test_get(self):
        self.add_items(4)
        with self.assertRaises(NoSuchElementException):
            self.hash_table.get("key 5")
        self.assertEqual(self.hash_table.get("key 4"), "value 4")       


=======
import unittest

from aed_ds.dictionaries.hash_table import HashTable
from aed_ds.exceptions import NoSuchElementException, DuplicatedKeyException


class TestHashTable(unittest.TestCase):
    def setUp(self):
        self.table = HashTable(size=11)

    def insert_items(self, quantity, shift=0):
        for i in range(quantity):
            k = f"key_{i+1+shift}"
            v = f"value_{i+1+shift}"
            self.table.insert(k, v)
    
    def remove_items(self, quantity, shift=0):
        for i in range(quantity):
            k = f"key_{i+1+shift}"
            self.table.remove(k)

    def test_size(self):
        self.assertEqual(self.table.size(), 0)
        self.insert_items(5)
        self.assertEqual(self.table.size(), 5)

    def test_is_full(self):
        self.table = HashTable(size=7)
        self.assertFalse(self.table.is_full())
        self.insert_items(7)
        self.assertTrue(self.table.is_full())
        self.remove_items(1)
        self.assertFalse(self.table.is_full())

    def test_get(self):
        with self.assertRaises(NoSuchElementException):
            self.table.get("missing_key")
        self.insert_items(5)
        self.assertEqual(self.table.get("key_3"), "value_3")
        with self.assertRaises(NoSuchElementException):
            self.table.get("missing_key")
        self.remove_items(1, shift=2)
        with self.assertRaises(NoSuchElementException):
            self.table.get("key_3")
        self.insert_items(1, shift=2)
        self.assertEqual(self.table.get("key_3"), "value_3")

    def test_insert(self):
        self.assertFalse(self.table.has_key("key_1"))
        self.table.insert("key_1", "value_1")
        self.assertTrue(self.table.has_key("key_1"))
        with self.assertRaises(DuplicatedKeyException):
            self.table.insert("key_1", "value_1")
        self.assertEqual(self.table.get("key_1"), "value_1")

    def test_update(self):
        with self.assertRaises(NoSuchElementException):
            self.table.update("key_1", "new_value_1")
        self.insert_items(1)
        self.assertEqual(self.table.get("key_1"), "value_1")
        self.table.update("key_1", "new_value_1")
        self.assertEqual(self.table.get("key_1"), "new_value_1")

    def test_remove(self):
        with self.assertRaises(NoSuchElementException):
            self.table.remove("missing_key")
        self.insert_items(1)
        self.assertEqual(self.table.remove("key_1"), "value_1")
        with self.assertRaises(NoSuchElementException):
            self.table.remove("key_1")
        self.insert_items(5)
        self.assertEqual(self.table.remove("key_3"), "value_3")

    def test_keys(self):
        self.assertEqual(self.table.keys().size(), 0)
        self.insert_items(5)
        self.assertEqual(self.table.keys().size(), 5)
        self.assertNotEqual(self.table.keys().find("key_1"), -1)

    def test_values(self):        
        self.assertEqual(self.table.values().size(), 0)
        self.insert_items(5)
        self.assertEqual(self.table.values().size(), 5)
        self.assertNotEqual(self.table.values().find("value_1"), -1)

    def test_items(self):
        self.assertEqual(self.table.items().size(), 0)
        self.insert_items(5)
        self.assertEqual(self.table.items().size(), 5)
        it = self.table.items().iterator()
        while it.has_next():
            item = it.next()
            self.assertIn(item.get_key(), [f"key_{i+1}" for i in range(5)])
            self.assertIn(item.get_value(), [f"value_{i+1}" for i in range(5)])
>>>>>>> upstream/develop
