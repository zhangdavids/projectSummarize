

# just recursion

class Node(object):
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right
        
# 中序遍历        
def mid_travelsal(root):
    if root.left is not None:
        mid_travelsal(root.right)
    print(root.value)
    if root.right is not None:
        mid_travelsal(root.right)
        
# 前序遍历
def pre_travelsal(root):
    print(root.value)
    if root.left is not None:
        pre_travelsal(root.left)
    if root.right is not None:
        pre_travelsal(root.right)
        
# 后序遍历
def post_travelsal(root):
    if root.left is not None:
        post_travelsal(root.left)
    if root.right is not None:
        post_travelsal(root.right)
    print(root.value)
