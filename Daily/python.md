1.斐波那契


```
def memoize(f):
    """
    计划性的缓存
    """
    call_cache = dict()

    def memoized(argument):
        try:
            return call_cache[argument]
        except KeyError:
            return call_cache.setdefault(argument, f(argument))

    return memoized


@memoize
def fibonacci(n):
    if n < 3:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':

    print(fibonacci(10))
    print(fibonacci(20))

```


2.魔法特性

    __new__是一个静态方法,而__init__是一个实例方法.
    __new__方法会返回一个创建的实例,而__init__什么都不返回.
    只有在__new__返回一个cls的实例时后面的__init__才能被调用.
    当创建一个新实例时调用__new__,初始化一个实例时用__init__.


3.闭包问题


    闭包(closure)是函数式编程的重要的语法结构。闭包也是一种组织代码的结构，它同样提高了代码的可重复使用性。

    当一个内嵌函数引用其外部作作用域的变量,我们就会得到一个闭包. 总结一下,创建一个闭包必须满足以下几点:

    必须有一个内嵌函数
    内嵌函数必须引用外部函数中的变量
    外部函数的返回值必须是内嵌函数
    
    闭包是延迟绑定


4.默认参数給空列表问题

    默认的list只在函数定义的时候被创建一次。 之后不指定list参数地调用extendList函数时，使用的都是同一个list。
    这是因为带默认参数的表达式是在函数定义的时候被计算的，而不是在函数调用时。


5.2和3的差异

    1.python2不支持的内容可以通过__future__模块导入使用
    2.print申明被print()函数取代
    3.整除
    python2 we get
    print '3 / 2 =', 3 / 2
    print '3 // 2 =', 3 // 2
    print '3 / 2.0 =', 3 / 2.0
    print '3 // 2.0 =', 3 // 2.0
    result
    3 / 2 = 1
    3 // 2 = 1
    3 / 2.0 = 1.5
    3 // 2.0 = 1.0
    3的result
    3 / 2 = 1.5
    3 // 2 = 1
    3 / 2.0 = 1.5
    3 // 2.0 = 1.0
    4.unicode
    python3 有unicode字符串 字节类 byte和bytearrays
    python2 是str字符串 unicode是单独的
    5.xrange
    惰性求值，如果你不得仅仅不遍历它一次，xrange() 函数 比 range() 更快 python2
    python3 只有range
    6.异常现在使用as关键字
    7.input（）
    在 Python 3 中已经解决了把用户的输入存储为一个 str 对象的问题。
    为了避免在 Python 2 中的读取非字符串类型的危险行为，我们不得不使用raw_input() 代替
    8.可迭代对象 而不是列表
    
    在 Python 3 中一些经常使用到的不再返回列表的函数和方法：
    zip()
    map()
    filter()
    dictionary’s .keys() method
    dictionary’s .values() method
    dictionary’s .items() method




6.垃圾回收


    主要使用引用计数（reference counting）来跟踪和回收垃圾。
    在引用计数的基础上，通过“标记-清除”（mark and sweep）解决容器对象可能产生的循环引用问题，
    通过“分代回收”（generation collection）以空间换时间的方法提高垃圾回收效率。



7. 多线程编程

```python
    from multiprocessing import Pool
    from multiprocessing.dummy import Pool

    IO密集 多线程
    CPU密集 多进程
```



8. select poll epoll


```bash
    基本上select有3个缺点:

    连接数受限
    查找配对速度慢
    数据由内核拷贝到用户态

    poll改善了第一个缺点

    epoll改了三个缺点.
```



9. python常用模块

        argparse 命令解析 用来替代optparse的命令行解析库。如果你考虑用更直观的，推荐docopt
        collections 
        functools
        glob 文件名的shell匹配
        multiprocessing 多进程
        threading 多线程
        os
        queue 队列
        SimpleHTTPServer
        subprocess

    




10.单例模式


    def singleton(cls, *args, **kw):
        instances = {}
        def getinstance():
            if cls not in instances:
                instances[cls] = cls(*args, **kw)
            return instances[cls]
        return getinstance

    @singleton
    class MyClass:
      pass


