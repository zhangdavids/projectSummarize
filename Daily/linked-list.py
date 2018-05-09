

def revese(node):
    p = node
    cur = node.next
    p.next = None
    while cur:
        tmp = cur.next
        cur.next = p
        p = cur
        cur = tmp
    return p
    
    
    
# 单链表逆置
