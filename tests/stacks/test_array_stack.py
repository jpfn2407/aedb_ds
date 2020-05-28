import unittest

from .test_stack import TestStack
from aed_ds.stacks.array_stack import ArrayStack


class TestArrayStack(TestStack, unittest.TestCase):
    def build_stack(self):
        self.stack = ArrayStack(self.limit)
    
    def setUp(self):
        self.set_limit(10)