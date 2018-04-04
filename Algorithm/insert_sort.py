def insert_sort(array):
    """
    时间复杂度：n^2
    空间复杂度： 1
    稳定
    :param array:
    :return:
    """
    for i in range(len(array)):
        for j in range(i):
            if array[i] < array[j]:
                array.insert(j, array.pop(i))
                break
    print(array)
    return array


if __name__ == '__main__':
    insert_sort([1, 2, 4, 5, 7, 2])