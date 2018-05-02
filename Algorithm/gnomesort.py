def gnomesort(seq):
    i = 0
    while i < len(seq):
        if i == 0 or seq[i-1] <= seq[i]:
            i += 1
        else:
            seq[i], seq[i-1] = seq[i-1], seq[i]
            i -= 1
            
            
def main():
    import random
    seq = [random.randint(1, 20) for i in range(10)]
    gnomesort(seq)
    print(seq)
    
    
if __name__ == "__main__":
    main()
