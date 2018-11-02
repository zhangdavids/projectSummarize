from .arrays import Array


"""
数组类型的 先分配一个固定大小的
如果不够 再进行调整
"""
class ArrayBag(object):
    DEFAULT_CAPACITY = 10

    def __init__(self, source_collections=None):
        self._items = Array(ArrayBag.DEFAULT_CAPACITY)
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
        cursor = 0
        while cursor < len(self):
            yield self._items[cursor]
            cursor += 1

    def __add__(self, other):
        result = ArrayBag(self)
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
        self._items = Array(ArrayBag.DEFAULT_CAPACITY)

    def add(self, item):
        self._items[(len(self))] = item
        self._size += 1

    def remove(self, item):
        if item not in self:
            raise KeyError(str(item) + " not in bag")
        target_index = 0
        for target_item in self:
            if target_item == item:
                break
            target_index += 1

        for i in range(target_index, len(self) - 1):
            self._items[i] = self._items[i + 1]
        self._size -= 1
