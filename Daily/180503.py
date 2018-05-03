

fib = lambda n: n if n < 2 else fib(n-1) + fib(n-2)

def fibon(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return n
    
# 合并两个有序列表
# 定义一个新的空列表
# 比较两个列表的头元素
# 小的插入到新列表 并且删除
# 直到有一个旧表为空
# 再把旧非空列表添加到新列表后面
def _recursion_merge_sort(l1, l2, tmp):
    if len(l1) == 0 or len(l2) == 0:
        tmp.extend(l1)
        tmp.extend(l2)
        return tmp
        
    else:
        if l1[0] < l2[0]:
            tmp.append(l1[0])
            del l1[0]
        else:
            tmp.append(l2[0])
            del l2[0]
            
        return _recursion_merge_sort(l1, l2, tmp)
        
def merge_sort(l1, l2):
    return _recursion_merge_sort(l1, l2, [])
