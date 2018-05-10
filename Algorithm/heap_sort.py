#coding: utf-8 
#!/usr/bin/python   
import random
import math

# 随机生成0~100之间的数值
def get_andomNumber(num):  
    lists=[]  
    i=0  
    while i<num:  
        lists.append(random.randint(0,100))  
        i+=1
    return lists


# 调整堆
def adjust_heap(lists, i, size):
    lchild = 2 * i + 1
    rchild = 2 * i + 2
    max = i
    if i < size / 2:
        if lchild < size and lists[lchild] > lists[max]:
            max = lchild
        if rchild < size and lists[rchild] > lists[max]:
            max = rchild
        if max != i:
            lists[max], lists[i] = lists[i], lists[max]
            adjust_heap(lists, max, size)

# 创建堆
def build_heap(lists, size):
    for i in range(0, (int(size/2)))[::-1]:
        adjust_heap(lists, i, size)

# 堆排序
def heap_sort(lists):
    size = len(lists)
    build_heap(lists, size)
    for i in range(0, size)[::-1]:
        lists[0], lists[i] = lists[i], lists[0]
        adjust_heap(lists, 0, i)
    return lists


a = get_andomNumber(10)
print("排序之前：%s" %a)

b = heap_sort(a)

print("排序之后：%s" %b)
