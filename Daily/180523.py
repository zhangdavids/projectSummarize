

# 延迟求值

class Lazy_property(object):
    def __init__(self, function):
        self.fget = function
        
    def __get__(self, obj, cls):
        value = self.fget(obj)
        setattr(obj, self.fget.__name__, value)
        return value
