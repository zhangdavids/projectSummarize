def shell_sort(array):
    gap = len(array)
    while gap > 1:
        gap = gap // 2
        for i in range(gap, len(array)):
            for j in range(i % gap, i, gap):
                if array[i] < array[j]:
                    array[i], array[j] = array[j], array[i]
    print(array)
    return array

if __name__ == '__main__':
    shell_sort([1, 2, 4, 15, 7, 2])