"""
链表最常见的结构 还是单链表 双链表
格子和指针表示链表结构
对比数组 数组项必须存储在连续的内存中 数组中项的逻辑顺序是和内存中的物理单元序列紧密耦合的
链表不一样 按照链表结构中一个給定项的地址和位置链接 就能够在内存中找到它的单元在何处
比如在C++中 常常以指针的形式直接访问数据
Cpython 当中 最常用的列表结构 本质上长度可变的数组（实现是数组实现 而不是链表实现）
"""

class Node(object):
    """普通节点只有后继"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class TwoWayNode(Node):
    """有前驱 也就是双链表节点"""
    def __init__(self, data, previous=None, next=None):
        Node.__init__(self, data, next)
        self.previous = previous


node1 = None
node2 = Node("A", None)
node3 = Node("B", node2)





