def two_sum(num, target):
    d = dict()
    for i in range(len(num)):
        x = num[i]
        if target-x in d:
            return (d[target-x], i)
        d[x] = i


print(two_sum([2,7,11,15], 17))


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        # yield b
        print(b)
        a, b = b, a+b


print(fib(10))


def fibon():
    a, b = 0, 1
    while 1:
        yield b
        a, b = b, a+b
