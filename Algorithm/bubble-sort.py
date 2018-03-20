
def bubble_sort(array):
    for i in range(len(array))[::-1]:
        for j in range(i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

    print(array)
    # return array

if __name__ == '__main__':
    array = [1, 2, 3, 6, 5, 4]
    bubble_sort(array)
