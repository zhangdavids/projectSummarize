import time
from functools import wrap


def timer(func):
    @wrap
    def wrapper():
        start_time = time.time()
        func()
        stop_time = time.time()
        print("it costs %s run time %s (s)"%(func.__name__, stop_time-start_time))
    return wrapper
    
    
    
# 写一个计算函数执行时间的装饰器
