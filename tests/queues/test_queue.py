from abc import ABC, abstractmethod

from aed_ds.exceptions import FullQueueException, EmptyQueueException


class TestQueue(ABC):
    @abstractmethod
    def build_queue(self): pass

    def set_limit(self, limit):
        self.limit = limit
        self.build_queue()

    def add_elements(self, quantity, shift=0):
        for i in range(quantity):
            self.queue.enqueue(f"element {i+1+shift}")
    
    def remove_elements(self, quantity):
        for _ in range(quantity):
            self.queue.dequeue()

    def test_is_empty(self):
        self.assertTrue(self.queue.is_empty())
        self.add_elements(5)
        self.assertFalse(self.queue.is_empty())
    
    def test_is_full(self):
        self.set_limit(10)
        if self.queue.is_full():
            with self.assertRaises(FullQueueException):
                self.queue.enqueue("too much")
        
    def test_size(self):
        self.assertEqual(self.queue.size(), 0)
        self.add_elements(5)
        self.assertEqual(self.queue.size(), 5)
        self.remove_elements(3)
        self.assertEqual(self.queue.size(), 2)

    def test_enqueue(self):
        self.queue.enqueue("element")
        self.assertEqual(self.queue.dequeue(), "element")

    def test_dequeue(self):
        with self.assertRaises(EmptyQueueException):
            self.queue.dequeue()
        self.add_elements(5)
        for i in range(5):
            self.assertEqual(self.queue.dequeue(), f"element {i+1}")
        with self.assertRaises(EmptyQueueException):
            self.queue.dequeue()

    