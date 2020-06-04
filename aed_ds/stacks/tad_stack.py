from abc import ABC, abstractmethod


class Stack(ABC):
    # Returns true iff the stack contains no elements.
    @abstractmethod
    def is_empty(self): pass

    # Returns true iff the stack cannot contain more elements.
    @abstractmethod
    def is_full(self): pass

    # Returns the number of elements in the stack.
    @abstractmethod
    def size(self): pass

    # Returns the element at the top of the stack.
    # Throws EmptyStackException
    @abstractmethod
    def top(self): pass

    # Inserts the specified element onto the top of the stack.
    # Throws FullStackException
    @abstractmethod
    def push(self, element): pass

    # Removes and returns the element at the top of the stack.
    # Throws EmptyStackException
    @abstractmethod
    def pop(self): pass
