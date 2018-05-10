import copy

# 第一种：如果字典只有顶级对象（没有带嵌套）
d = {'name':'david','age':'22'}
c1 = copy.copy(d)       # 浅拷贝
c2 = copy.deepcopy(d)   # 深拷贝

print(id(d),id(c1),id(c2))   # 5794912 5794984 31939824   三个不同对象

d['age'] = 25
print(d,c1,c2)
# {'name': 'david', 'age': 25}
# {'name': 'david', 'age': '22'}
# {'name': 'david', 'age': '22'}

# 源对象修改值的时候，深浅拷贝的对象值没有改变

# 第二种，字典中有嵌套
d = {'name':{'first':'zhang','last':'david'},
    'job':['IT','HR']}
c1 = copy.copy(d)
c2 = copy.deepcopy(d)
print(id(d),id(c1),id(c2))    # 31157416 31940256 35946856

d['job'][0] = 'tester'
print(d,c1,c2)
# {'name': {'first': 'zhang', 'last': 'david'}, 'job': ['tester', 'HR']}
# {'name': {'first': 'zhang', 'last': 'david'}, 'job': ['tester', 'HR']}
# {'name': {'first': 'zhang', 'last': 'david'}, 'job': ['IT', 'HR']}

# 源对象修改值的时候，浅拷贝的值跟着改变，深拷贝的值没变

# 深浅拷贝都是对源对象的复制，占用不同的内存空间
# 如果源对象只有一级目录的话，源做任何改动，不影响深浅拷贝对象
# 如果源对象不止一级目录的话，源做任何改动，都要影响浅拷贝，但不影响深拷贝
# 序列对象的切片其实是浅拷贝，即只拷贝顶级的对象
