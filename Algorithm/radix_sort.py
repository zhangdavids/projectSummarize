import math


def radix_sort(array, radix=10):
    k = int(math.ceil(math.log(max(array), radix)))
    bucket = [[] for i in range(radix)]
    for i in range(1, k+1):
        for j in array:
            bucket[int(j/(radix**(i-1)) % (radix))].append(j)
        del array[:]
        for z in bucket:
            array += z
            del z[:]
    return array
