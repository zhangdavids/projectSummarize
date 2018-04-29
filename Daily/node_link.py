class ListNode(object):
    def __init__(self, x, next=None):
        self.value = x
        self.next = next
        
    def get_data(self):
        return self.value
        
    def set_data(self, data):
        self.value = data
        
    def get_next_node(self):
        return self.next
        
    def set_next_node(self, data):
        self.next = data
        
    def __repr__(self):
        return self.value
        
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.size = 0
        
    def get_size(self):
        return self.size
        
    def add_node(self, data):
        new_node = ListNode(data, self.head)
        self.head = new_node
        self.size += 1
        return True
        
    # 注意指针的位置 
    def print_nodes(self):
        curr = self.head
        while curr:
            print(curr.value)
            curr = curr.get_next_node()
            
            
my_list = LinkedList()
my_list.add_node(2)
my_list.add_node(4)
my_list.add_node(3)
# print(my_list.get_size())
my_list.print_nodes()
