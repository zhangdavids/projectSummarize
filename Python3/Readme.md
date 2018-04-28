## 如何才是一个高级 python 程序员  

对python的理解划分

### python 语言基础
python文件是如何运行的

python的数据结构有哪些
tuple list dict

模块和函数

字符串

正则

处理文件

面向对象编程

异常处理以及程序调试

数据库编程  常用mysql数据库 

### GUI开发

tkinter

### web开发

涉及到html xml相关知识

django flask 框架

### 其他应用

测试驱动开发 TDD

并发处理 线程 进程 协程

python 的系统管理

增强式的交互环境

网络编程

常见的网络应用

+ ftp
+ http
+ 获取发送邮件
+ telnet远程登录
+ snmp管理网络
+ 网络分析

图像处理

语言扩展




###  先谈一谈 python2 和 python3 的差异  

+ 首先是 print，不再是一条语句，而是函数，因此必须加上括号
+ 捕获异常的方法改为 except exc as var 
+ 弃用比较运算符 <>， 改用 != 
+ from module import * 只能用于模块，不能用于函数
+ 不以点字符开头的都被当作绝对导入
+ sorted 函数与列表的 sort 方法不再接受 cmp 函数，应该用 key 函数来替代
+ 整数除法返回的是浮点数。取整可以使用 // 运算符。
+ 所有的字符串都是 Unicode，字节 bytes 需要加一个 b 或者 B 的前缀
+ 兼容性产生的问题  
  * 使用 \__future__ 模块将新版本里的功能反向迁移到旧版本当中，具体有 division, absolute\_import, print\_function, unicode\_literals

**标准库中也有很多变化**


### 使用环境隔离非常重要

1. virtualenv

2. venv (python3.3+)


### python 语法实践

#### 1. 内置类型 

##### 1.1 字符串与字节

python3 当中保存文本信息的数据类型是 str（字符串），保存的是 Unicode 码位。  
python2 当中对应的是字节字符串，这种类型现在用 bytes 对象来处理。

举例如下：  

\>>> print(bytes([102, 111, 111]))  
b'foo'  

\>>>list(b'foo bar')  
[102, 111, 111, 32, 98, 97, 114]

需要注意的细节： 尽量使用 .join()来实现字符串的拼接，而不是 +  


##### 1.2 集合类型

+ 列表 list
+ 元组 tuple
+ 字典 dictionary
+ 集合 set

元组不可变的，可以哈希  
列表在 CPython 中实际上可以理解成为长度可变的数组  
使用列表推导式更高效，更简洁  
使用枚举 enumerate  

字典：  
python3 keys() values() items() 返回的不再是列表，而是视图对象  

字典推导式：  

```python
squares = {number: number**2 for number in range(100)}
```

集合  

set() 和 frozenset()  

超越基础集合类型：  

+ namedtuple 用于创建元组子类的工厂函数  
+ deque 双端队列
+ ChainMap 类似字典的类，用于创建多个映射的单一视图
+ Counter 字典子类，计数
+ OrderedDict 有序字典
+ defaultdict 默认字典  设置缺失值


#### 2. 高级语法

+ 迭代器 iterator
+ 生成器 generator
+ 装饰器 decorator
+ 上下文管理器 context manager  


基于两个方法：  
\__next__ 返回容器的下一个元素  
\__iter__ 返回迭代器本身  

生成器基于 yield 语句，可以暂停函数并返回一个中间结果。  生成器的一个重要特性是利用 next 函数与调用的代码进行交互。  

装饰器的作用是使函数包装与方法包装（一个函数，接受函数并返回其增强函数）变得更加容易阅读和理解。  

with 语句使用场景  

+ 关闭一个文件  
+ 释放一个锁
+ 创建一个临时的代码补丁
+ 在特殊环境中运行受保护的代码  

### python 类的语法实践   

super（）函数，python2 的工作原理几乎完全相同，调用签名的唯一区别在于简化的零参数形式不可用，因此必须始终提供至少一个参数。  

新式类，所有类继承自 object  

**理解 python 方法的解析顺序**  

\__mor__

旧式类是深度优先

*新式类是广度优先（挑选最接近的祖先的方法），C3序列化*



描述符  

基于三个特殊方法

```
__set__()
__get__()
__delete__()
```

property 提供了一个内置的描述符类型，它知道如何将一个属性链接到一组方法上。  

槽（slots）  

允许使用\__slots__属性来指定的类设置一个静态属性列表。  


### 代码的管理

github 或者 是自建的 gitlab

github 工作流

需要持续集成（测试每一个提交）

持续交付 


### 项目文档化

** 文档和代码一样重要 **

### 代码优化

三个规则

+ 首先要能工作
+ 从用户的角度考虑
+ 保存代码的可读性和可维护性

查找瓶颈

+ cpu
+ 内存
+ 网络使用情况

** 如何降低复杂度 **

使用内置的集合模块

+ deque
+ defaultdict
+ namedtuple

架构体系的权衡

+ 使用任务队列 celery 等
+ 使用概率型数据结构


缓存

+ 确定型缓存
+ 非确定型缓存
+ 缓存服务

### 并发


多线程 适合于 IO 密集任务
多进程 适合于 CPU 密集任务


python 创始人 不建议使用 gevent 因为使用了 猴子补丁

在3.5版本之后 对异步编程有着重要的支持 asyncio

```python3.5
import time
import asyncio
import random

#  协程函数
async def waiter(name):
    for _ in range(4):
        time_to_sleep = random.randint(1, 3) / 4
        await asyncio.sleep(time_to_sleep)
        print(
            "{} waited {} seconds"
            "".format(name, time_to_sleep)
        )
        
# await 关键字 用于等待协程或者未来的结果并释放对事件循环的执行控制        
async def main():
    await asyncio.wait([waiter('foo'), waiter('bar')])
    
    
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
```


### python 当中常用的设计模式

创建型 生成具有特定行为的对象

+ 工厂设计模式
+ 单例

结构型 为特定的用例构建代码

+ 适配器

```
from os.path import split, splitext


class CoreAdapter(object):
    def __init__(self, filename):
        self._filename = filename
        
    @property
    def title(self):
        return splitext(split(self._filename)[-1])[0]
        
    @property
    def languages(self):
        return ("cn",)
        
    def __getitem__(self, item):
        return getattr(self, item, "Unknown")
        
        
class CoreInfo(object):
    def summary(self, dc_dict):
        print("Title: %s" % dc_dict['title'])
        print("Languages: %s" % ", ".join(dc_dict['languages']))
        print("Creator: %s" % dc_dict['creator'])
        
        
def main():
    adapted = CoreAdapter('example.txt')
    infos = CoreInfo()
    infos.summary(adapted)
    
    
if __name__ == "__main__":
    main()
```

+ 外观

```
# 提供对子系统的高层次简单地访问

```

+ 代理

```
# 提供对昂贵或者远程资源的访问
# 另外的使用范例是数据唯一性

class Url(object):
    def __init__(self, location):
        self._url = urlopen(location)
        
    def headers(self):
        return dict(self._url.headers.items())
        
    def get(self):
        return self._url.read()        

```

行为模式 分配责任和封装行为

+ 观察者

```
pass
```

+ 访问者

```
pass
```

+ 模板

```
pass
```








