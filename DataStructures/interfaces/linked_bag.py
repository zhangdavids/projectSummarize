from .node import Node


class LinkedBag(object):
    def __init__(self, source_collections=None):
        self._items = None
        self._size = 0
        if source_collections:
            for item in source_collections:
                self.add(item)

    def is_empty(self):
        return len(self) == 0

    def __len__(self):
        return self._size

    def __str__(self):
        return "{" + ", ".join(map(str, self)) + "}"

    def __iter__(self):
        cursor = self._items
        while cursor is not None:
            yield cursor.data
            cursor = cursor.next

    def __add__(self, other):
        result = LinkedBag(self)
        for item in other:
            result.add(item)
        return result

    def __eq__(self, other):
        if self is other:
            return True
        if type(self) != type(other) or len(self) != len(other):
            return False
        for item in self:
            if item not in other:
                return False

        return True

    def clear(self):
        self._size = 0
        self._items = Node()

    def add(self, item):
        self._items = Node(item, self._items)
        self._size += 1

    def remove(self, item):
        if item not in self:
            raise KeyError(str(item) + " not in bag")

        probe = self._items
        trailer = None
        for i in self:
            if i == item:
                break
            trailer = probe
            probe = probe.next

        if probe == self._items:
            self._items = self._items.nex
        else:
            trailer.next = probe.next
        self._size -= 1

