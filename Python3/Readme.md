## 如何才是一个高级 python 程序员  


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

** 标准库中也有很多变化 **


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


描述符  

property 提供了一个内置的描述符类型，它知道如何将一个属性链接到一组方法上。  

槽（slots）  

允许使用\__slots__属性来指定的类设置一个静态属性列表。  

待续...







