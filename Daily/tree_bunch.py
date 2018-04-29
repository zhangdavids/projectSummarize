class Bunch(dict):
    def __init__(self, *args, **kw):
        super(Bunch, self).__init(*args, **kw)
        self.__dict__ = self
        

 //二叉树的实现
 
 T = Bunch
 t = T(left=T(left='a', right='b'), right=T(left='c'))
 
 t.left.right
 
 
