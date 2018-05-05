class SingleTon(type):
    def __init__(cls, name, bases, dict):
        super(SingleTon, cls).__init__(name, bases, dict)
        cls._instance = None
        
    def __call__(cls, *args, **kw):
        if cls._instance is None:
            cls._instance = super(SingleTon, cls).__init__(*args, **kw)
        return cls._instance
        
        
class Test(object):
    __metaclass__ = SingleTon
    
    
# 元类的单例模式


# 使用同一个模板

class My_SingleTon(object):
    def foo(self):
        pass
        
        
my_singleton = My_SingleTon()


from mysingleton import my_singleton
my_singleton.foo()
