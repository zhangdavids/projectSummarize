#! usr/bin/env python
# _*_ coding: utf-8 _*_
__author__ = 'john cheung, zhangjohn202@gmail.com'
__mtime__ = '2018/4/4'


def F(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return F(n-1)+F(n-2)


from math import sqrt
def f(n):
    return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))


def fib():
    a,b = 0,1
    while True:
        yield a
        a, b = b, a + b


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