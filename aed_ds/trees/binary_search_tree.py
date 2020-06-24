from .tad_tree import Tree
from ..dictionaries.tad_ordered_dictionary import OrderedDictionary
from ..exceptions import DuplicatedKeyException, NoSuchElementException, \
    EmptyDictionaryException, EmptyTreeException
from .nodes.binary_nodes import BinarySearchTreeNode


class BinarySearchTree(OrderedDictionary, Tree):
    def __init__(self):
        self.root = None
        self.tree_height = 0
        self.count = 0

    # Returns the number of elements in the dictionary.
    def size(self):
        return self.count

    # Returns true if the dictionary is full.
    def is_full(self):
        return False

    # Returns the value associated with key k.
    # Throws NoSuchElementException
    def get(self, k):
        if self.get_element(self.root, k) == None:
            raise NoSuchElementException()
        else:
            return self.get_element(self.root, k).get_element() 

    def get_element(self, root, k):
        if root == None:
            return None
        elif root.get_key() == k:
            return root.get_element()
        elif root.get_key() < k:
            root = self.get_element(root.get_left_child(), k)
        else:
            root = self.get_element(root.get_right_child(), k)
        return root       

    # Inserts a new value, associated with key k.
    # Throws DuplicatedKeyException
    def insert(self, k, v):
        self.root = self.insert_element(self.root, k, v)

    def insert_element(self, root, k, v):
        if root is None:
            root = BinarySearchTreeNode(k, v)
            self.count += 1
        else:
            if root.get_key() == k:
                raise DuplicatedKeyException()
            elif root.get_key() > k:
                node = self.insert_element(root.get_left_child(), k, v)
                root.set_left_child(node)
            else:
                node = self.insert_element(root.get_right_child(), k, v)
                root.set_right_child(node)
        return root

    # Updates the value associated with key k.
    # Throws NoSuchElementException
    def update(self, k, v): pass

    # Removes the key k, and the value associated with it.
    # Throws NoSuchElementException
    def remove(self, k): pass

    # Returns a List with all the keys in the dictionary.
    def keys(self): pass

    # Returns a List with all the values in the dictionary.
    def values(self): pass

    # Returns a List with all the key value pairs in the dictionary.
    def items(self): pass

    # Returns an iterator of the elements in the dictionary
    def iterator(self): pass

    # Returns the element with the smallest key
    # Throws EmptyTreeException
    def get_min_element(self):
        if self.is_empty():
            raise EmptyDictionaryException()
        return self.get_min_node(self.root).get_element()

    def get_min_node(self, root):
        if root.get_left_child() is None:
            return root
        return self.get_min_node(root.get_left_child())

    # Returns the element with the largest key
    # Throws EmptyTreeException
    def get_max_element(self):
        if self.is_empty():
            raise EmptyDictionaryException()
        return self.get_max_node(self.root).get_element()

    def get_max_node(self, root):
        if root.get_right_child() is None:
            return root
        return self.get_max_node(root.get_right_child())

    # Returns the root of the tree
    # Throws EmptyTreeException
    def get_root(self):
        if self.is_empty():
            raise EmptyTreeException()
        else:
            return self.root.get_element()

    # Returns the height of the tree
    # Throws EmptyTreeException
    def height(self):
        if self.is_empty():
            raise EmptyTreeException()
        else:
            return self.tree_height

    # Returns True if the tree is empty
    def is_empty(self): 
        return self.count == 0
    