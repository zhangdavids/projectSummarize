#! usr/bin/env python
# _*_ coding: utf-8 _*_
__author__ = 'john cheung, zhangjohn202@gmail.com'
__mtime__ = '2018/4/4'


# 直接递归
def F(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return F(n-1)+F(n-2)

# 数学公式
from math import sqrt
def f(n):
    return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))

# 生成器语法
def fib():
    a,b = 0,1
    while True:
        yield a
        a, b = b, a + b

## Using looping technique
def fibon(n):
    a, b = 1, 1
    for i in range(n - 1):
        a, b = b, a + b
    return a

# Using memoization
def memoize(fn, arg):
    memo = {}
    if arg not in memo:
        memo[arg] = fn(arg)
        return memo[arg]

fibm = memoize(fibon, 5)
print(fibm)


# Using memoization as decorator
class Memoize:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}

    def __call__(self, arg):
        if arg not in self.memo:
            self.memo[arg] = self.fn(arg)
            return self.memo[arg]


@Memoize
def fibonacci(n):
    a, b = 1, 1
    for i in range(n - 1):
        a, b = b, a + b
    return a



# 0:   0
# 1:   1
# 2:   1
# 3:   2
# 4:   3
# 5:   5
# 6:   8
# 7:  13
# 8:  21
# 9:  34
# 10:  55