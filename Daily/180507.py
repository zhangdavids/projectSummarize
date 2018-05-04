
# 哈夫曼算法

from heapq import heapify, heappush, heappop
from itertools import count


def huffman(seq, frq):
    num = count()
    print(num)
    trees = list(zip(frq, num, seq))
    print(trees)
    heapify(trees)
    while len(trees) > 1:
        fa, _, a = heappop(trees)
        fb, _, b = heappop(trees)
        n = next(num)
        heappush(trees, (fa+fb, n, [a, b]))
    print()  
    print(trees) 
    return trees[0][-1]
       
        
def main():
    seq = "abcdefghi"    
    frq = [4, 5, 6, 9, 11, 12, 15, 16, 20]
    print(huffman(seq, frq))
    

if __name__ == "__main__":
    pass
    main()
          
