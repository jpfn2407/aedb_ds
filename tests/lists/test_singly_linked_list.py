import unittest

from aed_ds.exceptions import EmptyListException, InvalidPositionException
from aed_ds.lists.singly_linked_list import SinglyLinkedList
from aed_ds.lists.singly_linked_list_iterator import SinglyLinkedListIterator
from aed_ds.tad_iterator import Iterator


class TestSinglyLinkedList(unittest.TestCase):
    def setUp(self):
        self.list = SinglyLinkedList()
        
    def add_elements(self, quantity, shift=0):
        for i in range(quantity):
            self.list.insert_last(f"element {i+1+shift}")
    
    def remove_elements(self, quantity):
        for _ in range(quantity):
            self.list.remove_last()

    def test_is_empty(self):
        self.assertTrue(self.list.is_empty())
        self.add_elements(1)
        self.assertFalse(self.list.is_empty())

    def test_size(self):
        self.assertEqual(self.list.size(), 0)
        self.add_elements(3)
        self.assertEqual(self.list.size(), 3)
        self.remove_elements(3)
        self.assertEqual(self.list.size(), 0)

    def test_get_first(self):
        with self.assertRaises(EmptyListException):
            self.list.get_first()
        self.add_elements(3)
        self.assertEqual(self.list.get_first(), "element 1")

    def test_get_last(self):
        with self.assertRaises(EmptyListException):
            self.list.get_last()
        self.add_elements(3)
        self.assertEqual(self.list.get_last(), "element 3")
    
    def test_get(self):
        with self.assertRaises(EmptyListException):
            self.list.get(0)
        self.add_elements(5)
        self.assertEqual(self.list.get(2), "element 3")

    def test_find(self):
        self.assertEqual(self.list.find("empty list"), -1)
        self.add_elements(5)
        self.assertEqual(self.list.find("element 3"), 2)
        self.assertEqual(self.list.find("missing element"), -1)

    def test_insert_first(self):
        self.list.insert_first("element")
        self.assertEqual(self.list.get_first(), "element")
        self.list.make_empty()
        self.add_elements(5)
        self.assertNotEqual(self.list.get_first(), "element")
        self.list.insert_first("element")
        self.assertEqual(self.list.get_first(), "element")

    def test_insert_last(self):
        self.list.insert_first("element")
        self.assertEqual(self.list.get_last(), "element")
        self.list.make_empty()
        self.add_elements(5)
        self.assertNotEqual(self.list.get_last(), "element")
        self.list.insert_last("element")
        self.assertEqual(self.list.get_last(), "element")

    def test_insert(self):
        with self.assertRaises(InvalidPositionException):
            self.list.insert("element X", 42)
        self.list.insert("element 1", 0)
        self.assertEqual(self.list.get_first(), "element 1")
        self.add_elements(4, shift=1)
        self.list.insert("element X", 2)
        self.assertEqual(self.list.get(2), "element X")
        self.list.insert("last element", self.list.size())
        self.assertEqual(self.list.get_last(), "last element")
        with self.assertRaises(InvalidPositionException):
            self.list.insert("element bean", 42)

    def test_remove_first(self):
        with self.assertRaises(EmptyListException):
            self.list.remove_first()
        self.add_elements(5)
        self.list.remove_first()
        self.assertEqual(self.list.get_first(), "element 2")
    
    def test_remove_first_single_element(self):
        self.add_elements(1)
        self.assertEqual(self.list.remove_first(), "element 1")

        with self.assertRaises(EmptyListException):
            self.list.remove_first()

        with self.assertRaises(EmptyListException):
            self.list.get(0)
        
        with self.assertRaises(EmptyListException):
            self.list.get_last()
        
        with self.assertRaises(EmptyListException):
            self.list.get_first()
        
        self.assertTrue(self.list.is_empty())
        
        self.assertEqual(self.list.find("element 1"), -1)
        
        self.add_elements(1)
        self.assertEqual(self.list.get_first(), "element 1")
        self.assertEqual(self.list.get_last(), "element 1")
        self.assertEqual(self.list.remove_first(), "element 1")

    def test_remove_last(self):
        with self.assertRaises(EmptyListException):
            self.list.remove_last()
        self.add_elements(5)
        self.list.remove_last()
        self.assertEqual(self.list.get_last(), "element 4")
    
    def test_remove_last_two_elements(self):
        self.add_elements(2)
        self.assertEqual(self.list.remove_last(), "element 2")

    def test_remove_last_single_element(self):
        self.list.make_empty()
        self.add_elements(1)
        self.assertEqual(self.list.remove_last(), "element 1")

        with self.assertRaises(EmptyListException):
            self.list.remove_last()

        with self.assertRaises(EmptyListException):
            self.list.get(0)
        
        with self.assertRaises(EmptyListException):
            self.list.get_last()
        
        with self.assertRaises(EmptyListException):
            self.list.get_first()
        
        self.assertTrue(self.list.is_empty())
        
        self.assertEqual(self.list.find("element 1"), -1)
        
        self.add_elements(1)
        self.assertEqual(self.list.get_first(), "element 1")
        self.assertEqual(self.list.get_last(), "element 1")
        self.assertEqual(self.list.remove_last(), "element 1")

    def test_remove(self):
        with self.assertRaises(InvalidPositionException):
            self.list.remove(1)
        self.add_elements(5)
        with self.assertRaises(InvalidPositionException):
            self.list.remove(6)
        self.assertEqual(self.list.remove(0), "element 1")
        self.assertEqual(self.list.remove(2), "element 4")
        self.assertEqual(self.list.remove(2), "element 5")

    def test_remove_single_element(self):
        self.list.make_empty()
        self.add_elements(1)
        self.assertEqual(self.list.remove(0), "element 1")
        
        with self.assertRaises(InvalidPositionException):
            self.list.remove(0)

        with self.assertRaises(EmptyListException):
            self.list.get(0)
        
        with self.assertRaises(EmptyListException):
            self.list.get_last()
        
        with self.assertRaises(EmptyListException):
            self.list.get_first()
        
        self.assertTrue(self.list.is_empty())
        
        self.assertEqual(self.list.find("element 1"), -1)
        
        self.add_elements(1)
        self.assertEqual(self.list.get_first(), "element 1")
        self.assertEqual(self.list.get_last(), "element 1")
        self.assertEqual(self.list.remove(0), "element 1")

    def test_make_empty(self):
        self.assertTrue(self.list.is_empty())
        self.add_elements(5)
        self.assertFalse(self.list.is_empty())
        self.list.make_empty()
        self.assertTrue(self.list.is_empty())

    def test_iterator(self):
        self.assertIsInstance(self.list.iterator(), Iterator)
        self.assertIsInstance(self.list.iterator(), SinglyLinkedListIterator)