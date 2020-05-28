import unittest

from aed_ds.queues.list_queue import ListQueue
from .test_queue import TestQueue

class TestListQueue(unittest.TestCase, TestQueue):
    def build_queue(self):
        self.queue = ListQueue()

    def setUp(self):
        self.build_queue()