from abc import ABC, abstractmethod

from aed_ds.exceptions import FullStackException, EmptyStackException


class TestStack(ABC):
    @abstractmethod
    def build_stack(self): pass

    def set_limit(self, limit):
        self.limit = limit
        self.build_stack()

    def push_elements(self, quantity, shift=0):
        for i in range(quantity):
            self.stack.push(f"element {i+1+shift}")
    
    def pop_elements(self, quantity):
        for _ in range(quantity):
            self.stack.pop()

    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty())
        self.push_elements(5)
        self.assertFalse(self.stack.is_empty())
    
    def test_is_full(self):
        self.set_limit(10)
        if self.stack.is_full():
            with self.assertRaises(FullStackException):
                self.stack.enqueue("too much")
        
    def test_size(self):
        self.assertEqual(self.stack.size(), 0)
        self.push_elements(5)
        self.assertEqual(self.stack.size(), 5)
        self.pop_elements(3)
        self.assertEqual(self.stack.size(), 2)
    
    def test_top(self):
        with self.assertRaises(EmptyStackException):
            self.stack.top()
        self.push_elements(5)
        self.assertEqual(self.stack.top(), "element 5")
        self.pop_elements(1)
        self.assertEqual(self.stack.top(), "element 4")
    
    def test_push(self):
        if self.stack.is_full():
            with self.assertRaises(FullStackException):
                self.push()
        self.set_limit(5)
        self.assertEqual(self.stack.size(), 0)
        self.push_elements(5)
        self.assertEqual(self.stack.size(), 5)
        if self.stack.is_full():
            with self.assertRaises(FullStackException):
                self.stack.push("extra element")
        self.pop_elements(1)
        self.assertEqual(self.stack.size(), 4)
        self.stack.push("last element")
        self.assertEqual(self.stack.size(), 5)
        if self.stack.is_full():
            with self.assertRaises(FullStackException):
                self.stack.push("extra element")
    
    def test_pop(self):
        with self.assertRaises(EmptyStackException):
            self.stack.pop()
        self.assertEqual(self.stack.size(), 0)
        self.push_elements(5)
        self.assertEqual(self.stack.size(), 5)
        self.assertEqual(self.stack.pop(), "element 5")
        self.assertEqual(self.stack.size(), 4)
        self.assertEqual(self.stack.pop(), "element 4")
        self.pop_elements(3)
        with self.assertRaises(EmptyStackException):
            self.stack.pop()
        