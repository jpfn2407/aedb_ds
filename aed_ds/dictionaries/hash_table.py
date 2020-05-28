from .tad_dictionary import Dictionary
from ..exceptions import NoSuchElementException, DuplicatedKeyException
from ..lists.singly_linked_list import SinglyLinkedList
from .item import Item
import ctypes

class HashTable(Dictionary):
    def __init__(self, size=101):
        self.array_size = size
        self.num_elements = 0
        self.table = (self.array_size * ctypes.py_object)() # Array of pointers

        # Create an empty list for each table position
        for i in range(self.array_size):
            self.table[i] = SinglyLinkedList()

    def size(self):
        return self.num_elements

    def is_full(self):
        return self.num_elements == self.array_size

    def get(self, k):
        if not self.has_key(k):
            raise NoSuchElementException()

        idx = self.hash_function(k)
        colision_list = self.table[idx]
        it = colision_list.iterator()
        while it.has_next():
            current_item = it.next()
            if current_item.get_key() == k:
                return current_item.get_value()

    def insert(self, k, v):
        # Check if it has key
        if self.has_key(k):
            raise DuplicatedKeyException()
        
        # Check if it's not full
        elif not self.is_full():
            ## Insert new item
            # Calculate the table index
            idx = self.hash_function(k) # O(1)
            # Create a new Item
            item = Item(k, v)
            # Insert the item in the colision list
            self.table[idx].insert_last(item)
            # Update the number of elements
            self.num_elements += 1    

    def update(self, k, v):
        if not self.has_key(k):
            raise NoSuchElementException()

        idx = self.hash_function(k)
        colision_list = self.table[idx]
        it = colision_list.iterator()
        while it.has_next():
            current_item = it.next()
            if current_item.get_key() == k:
                current_item.set_value(v)    

    def remove(self, k):
        if not self.has_key(k):
            raise NoSuchElementException()

        idx = self.hash_function(k)
        colision_list = self.table[idx]
        it = colision_list.iterator()
        i = 0
        while it.has_next():
            current_item = it.next()
            if current_item.get_key() == k:
                #self.table[idx].get(i)
                self.table[idx].remove(i)
                self.num_elements -= 1
            i+=1    

    def keys(self):
        key_list = SinglyLinkedList()
        for i in range(self.array_size):
            colision_list = self.table[i]
            it = colision_list.iterator()
            while it.has_next():
                current_item = it.next()
                key_list.insert_last(current_item.get_key())
        return key_list

    def values(self):
        value_list = SinglyLinkedList()
        for i in range(self.array_size):
            colision_list = self.table[i]
            it = colision_list.iterator()
            while it.has_next():
                current_item = it.next()
                value_list.insert_last(current_item.get_value())
        return value_list

    def items(self):
        item_list = SinglyLinkedList()
        for i in range(self.array_size):
            colision_list = self.table[i]
            it = colision_list.iterator()
            while it.has_next():
                current_item = it.next()
                item_list.insert_last(current_item)
        return item_list

    def hash_function(self, k):
        return sum([ord(c) for c in k]) % self.array_size

    def has_key(self, k):
        idx = self.hash_function(k) # O(1)    
        colision_list = self.table[idx]
        it = colision_list.iterator()
        while it.has_next():
            current_item = it.next()
            if current_item.get_key() == k:
                return True
        return False
