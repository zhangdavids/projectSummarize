from .node import TwoWayNode
from .abstract_list import AbstractList


class LinkedList(AbstractList):
    def __init__(self, source_collection=None):
        self._head = TwoWayNode()
        self._head.previous = self._head.next = self._head
        AbstractList.__init__(self, source_collection)

    def __iter__(self):
        cursor = self._head.next
        while cursor != self._head:
            yield cursor.data
            cursor = cursor.next

