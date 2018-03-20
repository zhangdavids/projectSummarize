#coding:utf-8
def quicksort(list):
    if len(list)<2:
        return list
    else:
        midpivot = list[0]
        left = [i for i in list[1:] if i<=midpivot]
        right = [i for i in list[1:] if i > midpivot]
        finallylist = quicksort(left)+[midpivot]+quicksort(right)
        return finallylist

if __name__ == '__main__':

    print(quicksort([2,4,6,7,1,2,5]))