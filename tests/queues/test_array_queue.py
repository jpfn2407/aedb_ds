import unittest

from aed_ds.queues.array_queue import ArrayQueue
from .test_queue import TestQueue

class TestArrayQueue(unittest.TestCase, TestQueue):
    def build_queue(self):
        self.queue = ArrayQueue(self.limit)

    def setUp(self):
        self.limit = 10
        self.build_queue()