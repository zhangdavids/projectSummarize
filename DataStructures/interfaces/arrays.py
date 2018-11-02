"""
数组结构 一般情况下的数组 只能存储数字
实现基本包括 长度 字符串表示
注意 for 循环 本质调用的是 __iter__方法
创建的时候 需要指定数组的大小（容量）或者是物理大小

一般还可能需要实现 比如数组大小 不够 动态调整
删除很多元素 装载因子达到某个阀值 调小一些
目前想到的就这些
"""

class Array(object):
    def __init__(self, capacity, filled_value=None):
        self._items = list()
        for count in range(capacity):
            self._items.append(filled_value)

    def __len__(self):
        return len(self._items)

    def __str__(self):
        return str(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, key, value):
        self._items[key] = value


