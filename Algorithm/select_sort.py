# 选择排序
def select_sort(array):
    count = len(array)
    for i in range(0, count):
        min = i
        for j in range(i + 1, count):
            if array[min] > array[j]:
                min = j
        temp = array[min]
        array[min] = array[i]
        array[i] = temp
        # array[min], array[i] = array[i], array[min]  
        # 注意上面注释的写法才是python式的写法  
    return array
