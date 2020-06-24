import unittest

from aed_ds.trees.binary_search_tree import BinarySearchTree
from aed_ds.exceptions import NoSuchElementException, DuplicatedKeyException, \
    EmptyTreeException
from aed_ds.tad_iterator import Iterator


class TestBinarySearchTree(unittest.TestCase):
    def setUp(self):
        self.tree = BinarySearchTree()

    def add_items(self, quantity, shift=0):
        for i in range(quantity):
            k = i+1+shift
            v = f"value_{i+1+shift}"
            self.tree.insert(k, v)

    def remove_items(self, quantity, shift=0):
        for i in range(quantity):
            k = i+1+shift
            self.tree.remove(k)

    def remove_elements(self, quantity):
        for _ in range(quantity):
            self.list.remove_last()

    def test_size(self):
        self.assertEqual(self.tree.size(), 0)
        self.add_items(3)
        self.assertEqual(self.tree.size(), 3)

    def test_is_full(self):
        self.assertFalse(self.tree.is_full())

    def test_get(self):
        with self.assertRaises(NoSuchElementException):
            self.tree.get(42)
        self.add_items(3)
        self.assertEqual(self.tree.get(2), "value_2")

    def test_insert(self):
        self.tree.insert(5, "value_5")
        with self.assertRaises(DuplicatedKeyException):
            self.tree.insert(5, "value_5")
        self.assertFalse(type(self.tree.root), "NoneType")    

    def test_update(self):
        with self.assertRaises(NoSuchElementException):
            self.tree.get(3)
        self.add_items(5)
        self.tree.update(3, "new_value_3")
        self.assertEqual(self.tree.get(3), "new_value_3")

    def test_remove(self):
        with self.assertRaises(NoSuchElementException):
            self.tree.get(3)
        self.add_items(5)
        self.tree.remove(3)
        with self.assertRaises(NoSuchElementException):
            self.tree.get(3)

    def test_keys(self):
        self.assertTrue(self.tree.keys().is_empty())
        self.add_items(5)
        self.assertEqual(self.tree.keys().get(0), 1)
        self.assertEqual(self.tree.keys().get(1), 2)
        self.assertEqual(self.tree.keys().get(2), 3)
        self.assertEqual(self.tree.keys().get(3), 4)
        self.assertEqual(self.tree.keys().get(4), 5)

    def test_values(self):
        self.assertTrue(self.tree.values().is_empty())
        self.add_items(5)
        self.assertEqual(self.tree.values().get(0), "value_1")
        self.assertEqual(self.tree.values().get(1), "value_2")
        self.assertEqual(self.tree.values().get(2), "value_3")
        self.assertEqual(self.tree.values().get(3), "value_4")
        self.assertEqual(self.tree.values().get(4), "value_5")

    def test_items(self):
        self.assertTrue(self.tree.items().is_empty())
        self.add_items(5)
        self.assertEqual(self.tree.values().get(0).get_value(), "value_1")
        self.assertEqual(self.tree.values().get(1).get_value(), "value_2")
        self.assertEqual(self.tree.values().get(2).get_value(), "value_3")
        self.assertEqual(self.tree.values().get(3).get_value(), "value_4")
        self.assertEqual(self.tree.values().get(4).get_value(), "value_5")
        self.assertEqual(self.tree.values().get(0).get_key(), 1)
        self.assertEqual(self.tree.values().get(1).get_key(), 2)
        self.assertEqual(self.tree.values().get(2).get_key(), 3)
        self.assertEqual(self.tree.values().get(3).get_key(), 4)
        self.assertEqual(self.tree.values().get(4).get_key(), 5)

    def test_iterator(self):
        self.assertIsInstance(self.tree.iterator(), Iterator)

    def test_get_min_element(self):
        with self.assertRaises(EmptyTreeException):
            self.tree.get_min_element()
        self.tree.insert(2, "value_2")
        self.tree.insert(5, "value_5")
        self.tree.insert(3, "value_3")
        self.tree.insert(4, "value_4")
        self.tree.insert(1, "value_1")
        self.assertEqual(self.tree.get_min_element(), "value_1")

    def test_get_max_element(self):
        with self.assertRaises(EmptyTreeException):
            self.tree.get_max_element()
        self.tree.insert(2, "value_2")
        self.tree.insert(5, "value_5")
        self.tree.insert(3, "value_3")
        self.tree.insert(4, "value_4")
        self.tree.insert(1, "value_1")
        self.assertEqual(self.tree.get_max_element(), "value_5")

    def test_get_root(self):
        with self.assertRaises(EmptyTreeException):
            self.tree.get_root()
        self.tree.insert(5, "value_5")
        self.assertEqual(self.tree.get_root(), "value_5")
        self.tree.insert(2, "value_2")
        self.tree.insert(1, "value_1")
        self.tree.insert(3, "value_3")
        self.tree.insert(7, "value_7")
        self.tree.insert(6, "value_6")
        self.tree.insert(8, "value_8")
        self.assertEqual(self.tree.get_root(), "value_5")
        self.tree.remove(5)
        self.assertEqual(self.tree.get_root(), "value_6")

    def test_height(self):
        with self.assertRaises(EmptyTreeException):
            self.tree.height()
        self.tree.insert(5, "value_5")
        self.assertEqual(self.tree.height(), 1)
        self.tree.insert(2, "value_2")
        self.assertEqual(self.tree.height(), 2)
        self.tree.insert(1, "value_1")
        self.assertEqual(self.tree.height(), 3)
        self.tree.insert(3, "value_3")
        self.tree.insert(7, "value_7")
        self.tree.insert(6, "value_6")
        self.tree.insert(8, "value_8")
        self.assertEqual(self.tree.height(), 3)

    def test_is_empty(self):
        self.assertTrue(self.tree.is_empty())
        self.add_items(3)
        self.assertFalse(self.tree.is_empty())
        self.remove_items(3)
        self.assertTrue(self.tree.is_empty())
