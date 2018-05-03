

from collections import defaultdict


n, k = 10, 7
C = defaultdict(int)
for row in range(n+1):
    C[row, 0] = 1
    for col in range(1, k+1):
        C[row, col] = C[row-1, col] +  C[row-1, col-1]

print(C)      
print(C[10, 7])
