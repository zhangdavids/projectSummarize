# 代理 使用全局机制来标记和注册函数
# 常用于web框架 提供装饰器来保护函数访问的安全 举例 @protect('admin')

class User(object):
    def __init__(self, roles):
        self.roles = roles
        
        
class Unauthorized(Exception):
    pass
    
    
def protect(role):
    def _protect(function):
        def __protect(*args, **kw):
            user = globals().get('user')
            if user is None or role not in user.roles:
                raise Unauthorized("I won't tell you")
            return function(*args, **kw)
        return __protect
    return _protect
