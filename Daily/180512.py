import time
from functools import wraps


def timer(func):
    @wraps(func)
    def wrapper(*args, **kw):
        start_time = time.time()
        func(*args, **kw)
        stop_time = time.time()
        print("it costs %s run time %s (s)"%(func.__name__, stop_time-start_time))
        return func(*args, **kw)
    return wrapper
    
    
    
# 写一个计算函数执行时间的装饰器 不失去原始名称和文档字符串的解决方案

# 不能修改被装饰的函数的源代码
# 不能修改被装饰的函数的调用方式
# 满足上面的两种情况下给程序增添功能
