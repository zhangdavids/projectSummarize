def f(val, I=[]):
    for i in range(val):
        I.append(i*i)
    print(I)

f1 = f(2)
f2 = f(3,[3,2,1])
f3 = f(3)

print(f1,f2,f3)

# [0, 1, 0, 1, 4]  换做 print I 又如何 [0, 1]
# [3, 2, 1, 0, 1, 4]
# [0, 1, 0, 1, 4]
