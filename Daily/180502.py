# 划分
def partition(seq):
    pi, seq = seq[0], seq[1:]
    low = [i for i in seq if i <= pi]
    high = [i for i in seq if i > pi]
    return low, pi, high
    

# 选取
def select(seq, k):
    lo, pi, hi = partition(seq)
    m = len(lo)
    if m == k:
        return pi
    elif m < k:
        return select(hi, k-m-1)
    else:
        return select(lo, k)
        
        
def quicksort(seq):
    if len(seq) < 2:
        return seq
    lo, pi, hi = partition(seq)
    return quicksort(lo) + [pi] + quicksort(hi)
               
            
def main():
    import random
    seq = [random.randint(1, 20) for i in range(10)]
    
    print(quicksort(seq))
    
    
if __name__ == "__main__":
    main()
