# 上下文管理器 with语句 上下文管理器协议

class ContextIllustration:
    def __enter__(self):
        print("entering context")
        
    def __exit__(self, exc_type, exc_value, traceback):
        print("leaving context")
        
        if exc_type is None:
            print("with no error")
        else:
            print("with an error (%s)" % exc_value)
            
            
# 没有引发异常时的运行结果如下：
# >>> with ContextIllustration():
#         print("inside")
        
# ...
# entering context
# inside
# leaving context
# with no error
        
