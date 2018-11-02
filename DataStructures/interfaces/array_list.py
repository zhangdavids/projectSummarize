from .arrays import Array
from .abstract_list import AbstractList
from .array_list_iterator import ArrayListIterator


class ArrayList(AbstractList):
    DEFAULT_CAPACITY = 10

    def __init__(self, source_collections=None):
        self._items = Array(ArrayList.DEFAULT_CAPACITY)
        AbstractList.__init__(self, source_collections)

    def __iter__(self):
        cursor = 0
        while cursor < len(self):
            yield self._items[cursor]
            cursor += 1

    def __getitem__(self, i):
        if i < 0 or i >= len(self):
            raise IndexError("List index out of range")
        return self._items[i]

    def __setitem__(self, key, value):
        if key < 0 or key >= len(self):
            raise IndexError("List index out of range")
        self._items[key] = value

    def insert(self, key, value):
        if key < 0:
            key = 0
        elif key >= len(self):
            key = len(self)
        elif key < len(self):
            for j in range(len(self), key, -1):
                self._items[j] = self._items[j-1]
        self._items[key] = value
        self._size += 1
        self.inc_mod_count()




    def pop(self):
        pass

    def list_iterator(self):
        pass

