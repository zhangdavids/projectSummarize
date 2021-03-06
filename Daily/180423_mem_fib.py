
# 计划性的缓存

def memoize(function):
    call_cache = dict()
    
    def memoized(argument):
        try:
            return call_cache[argument]
        except KeyError:
            return call_cache.setdefault(argument, function(argument))
            
    return memoized

    
@memoize    
def fibonacci(n):
    if n < 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
        
        
print(fibonacci(10))
