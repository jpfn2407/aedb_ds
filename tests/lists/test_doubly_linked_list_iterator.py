import unittest

from aed_ds.lists.doubly_linked_list import DoublyLinkedList
from aed_ds.exceptions import NoSuchElementException

class TestDoublyLinkedListIterator(unittest.TestCase):
    def setUp(self):
        self.list = DoublyLinkedList()
        self.iterator = self.list.iterator()

    def add_elements(self, quantity, shift=0):
        for i in range(quantity):
            self.list.insert_last(f"element {i+1+shift}")
        self.iterator = self.list.iterator()    

    def test_has_next(self):
        # 0 elements
        self.assertFalse(self.iterator.has_next())

        # 1 elements
        self.add_elements(1)
        self.assertTrue(self.iterator.has_next())

        # 2 elements
        self.add_elements(1)
        self.assertTrue(self.iterator.has_next())

        # 5 elements
        self.add_elements(3)
        self.assertTrue(self.iterator.has_next())

        # iterate to the end and test
        for _ in range(5):
            self.assertTrue(self.iterator.has_next())
            self.iterator.next()
        self.assertFalse(self.iterator.has_next())

        # clear list        
        self.list.make_empty()
        self.iterator = self.list.iterator()
        self.assertFalse(self.iterator.has_next())
    
    def test_has_next_alternative(self):
        doubly_linked_list = DoublyLinkedList()
        it = doubly_linked_list.iterator()
        self.assertFalse(it.has_next())
        doubly_linked_list.insert_last("element 1")
        doubly_linked_list.insert_last("element 2")
        doubly_linked_list.insert_last("element 3")
        it = doubly_linked_list.iterator()
        self.assertTrue(it.has_next())
        it.next()
        self.assertTrue(it.has_next())
        it.next()
        self.assertTrue(it.has_next())
        it.next()
        self.assertFalse(it.has_next())

    def test_next(self):
        with self.assertRaises(NoSuchElementException):
            self.iterator.next()
        self.add_elements(1)
        self.assertEqual(self.iterator.next(), "element 1")
        self.add_elements(4, shift=1)
        self.assertEqual(self.iterator.next(), "element 1")
        self.assertEqual(self.iterator.next(), "element 2")
        self.assertEqual(self.iterator.next(), "element 3")
        self.assertEqual(self.iterator.next(), "element 4")
        self.assertEqual(self.iterator.next(), "element 5")
        with self.assertRaises(NoSuchElementException):
            self.iterator.next()

    def test_rewind(self):
        self.iterator.rewind()

        self.add_elements(5)
        
        for _ in range(3):
            self.iterator.next()
        self.iterator.rewind()
        self.assertTrue(self.iterator.has_next())
        self.assertEqual(self.iterator.next(), "element 1")
    
    def test_has_previous_single(self):
        self.add_elements(1)
        self.iterator.next()
        self.assertTrue(self.iterator.has_previous())

    def test_has_previous(self):
        self.add_elements(5)
        self.assertTrue(self.iterator.has_next())
        self.assertFalse(self.iterator.has_previous())
        
        for _ in range(5):
            self.iterator.next()
            self.assertTrue(self.iterator.has_previous())
    
    def test_previous(self):
        with self.assertRaises(NoSuchElementException):
            self.iterator.previous()
        self.add_elements(5)
        for i in range(5):
            self.assertEqual(self.iterator.next(), f"element {i+1}")
        for i in range(5):
            self.assertEqual(self.iterator.previous(), f"element {5-i}")
        with self.assertRaises(NoSuchElementException):
            self.iterator.previous() 
    
    def test_previous_single_element(self):
        self.add_elements(1)
        self.iterator.next()
        self.iterator.previous()
    
    def test_previous_two_elements(self):
        self.add_elements(2)
        self.iterator.next()
        self.iterator.previous()

    def test_full_forward(self):
        self.iterator.full_forward()

        self.add_elements(5)
        self.iterator.full_forward()
        
        # Iterate to middle and rewind
        for _ in range(3):
            self.iterator.previous()
        self.iterator.full_forward()
        self.assertTrue(self.iterator.has_previous())
        self.assertEqual(self.iterator.previous(), "element 5")

        # Iterate to start and full forward
        while self.iterator.has_previous():
            self.iterator.previous()
        self.iterator.full_forward()
        self.assertTrue(self.iterator.has_previous())
        self.assertEqual(self.iterator.previous(), "element 5")

    def test_full_forward_alternative(self):
        doubly_linked_list = DoublyLinkedList()
        doubly_linked_list.insert_last("element 1")
        doubly_linked_list.insert_last("element 2")
        doubly_linked_list.insert_last("element 3")
        it = doubly_linked_list.iterator()
        it.full_forward()
        self.assertEqual(it.previous(), "element 3")
